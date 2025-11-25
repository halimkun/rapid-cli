import uvicorn

from src.utils.logger import logger
from src.services.api.app import create_app
from src.core.config import config


def register(subparsers):
    parser = subparsers.add_parser(
        "api_main", help="Main API command, to run the primary API functions."
    )

    parser.add_argument(
        "--host", default="0.0.0.0", help="Host to run the API on (default: 0.0.0.0)"
    )

    parser.add_argument(
        "--port",
        type=int,
        default=int(config.get("api:server", "port", fallback="8000")),
        help="Port to run the API on (default: 8000)",
    )

    parser.set_defaults(func=run)


def run(args):
    logger.info("Starting FastAPI server...")
    app = create_app()

    logger.info(f"Running at http://{args.host}:{args.port}")
    uvicorn.run(
        app,
        host=args.host,
        port=args.port,
        log_level="info",
        reload=config.get("api:server", "reload", fallback="false").lower() == "true",
    )
