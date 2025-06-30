import random
from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operators = ['/','*','+','-']
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation = 'vertical')
        self.solution = TextInput(multiline = False, readonly = True, halign ='right',font_size= 55)
        main_layout.add_widget(self.solution)
        buttons = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['.','0','C','+']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text= label,pos_hint={"center_x":.5,"center_y":.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=",pos_hint = {"center_x":0.5,"center_y":0.5}
        )
        equals_button.bind(on_press = self.on_solution)
        main_layout.add_widget(equals_button)
        
        return main_layout
    
    
    def on_button_press(self,instance):
        current = self.solution.text
        button_text= instance.text
        
        if button_text == "C":
            #Clear the solution
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                #   Don't add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                #First character cannot be an operator
                return
            else:
                new_text= current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator =self.last_button in self.operators
    
    def on_solution(self,instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ =="__main__":
    app = MainApp()
    app.run()




# class ButtonApp(App):
#     def build(self):
        
        # lable = Label(text="Hello!", font_size= '40sp')
        # img = Image(source = 'python-hero.jfif')
        # layout = BoxLayout(padding=50,spacing=10,orientation = 'vertical') #here in layout padding you can put a list of padding that's left,top,right,bottom
        
        # for i in range(5):
        #     btn = Button(text=f"Button {i+1}",background_color=random.choice(colors))
            
        #     btn.index = i+1
        #     btn.bind(on_press=self.on_press_button)
            
        #     layout.add_widget(btn)
        
    #     return Button()

    # def on_press_button(self):
    #     print(f"You press button")

# if __name__ == "__main__":
#     app = ButtonApp()
#     app.run()