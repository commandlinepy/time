from colours import foreground
from schema import print_schema
import time
import json
filename = "./data.json"


def show_times(): 
  with open("./goal.json", "r") as f:
    temp_goal = json.load(f)
  
  if len(temp_goal):
    goal_dict = temp_goal[0].values()

    for goal in goal_dict:
      goal = int(goal) / 60
    time_format = time.strftime("%H:%M", time.gmtime(goal * 60))
    print(foreground.lightgreen + "Time Goal: " + time_format)
  else:
    print(foreground.lightred + "No time goal has been added. Try adding one.")

  with open(filename, "r") as f:
    temp = json.load(f)
  if len(temp):
    i = 0
    for entry in temp:
      print_schema(entry, i)
      i +=1
  else:
    print(foreground.lightred + "No time event values have been added. Try adding time events.")

