import logging

# Set up a logger specific to this module
logger = logging.getLogger("Tableau d'étudiants")
logger.setLevel(logging.INFO)
logger.propagate(False)

# Prevent duplicate handlers
if not logger.hasHandlers():
    # Set logging handler for this module
    file_handler = logging.FileHandler("logs/information.txt", mode="w")
    file_handler.setFormatter(logging.Formatter("%(level)s: %(message)s"))
    logger.addHandler(file_handler)