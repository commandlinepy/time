from colours import foreground
from schema import print_schema
import time
import json
filename = "./data.json"


def delete_time():
  print(foreground.darkgrey + "Time Goals are automatically deleted/replaced each time you add them.\n")
  
  with open(filename, "r") as f:
    temp = json.load(f)
  
    if len(temp):
      i = 0
      for entry in temp:
        print_schema(entry, i)
        i +=1
    else:
      print(foreground.lightred + "No time values have been added. Try adding time events.")
      return

    new_data = []
    data_length = len(temp) -1

    delete_option = input(foreground.lightred + "To delete a Time Event enter the" + foreground.lightcyan + f" ID number from 0-{data_length} " + foreground.lightred + "and press enter.\n\n")
      
    if delete_option.isnumeric():
      if int(delete_option) > data_length:
        print(foreground.lightred + "ID does not exist. Try again.")
        return    
      else:
        i = 0
        confirm = input(foreground.lightred + "Are you sure? (Y/N)")
        if confirm == "Y":
          for entry in temp:
            if i == int(delete_option):
              pass
              i +=1
            else:
              new_data.append(entry)
              i +=1
          with open(filename, "w") as f:
            json.dump(new_data, f, indent=4)
        else:
          print(foreground.yellow + "No problem. Try another option:")
    
    else: 
      print(foreground.lightred + "Deletion requires a numeric value.")
