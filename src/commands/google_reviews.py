from src.services.rapid_api.google_service import fetch_google_reviews
from src.utils.logger import logger


def register(subparsers):
    parser = subparsers.add_parser(
        "google_reviews",
        help="Fetch Google Reviews, since apparently opening Google is too advanced for you.",
    )

    parser.add_argument(
        "place",
        help="The place name. Spell it right this time. I'm not here to fix your typos.",
    )

    parser.set_defaults(func=run)


def run(args):
    logger.info(f"Trying to fetch Google reviews for '{args.place}'...")
    logger.debug(
        "Hold on, let me gather reviews written by people who think CAPS LOCK is a personality trait."
    )

    fetch_google_reviews(args.place)

    logger.info("Done. Shockingly, everything worked.")
