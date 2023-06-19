# The lengedary African Drum Circles;  You are part of a community that hosts one of the largest
# drum circles in Africa.There are different types of traditional drums used in the circle,each 
# with  its unique sound and rhythm.The Djembe,Talking drum,and Bougarabou are among the popular
# ones.These drums have common properties such as the mat                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           erial they are made from and their sizes 
# ,but they also have distinct characteristics.For instance the talking drum can mimic the lines
# of human speech,the Djembe is known for its wide range of tones,and the Bougarabou is noted for 
# its deep,rich bass tones.
# You want to create a software model of the drum circle ,that encaspulates these different types
# of drums .You wish to include methods for each drum that represents the sound it makes,and also
# group similar drums together.Think about creating a base drum class that contains properties and 
# methods common to all drums ,and then create subclasses for each specific type of drum(like Djembe
#                                                                                        ,talking drum,and bougarabou).
# The subclasses should inherit from the base  drum class and also implement their unique 
# characteristics.This software model would help newcomers understand the characteristics of each drum
# and how they contribute to the overall rhythm of the drum circles.

# METHOD 1

# class Drum:
#     def __init__(self, material, size):
#         self.material = material
#         self.size = size

#     def play_sound(self):
#         raise NotImplementedError("Subclasses must implement play_sound() method.")


# class Djembe(Drum):
#     def __init__(self, material, size):
#         super().__init__(material, size)

#     def play_sound(self):
#         print("Djembe: Wide range of tones.")


# class TalkingDrum(Drum):
#     def __init__(self, material, size):
#         super().__init__(material, size)

#     def play_sound(self):
#         print("Talking Drum: Mimics lines of human speech.")


# class Bougarabou(Drum):
#     def __init__(self, material, size):
#         super().__init__(material, size)

#     def play_sound(self):
#         print("Bougarabou: Deep, rich bass tones.")

# djembe = Djembe("Wood", "Large")
# djembe.play_sound()  # Output: Djembe: Wide range of tones.

# talking_drum = TalkingDrum("Leather", "Medium")
# talking_drum.play_sound()  # Output: Talking Drum: Mimics lines of human speech.

# bougarabou = Bougarabou("Wood", "Small")
# bougarabou.play_sound()  # Output: Bougarabou: Deep, rich bass tones.

# METHOD 2

class Drum:
    def __init__(self,material,size) :
        self.material=material
        self.size = size
        
    def predict_sound(self):
        print(f"{self.__class__.__name__}:{self.sound}")   
        
class Djembe(Drum):
    sound=("Produce a wide range of sound")
  
class Talking_Drum(Drum):
    sound=("It minics the line of human speech")  
    
class Boujouraborau(Drum):
    sound=("Produce deep,rich base tones") 
    
Drum1 = Talking_Drum(material="wood",size="large") 
Drum1.predict_sound()  

Drum2 = Djembe(material="wood",size="large") 
Drum2.predict_sound()
   
Drum3 = Boujouraborau(material="wood",size="large") 
Drum3.predict_sound()
   
      
             
        



# The Ever changing Ankara :You are a fashion  designer known for your unique and vibrant ankara designs.
# Recently you have discovered that some of your fabric patterns change their designs based on the temperature and mood
# of the wearer.You want to create a software  application that can predict the changes in the fabric design given the mood 
# and temperature data.Think about the classes you will need to model the changing Ankara and how to predict  the chANGES.

class Ankara:
    def __init__(self,temperature,mood):
        self.temperature=temperature
        self.mood= mood
        
    def predict_fabric_pattern(self):
        if self.temperature >=20 and self.mood=="Exited":
            return"Wear light and more patterned Ankara"
        elif self.temperature <=20 and self.mood=="Sad":
            return"Wear dull  and less patterned Ankara"
        else:
            return"No change in pattern"
        
ankara=Ankara(20,"Exited")
prediction=ankara.predict_fabric_pattern() 
print(prediction)       
ankara=Ankara(20,"sad")
prediction=ankara.predict_fabric_pattern() 
print(prediction)



# The great migration forecast:Ever year,millions of wildebeest,zebras,and other animals participate in the great migration
# accross the serengeti-Mara ecosystem.As a conservationist,you want to develop a software system that models this migration,
# predicting the movement of the herds based on weather patterns,river levels and predator location.consider what classes 
# you'll need to reprensent the animals,the environment and the various factors that influence the migration.



