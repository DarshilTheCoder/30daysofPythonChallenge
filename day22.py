#Today I am learning about CLI, CLI is the computer program that is used using a text interface. it have different type of arguments or you can say command line arguments. Positinal arguments which is required for a command to run, second one is the keyword argument which comes in key value pair like --argument_keyword value or --argument_keyword = value and often it have predefined values or default values. Understand how to parse command-line arguments to parser 

#Today's Challenge was to create a Temperature convertor using CLI

import argparse

class FileHandler:
    def __init__(self,file_name:str,mode:str) -> None:
        self.filename = file_name
        self.mode = mode
        
    def __enter__(self):
        return open(file=self.filename,mode=self.mode)

    def __exit__(self,exc_type, exc_value, traceback):
        print(f"{self.filename} is Closed!")

#Creating an argument parser which returns an ArgumentParser Object. 
arg_parser = argparse.ArgumentParser(description="Want to convert Temperature ? from degree Celsius to Fahrenheit or vice versa ")

#Creating an command-line arguments using add_arguments

arg_parser.add_argument("--temperature_value",default=100,type=float,help="Kindly enter the temperature value using --temperature_value value. Example --temperature_value 37.5" )
arg_parser.add_argument("--unit_value",default='C',type=str,help="You have two choices C for Celsius and F for Fahrenheit! Kindly enter the unit value using --unit_value value. Example --unit_value C",choices=['C','F'])

#Parsed command-line arguments to parser
args = arg_parser.parse_args()
temp_value = args.temperature_value
unit_value = args.unit_value



#temperature conversion logic
if unit_value == "C":
    print(f"You are converting degree Celsius to Fahrenheit, because your choice is {unit_value} ")
    # converted_temp = (temp_value - 32) * 5 / 9
    temp_in_fahrenheit = (temp_value * 9 / 5) + 32
    print(f"{temp_value:.2f}°C is equal to  {temp_in_fahrenheit:.2f}°F")
    try:
        with FileHandler(file_name='database_22.txt',mode='a') as f:
            f.write(f"{temp_value:.2f} degree C is equal to  {temp_in_fahrenheit:.2f} degree F \n")
    except FileNotFoundError as e:
        print("database_22.txt file is not found so creating first automcatically")
elif unit_value == "F":
    print(f"You are converting from Fahrenheit to degree Celsius, because your choice is {unit_value} ")
    temp_in_Celsius = (temp_value - 32) * 5 / 9
    print(f"{temp_value:.2f}°F  is equal to {temp_in_Celsius:.2f}°C")
    try:
        with FileHandler(file_name='database_22.txt',mode='a') as f:
            f.write(f"{temp_value:.2f} degree F  is equal to {temp_in_Celsius:.2f} degree C \n")
    except FileNotFoundError as e:
        print("database_22.txt file is not found so creating first automcatically")
