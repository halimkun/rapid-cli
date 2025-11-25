import argparse

from src.utils.args_formatter import CustomHelpFormatter
from src.commands.google_reviews import register as google_reviews_register
from src.commands.instagram import register as instagram_register
from src.commands.api_main import register as main_api_register


"""
===============================================================================
CLI Entry Point
-------------------------------------------------------------------------------
Yes, this is the main file. Everything starts here.
If something breaks, congratulations — now you get to fix it.
===============================================================================
"""


def main():
    """
    Main CLI function.
    Builds the parser, registers commands, and runs whatever the user typed.
    Don't expect magic. This is Python, not a miracle generator.
    """

    # The main parser — where all the chaos begins
    parser = argparse.ArgumentParser(
        description=(
            "A tool to fetch data from various online services.\n"
            "If you expected more features… well, lower your expectations."
        ),
        epilog=(
            "Still confused? Try 'python main.py <command> --help'. "
            "You know, basic reading skills."
        ),
        formatter_class=CustomHelpFormatter,
    )

    # Global version flag — because every tool needs one to look legit
    parser.add_argument(
        "--version",
        action="version",
        version="CLI v0.0.1 — Yes, it's early. Deal with it.",
        help="Show the version. Totally life-changing, I know.",
    )

    # Subparsers — where commands fight to be recognized
    subparsers = parser.add_subparsers(
        dest="command",
        title="Available Commands (don't get too excited)",
        metavar="<command>",
        help="Pick one. If this is hard, maybe CLI tools aren't for you.",
    )

    # Register commands
    main_api_register(subparsers)
    google_reviews_register(subparsers)
    instagram_register(subparsers)

    args = parser.parse_args()

    # User typed nothing? Of course they did.
    if not args.command:
        parser.print_help()
        return

    # Execute the chosen command. Good luck.
    args.func(args)
