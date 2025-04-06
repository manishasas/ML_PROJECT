import os
from datetime import datetime
import logging  # ← this was also missing!

# Step 1: Create a timestamped log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 2: Create logs directory path
logs_path = os.path.join(os.getcwd(), "logs")

# Step 3: Make sure the logs directory exists
os.makedirs(logs_path, exist_ok=True)

# Step 4: Full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Step 5: Set up basic logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Step 6: Test it
if __name__ == "__main__":
    logging.info("Logging has started")

