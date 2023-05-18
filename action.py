from enum import  IntEnum

class Action(IntEnum):
      ADD_TODO  = 1 
      REMOVE_TODO  = 2 
      UPDATE_TODO = 3
      COMPLETE_TODO = 4
      SHOW_TODO = 5
      SHOW_COMPLETED_TODO = 6
      EXIT_APP = 7