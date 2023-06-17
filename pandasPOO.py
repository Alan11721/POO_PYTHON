import pandas as pd


class MiDataFrame(pd.DataFrame):
    def __init__(self, args):
        super().__init__(args)
        print(args)

    def prom_columnas(self):
        return self.mean()


datos = {
    'A': [24.0, 33.2, 30.2, 29.4, 29.3],
    'B': [34.0, 30.2, 31.2, 29.4, 29.3]
}

df = MiDataFrame(datos)
print(df.prom_columnas())