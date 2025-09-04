from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import tabs.bar_chart as bc

Builder.load_file('styles/main.kv')

class LoginScreen(Screen):
    def login(self, username, password):
        if not username or not password:
            self.ids.status.text = 'Completa todos los campos'
            self.ids.status.color = (1, 0, 0, 1)
            return
        if username == 'admin' and password == '1234':
            self.ids.status.text = 'Acceso correcto'
            self.ids.status.color = (0, 1, 0, 1)
            self.manager.current = 'home'
        else:
            self.ids.status.text = 'Credenciales incorrectas'
            self.ids.status.color = (1, 0, 0, 1)
            self.ids.pwd.text = '' # Limpiar campo
            self.ids.pwd.focus = True # Foco en error

class HomeScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        # Create the screen manager
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        return sm
        
if __name__ == "__main__":
    MainApp().run()