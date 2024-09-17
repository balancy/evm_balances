"""App logger module."""

import logging


def get_logger(name: str) -> logging.Logger:
    """Return a logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s: %(message)s")
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger
