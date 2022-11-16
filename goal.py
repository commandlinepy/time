from colours import foreground
import time
import json
filename = "./data.json"

def set_time_goal():
  goal_data = {}
  with open("./goal.json", "r") as f:
    temp = json.load(f)

  goal = input(foreground.lightgreen + "\nEnter your time goal in minutes: ")

  if goal.isnumeric() and float(goal) >= 2:
    goal = float(goal) * 60
    goal_data["goal"] = goal

    if len(temp):
      temp.pop(0)
      temp.append(goal_data)
      with open("./goal.json", "w") as f:
        json.dump(temp, f, indent=4)
    else:
      temp.append(goal_data)
      with open("./goal.json", "w") as f:
        json.dump(temp, f, indent=4)

  else:
    print(foreground.lightred + "\nPlease enter a numeric value of 2 or above for your time event.")
    
