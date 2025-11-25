import configparser

from pathlib import Path

from src.utils.logger import logger


class Config:
    def __init__(self, config_file="config.ini"):
        # base_dir = parent folder dari 'src'
        base_dir = Path(__file__).resolve().parents[2]
        self.config_file = base_dir / config_file

        logger.info(f"Loading configuration from {self.config_file}")

        # opsional: baca file konfigurasi
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)

    def get(self, section, key, fallback=None):
        return self.config.get(section, key, fallback=fallback)


# Inisialisasi objek Config global
config = Config()
