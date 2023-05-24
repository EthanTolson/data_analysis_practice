import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import replace

class DataAnalysis():
    def __init__(self, dataframe1, dataframe2):
        self.df1 = dataframe1
        self.df2 = dataframe2
        self.arrange_columns()
        self.convert_date_col()
        self.remove_extra_cols()

    def arrange_columns(self):
        """
        Orders the Columns of Both Data Sets
        """
        col = ["Date", "Open", "High", "Low", "Close", "Volume", "Adj Close"]
        self.df1 = self.df1[col]
        self.df2 = self.df2[col]

    def convert_date_col(self):
        if "-" in self.df1["Date"][0]:
            for date in self.df1["Date"]:
                self.df1["Date"].replace({date : self._convert_date(date)}, inplace = True)
        
        if "-" in self.df2["Date"][0]:
            for date in self.df2["Date"]:
                self.df2["Date"].replace({date : self._convert_date(date)}, inplace = True)

    def _convert_date(self, date):
        """
        Converts Dates from YYYY-MM-DD format to MM/DD/YYYY

        Parameters:
        date : string in YYYY-MM-DD format
        """
        if "-" in date:
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
        else:
            return date

    def get_extra_cols_front(self, df1, df2):
        """
        Gets the index of the first dataset date that matches the first date of the second dataset

        Parameters:
        df1 : first dataframe (Should have columns with dates that exist before the dates of the second dataframe)
        df2 : second dataframe (Dates should be after the dates of the second)

        Returns:
        Index of the matching date in the longer dataframe
        """
        i = 0
        for date in df1["Date"]:
            if self._convert_date(date) == self._convert_date(df2["Date"][0]):
                break
            i += 1

        return i

    def get_extra_cols_back(self, df1, df2):
        """
        Gets the index of the first dataset date that matches the last date of the second dataset

        Parameters:
        df1 : first dataframe (Should have columns with dates that exist after the dates of the second dataframe)
        df2 : second dataframe (Dates should be after the dates of the second)

        Returns:
        Index of the matching date in the longer dataframe
        """
        i = len(df1)
        for date in reversed(df1["Date"]):
            if self._convert_date(date) == self._convert_date(df2["Date"][len(df2) - 1]):
                break
            i -= 1
        return i

    def remove_extra_cols(self):
        """
        Removes the extra columns from the Google dataset
        """
        list_columns_delete = []

        for i in range(0, self.get_extra_cols_front(self.df1, self.df2)):
            list_columns_delete.append(i)

        for i in range(self.get_extra_cols_back(self.df1, self.df2), len(self.df1)):
            list_columns_delete.append(i)
        if len(list_columns_delete) != 0:
            self.df1 = self.df1.drop(index = list_columns_delete)

        self.df1.reset_index(inplace = True, drop = True)
        self.df2.reset_index(inplace = True, drop = True)



    def get_percent_return(self, df1):
        """
        Returns the percentage change between the first data point and the last
        """
        return ((df1["Adj Close"][len(df1) - 1] - df1["Adj Close"][0]) / df1["Adj Close"][0]) + 1

    def get_new_amount(self, amount, df):
        """
        returns the amount after applying the change
        """
        if df == 1:
            return f"$ {amount * self.get_percent_return(self.df1):.2f}"
        else:
            return f"$ {amount * self.get_percent_return(self.df2):.2f}"

    def get_avg_vol_diff(self):
        """
        Returns the difference in the average volume of stocks traded
        """
        avg = self.df2.mean(numeric_only = True)["Volume"] - self.df1.mean(numeric_only = True)["Volume"]
        return str(int(avg))

    def display_graph(self, comp_name, col_name):
        """
        Displays t a graph based off of user choice
        """
        if comp_name == "Tesla":
            x = self.df2["Date"]
            y = self.df2[col_name]
        else:
            x = self.df1["Date"]
            y = self.df1[col_name]
        plt.bar(x, y)
        plt.title(f"{col_name} over Time ({comp_name})")
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.show()

    def get_df1_overview(self):
        """
        Gets data overview for google
        """
        return self.df1.describe()

    def get_df2_overview(self):
        """
        Gets data overview for tesla
        """
        return self.df2.describe()