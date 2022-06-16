import numpy as np
from dataclasses import replace
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from os import path
FILEPATH = f"{path.dirname(path.abspath(__file__))}"

def convert_date(date):
    """
    Converts Dates from YYYY-MM-DD format to MM/DD/YYYY

    Parameters:
    date : string in YYYY-MM-DD format
    """
    # places the year at the end
    date_conv = date[5:] + "-" + date[:4]

    # replaces the - with /
    date_conv = date_conv.replace("-", "/")


    if date_conv[0] == "0" and date_conv[3] == "0":
        date_conv = date_conv[1:3] + date_conv[4:]
    elif date_conv[0] == "0":
        date_conv = date_conv[1:]
    elif date_conv[3] == "0":
        date_conv = date_conv[0:3] + date_conv[4:]
    
    return date_conv

def get_extra_cols_front( df1, df2):
    """
    Gets the index of the first dataset date that matches the first date of the second dataset

    Parameters:
    df1 : first dataframe (Should have )
    
    """
    i = 0
    for date in df1["Date"]:
        if convert_date(date) == df2["Date"][0]:
            break
        i += 1

    return i

def get_extra_cols_back(df1, df2):
    i = len(df1)
    for date in reversed(df1["Date"]):
        if convert_date(date) == df2["Date"][len(df2) - 1]:
            break
        i -= 1
    return i

def main():
    tesla_dataframe = pd.read_csv(FILEPATH+"\\Tesla.csv")
    google_dataframe = pd.read_csv(FILEPATH + "\\GOOGL.csv")
    print(tesla_dataframe.head(4))
    print(tesla_dataframe.tail(2))
    print("------------------------------")
    print(tesla_dataframe.mean(0, numeric_only=True, skipna=True))
    print(tesla_dataframe.describe())
    print()

    print(google_dataframe.head(2))
    print(google_dataframe.tail(2))

    #print(tesla_dataframe["Open"].to_numpy())
    for column in tesla_dataframe:
        print(column)

    print("----------------------")


    list_columns_delete = []

    for i in range(0, get_extra_cols_front(google_dataframe, tesla_dataframe)):
        list_columns_delete.append(i)
    
    for i in range(get_extra_cols_back(google_dataframe, tesla_dataframe), len(google_dataframe)):
        list_columns_delete.append(i)

    google_dataframe = google_dataframe.drop(index = list_columns_delete)

    print(google_dataframe.head(2))
    print(google_dataframe.tail(2))

    print("--------------------")

    print(google_dataframe.dtypes)
    print(tesla_dataframe.dtypes)

    # Graph of open prices over time
    tesla_date = tesla_dataframe["Date"]
    tesla_open_price = tesla_dataframe["Open"]

    plt.bar(tesla_date, tesla_open_price)
    plt.title("Open Prices over Time")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()

    google_date = google_dataframe["Date"]
    google_open_price = google_dataframe["Open"]



    plt.bar(google_date, google_open_price)
    plt.title("Open Prices over Time")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()

if __name__ =="__main__":
    main()