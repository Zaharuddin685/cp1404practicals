from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy app to demonstrate dynamic label creation."""

    def __init__(self, **kwargs):
        """Initialize the app with a list of names."""
        super().__init__(**kwargs)
        self.names_list = ["Alice", "Bob", "Charlie", "David", "Eve"]  # List of names to display

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels Example"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()  # Call method to create labels dynamically
        return self.root

    def create_labels(self):
        """Create a label for each name and add it to the layout."""
        for name in self.names_list:
            # Create a new label for each name in the list
            temp_label = Label(text=name)
            # Add the label to the "main" layout widget
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
