from dataclasses import dataclass
from datetime import datetime 
from json import JSONEncoder 


@dataclass
class Todo: 
   title : str 
   description : str 
   is_completed: bool  = False
   create_at : str  =  str(datetime.now().strftime('le %d/%m/%Y à %H:%M:%S'))
   update_at : str  =""
   
   
   def __str__(self):
      return f"""
          title: {self.title}
          description: {self.description}
          is_completed: {self.is_completed}
          ajouter a : {self.create_at}
          {f"modifier a : {self.update_at}" if self.update_at !="" else ""}
    """
    
   def modify(self, title:str , description:str):
        self.title = title
        self.description = description
        self.update_at = str(datetime.now().strftime('le %d/%m/%Y à %H:%M:%S')) 
  
   def completed(self): 
       self.is_completed = True
       return self
    
   def __eq__(self, todo):
       return (self.title == todo.title and self.description == todo.description) 
    
   

class TodoEncoder(JSONEncoder): 
     def default(self, o: Todo):
         return o.__dict__  
     

@dataclass
class TodoPomodoro: 
     def __init__(self, title, time, pause):
         self.title = title
         self.timer = self._set_time(time)
         self.pause = pause 
     
     def _set_time(self,time)-> int:
         if 'min' in time: 
             slicee = time.split('min')
             return int(slicee[0]) * 60
         
     def __str__(self):
      return f"""
          title: {self.title}
           time: {self.timer}
    """
             
        
         
    