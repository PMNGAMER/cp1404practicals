class Monitor:
    """Represent a Monitor with model, width, and height."""

    def __init__(self, model, width, height):
        """Initialize a Monitor instance with model, width, and height."""
        self.model = model
        self.width = width
        self.height = height

    def get_resolution(self):
        """Return the resolution of the monitor as a tuple (width, height)."""
        return (self.width, self.height)

    def get_total_pixels(self):
        """Return the total number of pixels (width * height)."""
        return self.width * self.height
