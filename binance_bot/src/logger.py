import logging

def setup_logger(name="binance_bot", log_file="bot.log"):
    """Configure logger for the bot."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # File handler (logs to bot.log)
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    # Console handler (still prints to screen)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Format: [TIME] LEVEL: message
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Avoid duplicate handlers if called multiple times
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Create a default logger instance
logger = setup_logger()
