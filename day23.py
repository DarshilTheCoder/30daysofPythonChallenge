#Today I am learning abhout KIVY, which is used to built a cross-platform GUI, because it's a cross-platform framework and support multi-touch,keyboard and mouse input.. You are creating NUI that is Natural User Interface using KIVY, also there is no native controls and widgets, which means you create custom controls and widgets, that allows your applications looks consistent across all platforms. Kivy is basically use for layouts and it have major three layouts like box / float and grid layouts. With kivy one can add events like response to keypress / mouse pointers or touch events etc. Also you can set an event for future too . Kivy have properties that works with EventDispatcher like allow validtion checking and fire events when widgets changes its size or positon. It have KV language that enables us to create a simple user-inertactive interface, also it seperates the logic from main application logic

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class FileHandler:
    def __init__(self,file_name:str,mode:str) -> None:
        self.filename = file_name
        self.mode = mode
        
    def __enter__(self):
        return open(file=self.filename,mode=self.mode)

    def __exit__(self,exc_type, exc_value, traceback):
        print(f"{self.filename} is Closed!")


class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation = 'vertical')
        self.user_input = TextInput(multiline = False, halign ='center',font_size= 55)
        main_layout.add_widget(self.user_input)
        self.solution = TextInput(multiline = False, readonly = True, halign ='center',font_size= 55)
        
        convert_to_celsius_button = Button(
            text="convert to °C",pos_hint = {"center_x":0.5,"center_y":0.5}
        )
        convert_to_celsius_button.bind(on_press = self.on_solution)
        main_layout.add_widget(convert_to_celsius_button)
        
        convert_to_Fahrenheit_button = Button(
            text="convert to Fahrenheit or °F",pos_hint = {"center_x":0.5,"center_y":0.5}
        )
        convert_to_Fahrenheit_button.bind(on_press = self.on_solution)
        main_layout.add_widget(convert_to_Fahrenheit_button)
        main_layout.add_widget(self.solution)

        return main_layout
    
    def on_solution(self,instance):
        try:
            temperature = float(self.user_input.text)
            if instance.text == "convert to °C":
                self.user_input.text = f"{self.user_input.text} degree fahrenheit"
                temp_in_celsius = (temperature - 32) * 5 / 9
                self.solution.text = f"{temp_in_celsius:.2f} degree celsius"
                with FileHandler(file_name='database_23.txt',mode='a') as f:
                    f.write(f"{temperature} degree F value is equals to {temp_in_celsius:.2f} degree C \n")
            else:
                self.user_input.text = f"{self.user_input.text} degree celsius"
                temp_in_fahrenheit = (temperature * 9 / 5) + 32
                self.solution.text = f"{temp_in_fahrenheit:.2f} degree fahrenheit"
                with FileHandler(file_name='database_23.txt',mode='a') as f:
                    f.write(f"{temperature} degree C value is equals to {temp_in_fahrenheit:.2f} degree F \n")
        except ValueError:
            self.solution.text = "Invalid Input!"

        
    
if __name__ == "__main__":
    app = MainApp()
    app.run()