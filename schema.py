from colours import foreground
import time

def print_schema(entry, i):
  time_elapsed = entry["time_elapsed"]
  
  time_format = time.strftime("%H:%M", time.gmtime(time_elapsed * 60))
  print(foreground.lightcyan + f"ID: {i}\t Time Event: ",time_format)