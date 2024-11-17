from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class MilesToKmConverterApp(App):
    """App for converting miles to kilometers"""
    result = StringProperty("0.0")

    def build(self):
        """Build the app interface from the KV file"""
        Window.size = (400, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self, miles):
        """Convert miles to kilometers and update the result"""
        try:
            miles = float(miles) if miles else 0.0
            self.result = f"{miles * MILES_TO_KM:.5f}"
        except ValueError:
            self.result = "0.0"

    def handle_increment(self, miles, change):
        """Adjust the miles input up or down by the given change value"""
        try:
            miles = float(miles) if miles else 0.0
            miles += change
            self.root.ids.input_miles.text = str(miles)
            self.handle_conversion(miles)
        except ValueError:
            self.root.ids.input_miles.text = str(change)


if __name__ == '__main__':
    MilesToKmConverterApp().run()
