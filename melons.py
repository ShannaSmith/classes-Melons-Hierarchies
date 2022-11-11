"""Classes for melon orders."""
class AbstractMelonOrder:
    def __init__(self,species,qty):
        self.species = species
        self.qty=qty
        self.shipped = False
        
    def get_total(self):
        """Calculate price, including tax."""
        order_qty = int(self.qty)
        base_price = 5
        if self.species == "Christmas melon":
            base_price = base_price * 5
        else:
             base_price = 5
        if self.order_type == "international" and order_qty < 10:
            total = ((1 + self.tax) * self.qty * base_price) + 3.00
        else:
            total = (1 + self.tax) * self.qty * base_price

        return total
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
    

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
     
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order() attributes."""
        super().__init__(species, qty)
      
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    
    def get_country_code(self):
        """Return the country code."""

        return self.country_code
