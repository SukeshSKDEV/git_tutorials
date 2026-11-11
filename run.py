
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logging.info("git tutorial started")

try:
    dataset_name = "git_tutorials.csv"
    logging.info("Loading dataset: %s", dataset_name)

    # Simulate a missing dataset
    raise FileNotFoundError("Dataset file not found")

except FileNotFoundError as error:
    logging.error("Could not load dataset: %s", error)

logging.info("Program finished")
