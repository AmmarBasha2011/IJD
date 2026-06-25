import logging
import os


_logger = None


def get_logger(name="INEXJD", level=logging.INFO, log_file=None):
    """
    Get or configure the INEXJD logger.
    
    Args:
        name (str): Logger name
        level (int): Logging level
        log_file (str, optional): Path to log file
        
    Returns:
        logging.Logger: Configured logger instance
    """
    global _logger
    if _logger is not None:
        return _logger
    
    _logger = logging.getLogger(name)
    _logger.setLevel(level)
    _logger.handlers.clear()
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    _logger.addHandler(ch)
    
    # File handler
    if log_file:
        log_dir = os.path.dirname(log_file)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)
        fh = logging.FileHandler(log_file)
        fh.setLevel(level)
        fh.setFormatter(formatter)
        _logger.addHandler(fh)
    
    return _logger


def set_log_level(level):
    """Set global log level."""
    logger = get_logger()
    logger.setLevel(level)
    for handler in logger.handlers:
        handler.setLevel(level)
