"""Module for the WalletBalanceClient class."""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

import httpx
from environs import Env
from web3 import AsyncWeb3

from app_logger import get_logger
from constants import NETWORKS

if TYPE_CHECKING:
    import logging


class WalletBalanceClient:
    """Client for fetching exchange rates and getting wallet balance."""

    _exchange_rates_url = "https://api.coingecko.com/api/v3/simple/price"

    def __init__(
        self,
        network: str = "ETH",
    ) -> None:
        """Initialize the client."""
        self._url = NETWORKS[network]["url"]
        self._native_token = NETWORKS[network]["native_token"]

    async def fetch_rate(self, to_currency: str = "usd") -> float:
        """Fetch the exchange rate."""
        params = {
            "ids": self._native_token,
            "vs_currencies": to_currency,
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(
                self._exchange_rates_url,
                params=params,
            )

        response.raise_for_status()

        data = response.json()
        return data[self._native_token][to_currency]

    async def read_balance(self, address: str) -> float:
        """Read wallet balance."""
        w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(self._url))

        if not await w3.is_connected():
            message = f"Failed to connect to {self._url}"
            raise ConnectionError(message)

        checksum_address = w3.to_checksum_address(address)
        balance_wei = await w3.eth.get_balance(checksum_address)

        return float(w3.from_wei(balance_wei, "ether"))


async def _fetch_rate(
    client: WalletBalanceClient,
    logger: logging.Logger,
) -> None:
    """Async function to check the exchange rate."""
    rate = await client.fetch_rate()

    logger.info(f"Exchange rate is {rate}")


async def _read_balance(
    client: WalletBalanceClient,
    address: str,
    logger: logging.Logger,
) -> None:
    """Async function to read the wallet balance."""
    balance = await client.read_balance(address)

    logger.info(f"Balance of {address} is {balance:.2f} ETH")


async def main() -> None:
    """Async main function."""
    env = Env()
    env.read_env()

    address: str = env.str(
        "ADDRESS",
        "0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5",
    )

    logger = get_logger(__name__)

    client = WalletBalanceClient()

    rate_task = _fetch_rate(logger=logger, client=client)
    balance_task = _read_balance(logger=logger, client=client, address=address)

    await asyncio.gather(balance_task, rate_task)


if __name__ == "__main__":
    asyncio.run(main())
