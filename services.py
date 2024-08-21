"""Services module."""

from __future__ import annotations

from typing import TYPE_CHECKING

from environs import Env

if TYPE_CHECKING:
    from decimal import Decimal

import logging

import web3

PUBLIC_RPC_URL = "https://cloudflare-eth.com"


def read_balance(address: str) -> int | Decimal:
    """Read wallet balance."""
    w3 = web3.Web3(web3.HTTPProvider(PUBLIC_RPC_URL))
    checksum_address = w3.to_checksum_address(address)
    balance_wei = w3.eth.get_balance(checksum_address)
    return w3.from_wei(balance_wei, "ether")


if __name__ == "__main__":
    env = Env()
    env.read_env()

    address: str = env.str(
        "ADDRESS",
        "0x95222290DD7278Aa3Ddd389Cc1E1d165CC4BAfe5",
    )
    balance = read_balance(address)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s: %(message)s")
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    logger.info(f"Balance of {address} is {balance:.2f} ETH")
