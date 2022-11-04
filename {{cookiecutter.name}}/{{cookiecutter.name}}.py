import inspect
import logging
import os
from datetime import datetime

from jsonargparse import CLI

output_dir = os.path.join(os.path.dirname(__file__), "output/")
default_logs_path = os.path.join(
    output_dir, f"logging_{datetime.now().strftime('%Y%m%d_%H-%M-%S')}.log"
)


def main(
    # Input paths
    # Configs
    logging_level: str,
    # Output paths
    logging_path: str = default_logs_path,
):
    """{{cookiecutter.short_description}}"""

    # Configure logging
    logging.basicConfig(
        format="%(asctime)s %(levelname)-8s %(name)-15s %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
        level=logging_level,
        filename=logging_path,
    )
    # Log the current configuration
    logging.info(inspect.getargvalues(inspect.currentframe()).locals)

    ##################
    # Code starts here
    ##################

    print("Script is ready :)")

    ################
    # Code ends here
    ################

    # Exit message
    logging.info("Done with {{cookiecutter.name}}.py")


if __name__ == "__main__":
    CLI(main, as_positional=False)
