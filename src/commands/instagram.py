from src.services.rapid_api.instagram import fetch_instagram_posts
from src.utils.logger import logger


def register(subparsers):
    parser = subparsers.add_parser(
        "instagram",
        help="Fetch Instagram posts, because stalking manually is apparently rocket science for you.",
    )

    parser.add_argument(
        "username",
        help="Instagram username. The REAL one. Not whatever random garbage you usually type.",
    )

    parser.set_defaults(func=run)


def run(args):
    logger.info(f"Trying to fetch Instagram posts for '{args.username}'...")
    logger.critical("If this crashes, it's 99% your fault, not mine.")

    fetch_instagram_posts(args.username)

    logger.info("Done. Shockingly, everything worked.")
