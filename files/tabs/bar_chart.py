from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
    
class BarChartWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = [30, 70, 45, 90, 60]
        self.bind(size=self.update_chart, pos=self.update_chart)  # redraw when resized
        self.draw_bars()

    def draw_bars(self):
        self.canvas.clear()
        with self.canvas:
            Color(0.2, 0.6, 0.86, 1) 
            bar_width = self.width / (len(self.data) * 2)
            spacing = bar_width
            for index, value in enumerate(self.data):
                x = spacing + index * (bar_width + spacing)
                y = 0
                Rectangle(pos=(self.x + x, self.y + y), size=(bar_width, value))

    def update_chart(self, *args):
        self.draw_bars()