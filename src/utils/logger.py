import logging

# Dracula ANSI colors
COLORS = {
    "DEBUG": "\033[38;5;117m",  # Cyan (8BE9FD)
    "INFO": "\033[38;5;84m",  # Green (50FA7B)
    "WARNING": "\033[38;5;228m",  # Yellow (F1FA8C)
    "ERROR": "\033[38;5;203m",  # Red (FF5555)
    "CRITICAL": "\033[38;5;170m",  # Pink/Magenta (FF79C6)
}

RESET = "\033[0m"

MAX_LEVEL_LEN = 8


class LoggerFormatter(logging.Formatter):
    def format(self, record):
        level_name = record.levelname
        color = COLORS.get(level_name, RESET)

        # align kiri
        padded = level_name.ljust(MAX_LEVEL_LEN)
        record.levelname = f"{color}{padded}{RESET}"

        return super().format(record)


logger = logging.getLogger("toxic_logger")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()

# tambahkan timestamp
formatter = LoggerFormatter(
    "[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

handler.setFormatter(formatter)
logger.addHandler(handler)
