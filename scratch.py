import monitor
import logger

summary = monitor.get_resource_summary()

path = logger.save_snapshot(summary)
print("Saved to:",path)

path = logger.save_snapshot(summary)
print("Saved again to:",path)