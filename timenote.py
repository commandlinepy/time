from colours import foreground

from goal import set_time_goal
from show import show_times
from add import add_time
from calc import calc_event_goal
from delete import delete_time


def show_menu():
  print(foreground.yellow + "\nSELECT A NUMBER OPTION BELOW AND PRESS ENTER:")
  
  print(foreground.lightblue + "(1)SET TIME GOAL " +
  foreground.lightgreen + "(2)ADD TIME EVENT " +
  foreground.lightred + "(3)DELETE TIME EVENT")

  print(foreground.pink + "(4)SHOW TIMES " +
  foreground.lightcyan + "(5)CALCULATE TIME REMAINING " +
  foreground.white + "(0)EXIT")


def main():
  while True:
    show_menu()
    choice = input("\n")
    if choice == "1":
      set_time_goal()
    elif choice == "2":
      add_time()
    elif choice == "3":
      delete_time()
    elif choice == "4":
      show_times()
    elif choice == "5":
      calc_event_goal()
    elif choice == "0":
      break
    else:
      print(foreground.lightred + "Incorrect option, please try again.")


if __name__ == "__main__":
    main()
