## Preamble
"""
# Program: KivyTestFile.py
# Version: 0.0.1
# Author: Jonathan Myers
# Date Created: Thu Sep  9 15:25:41 2021
# Date Modified: Thu Sep  9 15:25:41 2021
# Purpose: Test the Kivy GUI framework for processing interface for HTC.
# Imports: Kivy
# Inputs/Arguments: 
# Outputs/Returns: 
"""

## Articles
import kivy
from kivy.app import App
from kivy.uix.button import Button

kivy.require("2.0.0")

class KivyApp(App):
    def build(self):
        buttonState =  Button(text="Push Here",
                              font_size="20sp",
                              background_color=(1,1,1,1),
                              color=(1,1,1,1),
                              size=(32,32),
                              size_hint=(0.2,0.2),
                              pos=(300,300))
        buttonState.bind(on_press=self.commandRun)
        return buttonState
    
    def commandRun(self,event):
        print("Button Pressed")

KivyApp().run()


# M02 End Program