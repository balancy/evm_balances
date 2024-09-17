"""App module."""

from __future__ import annotations

import asyncio
from typing import Any

from litestar import Litestar, get, status_codes
from litestar.config.cors import CORSConfig

from constants import NETWORKS
from wallet_balance_client import WalletBalanceClient

cors_config = CORSConfig(
    allow_origins=[
        "*",
    ],
)


@get("/")
async def index() -> str:
    """Index page."""
    return "Hello, guest!"


@get("/balances", sync_to_thread=True)
async def get_balance(
    network: str,
    address: str,
) -> tuple[dict[str, Any], int]:
    """Get wallet balance."""
    if network not in NETWORKS:
        return {
            "status": f"Unsupported network: {network}",
        }, status_codes.HTTP_400_BAD_REQUEST

    client = WalletBalanceClient(network=network)

    balance_task = client.read_balance(address=address)
    rate_task = client.fetch_rate()

    results = await asyncio.gather(balance_task, rate_task)

    balance, rate = results

    return {"balance": round(balance * rate, 2)}, status_codes.HTTP_200_OK


app = Litestar(route_handlers=[index, get_balance], cors_config=cors_config)
