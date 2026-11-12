"""
monitor.py

System information, resource monitoring, warnings, live monitor,
and process information for the TB System Resource Monitor.
"""

import os
import platform
import socket
import time
from webbrowser import get

import psutil


# -------------------------------------------------------------------
# Settings (constants)
# -------------------------------------------------------------------

# # 1 GB = 1024 * 1024 * 1024 bytes
# TODO: Fill in the exponent so this equals the number of bytes in 1 GB.
BYTES_PER_GB = 1024 ** 3 # 1 GB = 1024^3 bytes
# Warning thresholds (in percent)
# TODO: Fill in the default thresholds: CPU 80, memory 80, disk 90.
THRESHOLDS = {
    "cpu": 80,
    "memory": 80,
    "disk": 80,
}
# How many seconds the live monitor waits between refreshes
# TODO: Set this to 2 seconds.
REFRESH_SECONDS = 2
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

# -------------------------------------------------------------------
# Part 6: Resource summary
# -------------------------------------------------------------------

def get_resource_summary():
    """
    Gather CPU, memory, and disk information into ONE dictionary.
    """

    # TODO: Call your memory function and store its dictionary.
    memory = get_memory_usage()

    # TODO: Call your disk function and store its dictionary.
    disk = get_disk_usage()

    # TODO: Call your CPU function and store its value.
    cpu_percent = get_cpu_usage()

    summary = {
        # TODO: Call your CPU function.
        "cpu_percent": cpu_percent,
        "memory_percent" : memory["percent"],

        # TODO: Get the used GB value out of the memory dictionary.
        "memory_used_gb": memory["used_gb"],

        # TODO: Get the total GB value out of the memory dictionary.
        "memory_total_gb": memory["total_gb"],

        # TODO: Get the percent value out of the disk dictionary.
        "disk_percent": disk["percent"],

        "disk_used_gb": disk["used_gb"],

        # TODO: Get the total GB value out of the disk dictionary.
        "disk_total_gb": disk["total_gb"],
    }

    return summary

def display_resource_summary(summary):
    """
    Print a resource summary dictionary in a readable format.
    """

    print()
    print("Current System Status")
    print("-" * 30)
    print(f"CPU Usage:    {summary['cpu_percent']}%")

    # TODO: Fill in the correct summary keys.
    print(f"Memory Usage: {summary['memory_percent']}%")
    print(f"Used Memory:  {summary['memory_used_gb']:.2f} GB")
    print(f"Total Memory: {summary['memory_total_gb']:.2f} GB")
    print(f"Disk Usage:   {summary['disk_percent']}%")
    print(f"Used Disk:    {summary['disk_used_gb']:.2f} GB")
    print(f"Total Disk:   {summary['disk_total_gb']:.2f} GB")
# -------------------------------------------------------------------
# Part 7: Warnings
# -------------------------------------------------------------------

def check_status(value, threshold):
    """
    Return "HIGH" if value is above threshold, otherwise "OK".
    """

    # TODO: Check whether value is greater than threshold.
    if value > threshold:
        # TODO: Return the text "HIGH".
        return "HIGH"

    return "OK"
def get_statuses(summary):
    """
    Return a dictionary with the status ("OK" or "HIGH") of each resource.
    """

    statuses = {
        "cpu": check_status(summary["cpu_percent"], THRESHOLDS["cpu"]),

        # TODO: Check memory_percent against the memory threshold.
        "memory": check_status(summary["memory_percent"], THRESHOLDS["memory"]),

        # TODO: Check disk_percent against the disk threshold.
        "disk": check_status(summary["disk_percent"], THRESHOLDS["disk"]),
    }

    return statuses

def get_warnings(summary):
    """
    Return a list of warning messages for any resource that is HIGH.
    """

    warnings = []
    statuses = get_statuses(summary)

    if statuses["cpu"] == "HIGH":
        warnings.append("WARNING: CPU usage is high!")

    # TODO: Check the memory status and add the memory warning.
    if statuses["memory"] == "HIGH":
        warnings.append("WARNING: Memory usage is high!")

    # TODO: Check the disk status and add the disk warning.
    #       Write the full if statement, following the two above.
    if statuses["disk"] == "HIGH":
        warnings.append("WARNING: Disk usage is high!")

    return warnings
