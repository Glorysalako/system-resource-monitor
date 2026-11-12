"""
logger.py

Saves resource snapshots to a CSV file for the TB System Resource Monitor.
"""

import csv
import os
from datetime import datetime


# The folder that contains this file (your project folder)
PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))

# logs/ folder inside the project folder
LOG_FOLDER = os.path.join(PROJECT_FOLDER, "logs")

# logs/snapshots.csv
LOG_FILE = os.path.join(LOG_FOLDER, "snapshots.csv")

# The column names (header row) of the CSV file
FIELDNAMES = ["timestamp", "cpu_percent", "memory_percent", "disk_percent"]

def get_timestamp():
    """
    Return the current date and time as text, like "2026-10-27 18:30:00".
    """

    # TODO: Get the current date and time using datetime.now().
    now = datetime.now()

    return now.strftime("%Y-%m-%d %H:%M:%S")

def needs_header():
    """
    Return True if the CSV file still needs a header row.
    """

    # The file does not exist yet
    # TODO: Use os.path.exists() to check whether LOG_FILE exists.
    if not os.path.exists(LOG_FILE):
        # TODO: The file is missing, so it needs a header.
        return True

    # The file exists but is empty
    # TODO: Check whether the file size is 0 bytes.
    if os.path.getsize(LOG_FILE) == 0:
        return True

    return False

def save_snapshot(summary):
    """
    Add one row to logs/snapshots.csv using a resource summary dictionary.
    Return the path of the file that was written.
    """

    # Make sure the logs folder exists
    # TODO: Use os.makedirs() to create LOG_FOLDER if it is missing.
    os.makedirs(LOG_FOLDER, exist_ok=True)

    # Check this BEFORE opening the file (opening creates it)
    # TODO: Call your needs_header() function.
    write_header = needs_header()

    row = {
        "timestamp": get_timestamp(),

        # TODO: Copy the values from the summary dictionary.
        "cpu_percent": summary["cpu_percent"],
        "memory_percent": summary["memory_percent"],
        "disk_percent": summary["disk_percent"],
    }

    # TODO: Open LOG_FILE in append mode.
    with open(LOG_FILE, "a", newline="") as csv_file:
        # TODO: Pass the list of column names as fieldnames.
        writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)

        # TODO: Only write the header if the file needed one.
        if write_header:
            writer.writeheader()

        # TODO: Write the row dictionary to the file.
        writer.writerow(row)

    # TODO: Return the path of the log file.
    return LOG_FILE

