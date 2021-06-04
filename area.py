import pandas as pd

data = pd.read_csv("Book1.csv")


class Area:
    def __init__(self, **kwargs):
        self.decimal = kwargs.get("decimal")
        self.origin_unit = kwargs.get("origin_unit")
        self.destiny_unit = kwargs.get("destiny_unit")
        self.origin_qty = kwargs.get("origin_qty")
        self.unit_list = data["Unit"].tolist()
        self.factors_list = data[self.origin_unit].tolist()

    def convertor(self):
        position = self.unit_list.index(self.destiny_unit)
        result = round(self.origin_qty * self.factors_list[position], self.decimal)
        return result
