"""
monitor.py

System information, resource monitoring, warnings, live monitor,
and process information for the TB System Resource Monitor.
"""

import os
import platform
import socket
import time

import psutil


# -------------------------------------------------------------------
# Settings (constants)
# -------------------------------------------------------------------

# You will add settings here in Parts 5, 7, and 8.


# -------------------------------------------------------------------
# Part 4: System information
# -------------------------------------------------------------------
def get_system_info():
    """
    Return a dictionary of basic information about this computer.
    """

    info = {
        # TODO: Use platform.system() to get the operating system name.
        "os_name":platform.system(),

        "os_release": platform.release(),

        # TODO: Use socket.gethostname() to get the computer's name.
        "hostname": socket.gethostname(),

        # TODO: Use platform.processor() to get the processor description.
        "processor": platform.processor(),

        "python_version": platform.python_version(),
    }

    # Some computers report an empty processor string.
    # TODO: Check whether the processor value is an empty string ("").
    if info["processor"] == "":
        info["processor"] = "Not available"

    # TODO: Return the dictionary.
    return info

def display_system_info():
    """
    Print the system information in a readable format.
    """

    # TODO: Call get_system_info() and store the dictionary it returns.
    info = get_system_info()

    print()
    print("System Information")
    print("System Information" * 30)

    # TODO: Fill in the dictionary keys from get_system_info().
    print(f"Operating System: {info['os_name']} {info['os_release']}")
    print(f"Computer Name:    {info['hostname']}")
    print(f"Processor:        {info['processor']}")
    print(f"Python Version:   {info['python_version']}")

    