import os
import logging
from datetime import datetime
from colorama import Fore, Style

# Define the target directory for logs
target_directory = './data'
logs_directory = os.path.join(target_directory, 'logs')

# Ensure the logs directory exists
os.makedirs(logs_directory, exist_ok=True)
print(f"'logs' directory is ready at {logs_directory}")

# Define a color scheme for console output
COLORS = {
    'WARNING': Fore.YELLOW,
    'INFO': Fore.BLUE,
    'DEBUG': Fore.GREEN,
    'CRITICAL': Fore.RED + Style.BRIGHT,
    'ERROR': Fore.RED
}

class ColoredConsoleHandler(logging.StreamHandler):
    def emit(self, record):
        # Use the color scheme defined above
        color = COLORS.get(record.levelname)
        levelname_color = color + record.levelname + Style.RESET_ALL
        message = self.format(record)
        # Replace the levelname with a colored one
        message = message.replace(record.levelname, levelname_color)
        print(message)

# Custom Formatter
class CustomFormatter(logging.Formatter):
    """Custom formatter, overrides funcName with value of funcname if it exists"""
    def format(self, record):
        if hasattr(record, 'funcname'):
            record.funcName = record.funcname
        return super(CustomFormatter, self).format(record)

def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Log format
    log_format = CustomFormatter('%(asctime)s - %(levelname)s - %(message)s')

    # Console handler with color
    console_handler = ColoredConsoleHandler()
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # File handler
    log_filename = f'application_{datetime.now().strftime("%Y%m%d%H%M%S")}.log'
    file_handler = logging.FileHandler(os.path.join(logs_directory, log_filename))
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    return logger

# Initialize the logger
logger = setup_logging()

