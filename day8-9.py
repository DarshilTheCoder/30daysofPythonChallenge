#Today I learned about one of most important topic of the programming and that is Object Oriented Programming. Now always thinking why it is called object oriented, because here we are going to create a different different objects which are called as an instance  of a class, that have specific values of properites. Now what's class. Class is nothing but a set of properties and methods or functions, which can be called by making an instance of a oject. So everything is oriented to object, because you create an object in order to run the methods specified in class, also you passed arguments to a object only in order specify the perticular values of properties defined in class and once object is defined it becomes an instance of class and then you can call the function using that  instance.

#Class is a blueprint of what an object looks like. Also learned that we can define the data type of arguments we want while creating a class
#One new thing I learned is the dunder method. Basically it is used so that whenever user just try to print an instance then if dunder method like __str__() or __repr__() is there then it return the str otherwise by default it will return the object

#The main use of creating class is that you don't need to re-create the same thing again and again for different client. For example you are real-estate owner and you are building properites of 5 BHK and you have project of creating 100 such houses. Now you don't create 100 blueprints for each house, will create one blueprint and that's a class only.

import sys
class car:
    def __init__(self,car_name:str,car_brand:str,car_color:str, car_model_year:int) ->None:
        self.name = car_name #This is called properties of a class
        self.brand = car_brand
        self.color = car_color
        self.model_year = car_model_year
        self.engine_on:bool = False
    
    def display(self) -> None:
        print(f"The name of your car is {self.name}")
        print(f"Your car brand name is {self.brand}")
        print(f"The color of your car is {self.color}")
        print(f"You car manufacturing year is {self.model_year}")
    
    def engine_turn_on(self) -> None: #this is called the methods of a class
        if self.engine_on:
            print(f"{self.name} of brand {self.brand}'s engine is already on.")
        else:
            self.engine_on = True
            print(f"{self.name} of brand {self.brand}'s engine is on. Now you can drive your car. Thank you")
    
    def engine_turn_off(self) -> None:
        if self.engine_on:
            self.engine_on = False
            print(f"{self.name} of brand {self.brand}'s engine is off now.")
        else:
            print(f"{self.name} of brand {self.brand}'s engine is already off")
    
    def car_running(self)->None:
        if self.engine_on:
            print(f"{self.name} is ready for run")
        else:
            print(f"{self.name}'s engine is off. Kindly start it")
            user_input = input(f'Want to start {self.name} car engine ? Write yes = ')
            if user_input.lower() == 'yes':
                self.engine_turn_on()
                print(f"Now your car is running. ")
    
    def __str__(self) -> str: #This is called the dunder method 
        return f"This is a '{self.name}' car of brand '{self.brand}'"


class ElectricCar(car):
    def battery_capacity(self,battery_capacity:str):
        print("Welcome to Electric Era")
        print(f"{self.name} car has battery {battery_capacity}")

tiago = car(car_name='tiago',car_brand='TATA',car_color='black',car_model_year=2024) #this is called an instance of a class or you can say that you created an object of class car.
defender = car(car_name='defender', car_brand='Land Rover',car_color='golden',car_model_year=2025)
windsor = ElectricCar(car_name='Windsor',car_brand='MG Motors',car_color='Pearl White',car_model_year=2025)


def main_function():
    user_input = input('Enter the name of car tiago or defender or windsor do you want to exit if yes then write exit= ')
    if user_input.lower() =='tiago':
        tiago.display()
        tiago.engine_turn_on()
        tiago.engine_turn_on()
        tiago.engine_turn_off()
        tiago.car_running()
        tiago.engine_turn_off()
        print(tiago)
    elif user_input.lower() =='defender':
        defender.engine_turn_on()
        defender.engine_turn_on()
        defender.engine_turn_off()
        defender.car_running()
        defender.engine_turn_off()
        print(defender)
    elif user_input.lower() == 'windsor':
        windsor.display()
        windsor.battery_capacity(battery_capacity='120 KW')
        windsor.engine_turn_on()
        windsor.engine_turn_on()
        windsor.engine_turn_off()
        windsor.car_running()
        windsor.engine_turn_off()
    elif user_input.lower() == 'exit':
        sys.exit()
    else:
        print("Kindly enter the name of car from given two option only.")
        main_function()
        
main_function()