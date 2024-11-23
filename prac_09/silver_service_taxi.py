from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with fanciness and flagfall."""

    flagfall = 4.50  # Class variable for additional charge per fare

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness  # Scale the price per km based on fanciness

    def get_fare(self):
        """Calculate the total fare including the flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
