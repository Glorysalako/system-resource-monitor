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

# # 1 GB = 1024 * 1024 * 1024 bytes
# TODO: Fill in the exponent so this equals the number of bytes in 1 GB.
BYTES_PER_GB = 1024 ** 3 # 1 GB = 1024^3 bytes


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


# -------------------------------------------------------------------
# Part 5: CPU, memory, and disk
# -------------------------------------------------------------------

def bytes_to_gb(num_bytes):
    """
    Convert a number of bytes to gigabytes, rounded to 2 decimal places.
    """

    # TODO: Divide the number of bytes by the number of bytes in 1 GB.
    gigabytes = 1073741824 / 1024 ** 3

    # TODO: Round gigabytes to 2 decimal places.
    return round(gigabytes, 2)

def get_cpu_usage():
    """Return the current CPU usage percentage.
    """

    # TODO:
    # Use psutil.cpu_percent().
    # Use an interval of 1 second.
    cpu_usage = psutil.cpu_percent(interval=1)

    # TODO: Return the CPU usage.
    return cpu_usage

def get_memory_usage():
    """
    Return a dictionary with memory (RAM) percent, used GB, and total GB.
    """

    # TODO: Call psutil.virtual_memory() and store the result.
    memory = psutil.virtual_memory()

    memory_info = {
        # TODO: Use the .percent attribute of memory.
        "percent": memory.percent,

        # TODO: Convert memory.used from bytes to GB using your function.
        "used_gb": bytes_to_gb(memory.used),

        # TODO: Convert the total memory from bytes to GB.
        "total_gb": bytes_to_gb(memory.total),
    }

    return memory_info

def get_disk_path():
    """
    Return the path of the main disk for this operating system.
    """

    # TODO: Get the name of the operating system (same function as Part 4).
    system_name = platform.system()

    # TODO: Fill in the name platform.system() returns on Windows.
    if system_name == "Windows":
        return "C:\\"
    elif system_name == "Darwin" and os.path.exists("/System/Volumes/Data"):
        # On modern macOS, your files live on the "Data" volume.
        return "/System/Volumes/Data"
    else:
        # TODO: Return the root path used by Linux (and older macOS).
        return "/"

def get_disk_usage():
    """
    Return a dictionary with disk percent, used GB, and total GB.
    """

    # TODO: Call psutil.disk_usage() and pass it the path from get_disk_path().
    disk = psutil.disk_usage(get_disk_path())

    # TODO: Build the dictionary the same way you did in get_memory_usage().
    disk_info = {
        "percent": disk.percent,
        "used_gb": bytes_to_gb(disk.used),
        "total_gb": bytes_to_gb(disk.total),
    }

    return disk_info

    