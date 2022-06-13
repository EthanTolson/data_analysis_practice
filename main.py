import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from os import path
FILEPATH = f"{path.dirname(path.abspath(__file__))}"

def main():
    dataframe = pd.read_csv(FILEPATH+"\\Tesla.csv")
    print(dataframe.head(2))
    print(dataframe.tail(2))
    print("------------------------------")
    print(dataframe.mean(0, numeric_only=True, skipna=True))
    print(dataframe.describe())
    print()
    #print(dataframe["Open"].to_numpy())
    for column in dataframe:
        print(column)

    # Graph of open prices over time
    date = dataframe["Date"]
    open_price = dataframe["Open"]

    plt.bar(date, open_price)
    plt.title("Open Prices over Time")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()

if __name__ =="__main__":
    main()