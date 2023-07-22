import os
import logging
import datetime
from configuration import load_config


def setup_logger(log_dir):
    # Create the log directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Get the current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Define the log file path and format
    log_filename = f"log_{current_date}.txt"
    log_path = os.path.join(log_dir, log_filename)
    formatter = logging.Formatter("%(asctime)s:%(msecs)03d - %(levelname)s : %(message)s", "%Y-%m-%d %H:%M:%S")

    # Create a file handler and set the formatter
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # Optionally, you can also add a stream handler to print logs to the console
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger

config = load_config()
log_dir = config["logs"]
logger = setup_logger(log_dir)

if __name__ == "__main__":
    logger.info("Logger set up successful")