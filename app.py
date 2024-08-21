"""App module."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from decimal import Decimal

from litestar import Litestar, get

from services import read_balance


@get("/")
async def index() -> str:
    """Index page."""
    return "Hello, guest!"


@get("/balances/{address:str}")
async def get_balance(address: str) -> dict[str, int | Decimal]:
    """Get wallet balance."""
    return {"balance": read_balance(address)}


app = Litestar([index, get_balance])
