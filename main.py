import numpy as np
import pandas as pd
import matplotlib as mpl
from os import path
FILEPATH = f"{path.dirname(path.abspath(__file__))}"

def main():
    dataframe = pd.read_csv(FILEPATH+"\\Tesla.csv")
    print(dataframe.head(2))
    print(dataframe.tail(2))
    print(dataframe.mean(0))

if __name__ =="__main__":
    main()