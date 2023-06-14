import os
import logging
from flask import Flask


def configure_logger(app: Flask):
    """
    Configure and return a logger instance with different handlers for console, Werkzeug logs,
    general logs, and error logs.

    This function sets up a logger with multiple handlers to direct log messages based on their
    level and source. Non-Werkzeug log messages are sent to the console, Werkzeug logs are written
    to the 'werkzeug.log' file, INFO and higher level messages (excluding Werkzeug) are stored in
    the 'general.log' file, and ERROR and higher level messages are captured in the 'errors.log' file.

    Args:
        app (Flask): The Flask application object.

    Returns:
        logging.Logger: The configured logger instance.

    Note:
        Make sure to call this function after creating the Flask application object.
    """
    # Create a logger instance
    logger = app.logger

    # Set the log level for the logger
    logger.setLevel(logging.DEBUG)

    # Create a console handler for non-Werkzeug logs
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Create the 'logs/' folder if it doesn't exist
    if not os.path.exists("logs/"):
        try:
            os.makedirs("logs/")
        except PermissionError:
            logger.error("Failed to create 'logs/' folder. Check permissions.")

    # Create a file handler for Werkzeug logs
    try:
        werkzeug_handler = logging.FileHandler("logs/werkzeug.log")
        werkzeug_handler.setLevel(logging.INFO)  # Set the desired level for Werkzeug logs
        werkzeug_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        werkzeug_handler.setFormatter(werkzeug_formatter)
        werkzeug_logger = logging.getLogger("werkzeug")
        werkzeug_logger.setLevel(logging.INFO)  # Set the desired level for Werkzeug logs
        werkzeug_logger.addHandler(werkzeug_handler)
    except PermissionError:
        logger.error("Failed to create 'werkzeug.log' file. Check permissions.")

    # Create a file handler for general logs (INFO and higher, excluding Werkzeug)
    try:
        general_handler = logging.FileHandler("logs/general.log")
        general_handler.setLevel(logging.INFO)
        general_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        general_handler.setFormatter(general_formatter)
        logger.addHandler(general_handler)
    except PermissionError:
        logger.error("Failed to create 'general.log' file. Check permissions.")

    # Create a file handler for error logs (ERROR and higher)
    try:
        error_handler = logging.FileHandler("logs/errors.log")
        error_handler.setLevel(logging.ERROR)
        error_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        error_handler.setFormatter(error_formatter)
        logger.addHandler(error_handler)
    except PermissionError:
        logger.error("Failed to create 'errors.log' file. Check permissions.")

    return logger
