import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        log_directory = "./Logs"

        # Create the Logs directory if it doesn't exist

        if not os.path.exists(log_directory):
                os.makedirs(log_directory)
                print("Logs directory created.")

        log_file_path = os.path.join(log_directory, "automation.log")

        # Set up logging configuration
        logging.basicConfig(
            filename=log_file_path,
            format="%(asctime)s: %(levelname)s: %(message)s",
            datefmt="%Y %m %d %I:%M:%S",
            level=logging.INFO  # Ensure logging level is set
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
