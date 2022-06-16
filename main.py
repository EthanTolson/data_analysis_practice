import pandas as pd
from display import Display
from os import path
FILEPATH = f"{path.dirname(path.abspath(__file__))}"

def main():
    tesla_dataframe = pd.read_csv(FILEPATH+"\\Tesla.csv")
    google_dataframe = pd.read_csv(FILEPATH + "\\GOOGL.csv")
    display1 = Display(google_dataframe, tesla_dataframe)
    display1.drawInterface()
    display1.window.mainloop()

if __name__ == "__main__":
    main()