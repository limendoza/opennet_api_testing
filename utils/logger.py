import logging
import os
from datetime import datetime


class Logger:
    logging_format = logging.Formatter(
        '%(asctime)s|%(name)s|%(levelname)s|%(filename)s|%(lineno)d:%(message)s', '%Y-%m-%d|%H:%M:%S')
    _stream_handler = None
    _file_handler = None
    _logger = None

    @staticmethod
    def initialize_logger(name, log_level=logging.INFO, file_name="automation.log"):
        Logger._logger = logging.getLogger(name)
        Logger._logger.setLevel(log_level)

        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        full_log_path = os.path.join(log_dir, f"{timestamp}_{file_name}")
        Logger._stream_handler = logging.StreamHandler()
        Logger._file_handler = logging.FileHandler(full_log_path)

        Logger._stream_handler.setFormatter(Logger.logging_format)
        Logger._file_handler.setFormatter(Logger.logging_format)

    @staticmethod
    def create_logger(name, log_level=logging.INFO):
        if not Logger._stream_handler and not Logger._file_handler:
            raise AssertionError("Logger not initialized")

        logger = logging.getLogger(name)
        logger.setLevel(log_level)
        logger.addHandler(Logger._stream_handler)
        logger.addHandler(Logger._file_handler)
        return logger
