from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """App that dynamically generates labels for a list of names"""

    def __init__(self, **kwargs):
        """Initialize the app with a predefined list of names"""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        """Build the Kivy interface"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a Label for each name and add it to the GUI"""
        for name in self.names:
            temp_label = Label(text=name, font_size=24)
            self.root.ids.main.add_widget(temp_label)


if __name__ == '__main__':
    DynamicLabelsApp().run()
