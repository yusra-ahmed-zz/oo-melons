"""This file should have our order classes in it."""


class AbstractMelonOrder(object):
    """ A melon order."""

    def __init__(self, species, qty):
        # include tax, order_type, country_code in parameters?
        self.species = species
        self.qty = qty
        self.shipped = False
        # self.tax = tax
        # self.order_type()

    def get_total(self):
        """Calculate price."""

        base_price = 5
        if self.species.lower() == 'christmas':
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
        
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        # self.species = species
        # self.qty = qty
        # self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08
        super(DomesticMelonOrder,self).__init__(species, qty)

    # def get_total(self):
    #     """Calculate price."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price
    #     return total

    # def mark_shipped(self):
    #     """Set shipped to true."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        # self.species = species
        # self.qty = qty
        self.country_code = country_code
        # self.shipped = False
        self.order_type = "international"
        self.tax = 0.17
        super(InternationalMelonOrder,self).__init__(species,qty)


    def get_total(self):
        total = super(InternationalMelonOrder,self).get_total()
        if self.qty < 10:
            total = total + 3

        return total

    # def get_total(self):
    #     """Calculate price."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price
    #     return total

    # def mark_shipped(self):
    #     """Set shipped to true."""

    #     self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
