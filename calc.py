from colours import foreground
import time
import json

seconds = 0
def calc_event_goal():
  global seconds
  
  with open("./data.json", "r") as f:
    temp = json.load(f)

  if len(temp):
    total = sum(map(lambda x: int(x['time_elapsed']), temp))
    seconds = total * 60
    time_format = time.strftime("%H:%M", time.gmtime(seconds))
    print(foreground.yellow + f"Total Time:\t\t", time_format)
  else:
    seconds = 0
    print(foreground.lightred + "No time values have been added. Try adding time events.")

  with open("./goal.json", "r") as f:
    temp_goal = json.load(f)
  
    if len(temp_goal):
      goal_dict = temp_goal[0].values()
      
      for goal in goal_dict:
        goal = int(goal)

      if goal < seconds: 
        time_format = time.strftime("%H:%M", time.gmtime(goal * 60))
        print(foreground.lightred + "Time Goal: " + time_format)

        print(foreground.yellow + "Goal exceeded!!!")
        print(foreground.darkgrey + "The time goal you set is now less than your time events total.")
      else:
        goalTotal = goal - seconds
        if goalTotal == 0:
          print("\t\tGoal reached!!!")
        else:
          ttg = time.strftime("%H:%M", time.gmtime(goalTotal))
          print(foreground.lightblue + "Goal reached in:\t", ttg)

    else:
      print(foreground.lightred + "No time goal has been added. Try adding one")
