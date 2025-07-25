"""
This module defines the electric field in the solar cell.
"""

class ElectricField:

    """
    The method value_at gives the value of the electric field,
    at the given position 'x'.
    """

    def __init__(self, E_value):
        self.E_value = E_value

    def value_at(self, x):
        return self.E_value