class Migration:
    def __init__(self, weather, river_level, predictor_location):
        self.weather = weather
        self.river_level = river_level
        self.predictor_location = predictor_location
        
    def predictor_migration(self):
        river_level_in_fts = 200
        current_weather = "rainy"
        
        if self.river_level > river_level_in_fts and self.weather == current_weather:
            return "Migration will not occur" 
         
        else:
            return "Migration will occur"
        
    def new_location(self, current_location):
        self.current_location = current_location
        return f"Migration from {self.predictor_location} to {self.current_location}"
           
migration = Migration("rainy", 300, "Maasai Mara")
print(migration.predictor_migration())
print(migration.new_location("Serengeti"))



# NollyWood Movie planner: As a producer in the booming  NoolyWood movie industry ,you are in charge of multiple firm projects 
# at once.Each movie has different cast members,shooting schedules and budjects.You want to write a program  to help manage film
# projects efficiently.The software should be able to handle the complexities of scheduling ,budgetting and cordinating between
# different movie projects.

class film:
    def __init__(self,title,cast,shooting_schedule,budget) :
        self.title= title
        self.cast=cast
        self.shooting_schedule=shooting_schedule
        self.budget=budget
        
class producer:
    def __init__(self):
        self.projects=[]
    def add_projects(self,film):   
        self.projects.append(film)  
    def remove_projects(self,film) :
        self.projects.remove(film) 
    def get_project_by_title(self,title):
        for project in self.projects:
            if project.title == title:
               return project
        return None 
    
    def get_project_cast(self,title):
        project = self.get_project_by_title(title) 
        if project:
            return project.cast
        return None
    
    def updated_project_schedule(self,title,shooting_schedule):
        project = self.get_project_by_title(title)
        if project:
            project.shooting_schedule = shooting_schedule
            
            
    def updated_project_budget(self,title,budget) :
        project = self.get_project_by_title(title) 
        if project:
            project.budget = budget      
             



# The magical Baobao:In a small village,there is a baobao tree believed to have magical properties.Every season,it bears different
# types of fruits,each with its own unique power.You have decided to create a software system that tracks the changes in the tree
# and  which type of fruit it will bear next season and what powers it will posses .The stytems should also record  the effect of each fruit when consumed.

           
class Fruit:
    def __init__(self, type, power, effect):
        self.type = type
        self.power = power
        self.effect = effect
class Baobab_tree:
    def __init__(self, fruit):
        self.fruit.append(fruit)
    def prediction(self):
        return "Type of fruit to be bored next season"
    def fruit_power(self):
        return "type of power the fruit possesses"
    def fruit_effect(self):
        return "the effect the fruit has when consumed"


# class PossibleFruit:
#     def __init__(self, power, name, effects, seasons):
#         self.power = power
#         self.name = name
#         self.effects = effects
#         self.seasons = seasons
#     def __str__(self):
#         return f"{self.name} ({self.power}): {self.effects} - Seasons: {self.seasons}"
# fruit = []
# firstFruit = PossibleFruit("strength", "baobabseed", "get healthier", "wet")
# fruit.append(firstFruit)

# class Seasons:
#     def __init__(self, seasons):
#         self.seasons = seasons
#     def predictFruit(self):
#         b = [item for item in fruit if item.seasons == self.seasons]
#         return b
# seasonInstance = Seasons("wet")
# fruitsForSeason = seasonInstance.predictFruit()
# for fruit in fruitsForSeason:
#     print(fruit)


tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index+1}. {task}")

def remove_task():
    view_tasks()
    if len(tasks) == 0:
        return

    choice = input("Enter the task number to remove: ")
    try:
        choice = int(choice)
        if choice > 0 and choice <= len(tasks):
            task = tasks.pop(choice - 1)
            print(f"Task '{task}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
    
    
    
    
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    while True:
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = add(num1, num2)
            print("Result:", result)
        elif choice == "2":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == "3":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = multiply(num1, num2)
            print("Result:", result)
        elif choice == "4":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = divide(num1, num2)
            print("Result:", result)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    calculator()


    