def display_warnings(summary):
    """
    Print each warning, or a friendly message if there are none.
    """
    warnings = get_warnings(summary)

    # TODO: Check whether the warnings list is empty (has length 0).
    if len(warnings) == 0:
        print("All resources are within normal limits.")
    else:
        # TODO: Loop through each warning in the list and print it.
        for warning in warnings:
            print(warning)

# -------------------------------------------------------------------
# Part 8: Live monitor
# -------------------------------------------------------------------

def clear_screen():
    """
    Clear the terminal window.
    """

    # os.name is "nt" on Windows
    # TODO: Fill in the value of os.name on Windows,
    #       and the Windows clear-screen command.
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def display_live_screen(summary):
    """
    Print one "frame" of the live monitor.
    """

    # TODO: Get the statuses dictionary for this summary.
    statuses = get_statuses(summary)

    print("=" * 30)
    print("   TB System Resource Monitor")
    print("=" * 30)
    print()
    print(f"CPU Usage:      {summary['cpu_percent']}%")
    print(f"Memory Usage:   {summary['memory_percent']}%")

    # TODO: Print the disk percent from the summary.
    print(f"Disk Usage:     {summary['disk_percent']}%")
    print()
    print("Status:")
    print(f"CPU:    {statuses['cpu']}")

    # TODO: Print the memory and disk statuses.
    print(f"Memory: {statuses['memory']}")
    print(f"Disk:   {statuses['disk']}")
    print()
    print("Press Ctrl+C to stop monitoring.")
def start_live_monitor():
    """
    Keep refreshing the screen until the user presses Ctrl+C.
    """

    try:
        # TODO: Start a loop that runs forever.
        while True:
            # TODO: Gather a fresh resource summary.
            summary = get_resource_summary()

            clear_screen()

            # TODO: Display this summary on the screen.
            display_live_screen(summary)

            # TODO: Wait REFRESH_SECONDS seconds before the next refresh.
            time.sleep(REFRESH_SECONDS)

    # TODO: Catch the exception raised when the user presses Ctrl+C.
    except KeyboardInterrupt:
        print()
        print("Live monitor stopped. Returning to the menu...")


# -------------------------------------------------------------------
# Part 9: Top processes
# -------------------------------------------------------------------

def get_memory_value(process_info):
    """
    Return the memory percent from one process dictionary.
    Used as the "key" when sorting.
    """

    # TODO: Return the value stored under the "memory_percent" key.
    return process_info["memory_percent"]

def get_top_processes(limit=5):
    """
    Return a list of the processes using the most memory.
    Each item in the list is a dictionary.
    """

    # TODO: Start with an empty list.
    processes = []

    # TODO: Loop over every running process using psutil.
    for process in psutil.process_iter():
        try:
            process_info = {
                # TODO: Fill in the attribute/methods from the table in Step 9.1.
                "pid": process.pid,
                "name": process.name(),
                "memory_percent": process.memory_percent(),
            }

            # TODO: Add process_info to the end of the processes list.
            processes.append(process_info)

        # TODO: Catch the three psutil exceptions from Step 9.1.
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # The process ended, or we are not allowed to read it.
            # TODO: Skip this process and move on to the next one.
            continue

    # TODO: Sort by memory percent, largest first.
    processes.sort(key=get_memory_value, reverse=True)

    # TODO: Return only the first `limit` items.
    return processes[:limit]

def display_top_processes(limit=5):
    """
    Print the top processes in a table.
    """

    # TODO: Get the top processes, passing along limit.
    top_processes = get_top_processes(limit)

    print()
    print("Top Processes by Memory")
    print()
    print(f"{'PID':<8} {'Name':<25} {'Memory':>8}")
    print("-" * 43)

    for process_info in top_processes:
        # TODO: Read the pid and memory_percent from the dictionary.
        pid = process_info["pid"]
        name = process_info["name"][:25]
        memory = process_info["memory_percent"]

        print(f"{pid:<8} {name:<25} {memory:>7.1f}%")

