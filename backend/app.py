"""App module."""

from __future__ import annotations

from decimal import Decimal

from litestar import Litestar, get
from litestar.config.cors import CORSConfig

from services import read_balance

cors_config = CORSConfig(allow_origins=["*"])


@get("/")
async def index() -> str:
    """Index page."""
    return "Hello, guest!"


@get("/balances/{address:str}")
async def get_balance(address: str) -> dict[str, int | Decimal]:
    """Get wallet balance."""
    return {"balance": read_balance(address)}


app = Litestar(route_handlers=[index, get_balance], cors_config=cors_config)
