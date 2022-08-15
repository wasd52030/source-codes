import logging

import httpx
from rich.logging import RichHandler

logging.basicConfig(
    level=logging.INFO,
    style="{",
    format="{message}", datefmt="[%X]",
    handlers=[RichHandler(show_time=False, show_path=False, markup=True, keywords=RichHandler.KEYWORDS + ['STREAM'],
                          rich_tracebacks=True)]
)
log = logging.getLogger("rich")

if __name__ == '__main__':
    # log.info("", exc_info=Exception(1))
    print(repr(IndexError))
    try:
        1/0
    except Exception as e:
        log.warning(f"STREAM {e}")

    log.warning("GET", exc_info=IndexError(123))
    # log.warning("Hello, World! https://www.baidu.com")
    # log.warning("Hello, World! https://www.baidu.com")
    # log.error("Hello, World! https://www.baidu.com")
