from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class Main(MDApp):
    def build(self):
        return MDLabel(text="hola gente de youtube",font_size=35)
    


if __name__ == "__main__":
    Main().run()