import logging


class LoggerFactory:

    def __init__(self, logger_name):
        self.logger_name = logger_name
        self.__logger = logging.getLogger(logger_name)

        log_formatter = '%(asctime)s - %(levelname)s - %(message)s'
        logger = logging.getLogger(__name__)
        logging.basicConfig(format=log_formatter, level=logging.INFO)

        f_handler = logging.FileHandler('logs.log')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)
        f_handler.setLevel(logging.DEBUG)
        logger.addHandler(f_handler)
        self.__logger.addHandler(f_handler)

    def get_logger(self):
        return self.__logger
