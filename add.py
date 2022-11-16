from colours import foreground
import time
import json
filename = "./data.json"




def add_time():
  item_data = {}
  time = input(foreground.lightgreen + f"Enter time in minutes: ")

  if time.isnumeric() and float(time) >= 1:      
    item_data["time_elapsed"] = int(time)
    with open(filename, "r") as f:
      temp = json.load(f)
    temp.append(item_data)
    with open(filename, "w") as f:
      json.dump(temp, f, indent=4)

  else:
    print(foreground.lightred + "\nPlease enter a numeric value of 1 or above for your time event.")
