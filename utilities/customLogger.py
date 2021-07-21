import logging


# method loggen is a method inside LogGen class
# where to generate the log file

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log")
        # create object for logging. logger is the object
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
