import logging
import os
from datetime import datetime


def get_logger(test_name):
    log_dir = "log"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(
        log_dir,
        f"{test_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    )

    logger = logging.getLogger(test_name)
    logger.setLevel(logging.INFO)
    logger.propagate = True

    # Avoid duplicate handlers
    if not logger.handlers:

        # File Handler (for saving logs in file)
        file_handler = logging.FileHandler(log_file)
        file_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # Stream Handler (VERY IMPORTANT for pytest-html)
        stream_handler = logging.StreamHandler()
        stream_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)

    return logger, log_file
