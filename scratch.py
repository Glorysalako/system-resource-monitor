import monitor

all_processes = monitor.get_top_processes(1000)
print("Processes read successfully:", len(all_processes))

monitor.display_top_processes()