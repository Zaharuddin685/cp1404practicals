from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A special Taxi with fanciness and flagfall added."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi with fanciness scaling."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Override price_per_km using class variable from Taxi
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the total fare including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like Taxi but include flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
