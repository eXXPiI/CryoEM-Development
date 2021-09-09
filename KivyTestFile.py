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
        buttonState =  Button(text="Push Here")
        return buttonState

KivyApp().run()


# M02 End Program