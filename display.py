import tkinter as tk
from data_analysis import DataAnalysis

class Display():
    def __init__(self, df1, df2):
        # create tkinter object set the title and create a dataanalysis object to call functions
        self.window = tk.Tk()
        self.window.title("Tesla v. Google")
        self.window.state('zoomed')
        self.window.geometry("500x500")
        self.data_analysis = DataAnalysis(df1, df2)

    def drawInterface(self):
        # list of possible companies and columns a user can select
        variableOptionsComp = ["Tesla", "Google"]
        variableOptionsCol = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]

        # these buttons controll the actions the user has
        self.button1 = tk.Button(text = "Display Graph", foreground = "White", background = "Blue", activebackground = "Pink", font = 2, width = 15, height = 2, command = self.displayGraph)
        self.button2 = tk.Button(text = "Calculate Amount", foreground = "White", background = "Blue", activebackground = "Pink", font = 2, width = 15, height = 2, command = self.calculate_new_amount)
        self.button3 = tk.Button(text = "Average\nVolume", foreground = "White", background = "Blue", activebackground = "Pink", font = 2, width = 15, height = 2,command = self.calc_average_difference_volume)
       
        #amount to check
        self.entry1 = tk.Entry()
    


        #output for the amount you would have made
        self.label1 = tk.Label()

        # label for average volume
        self.label2 = tk.Label(text= "Click the Average Volume Button")
        
        
        #drop down menus
        self.clicked1 = tk.StringVar()
        self.clicked1.set("Tesla")
        self.dropDown1 = tk.OptionMenu(self.window, self.clicked1, *variableOptionsComp)

        self.clicked2 = tk.StringVar()
        self.clicked2.set("Open")
        self.dropDown2 = tk.OptionMenu(self.window, self.clicked2, *variableOptionsCol)

        self.clicked3 = tk.StringVar()
        self.clicked3.set("Tesla")
        self.dropDown3 = tk.OptionMenu(self.window, self.clicked3, *variableOptionsComp)

        #placing all buttons, entries, and dropdown menus onto the window
        self.label3 = tk.Label(text = "If you invested $")
        self.label3.grid(row=1, column=1, padx=10, pady=10)
        self.entry1.grid(row=1, column=2, padx=10, pady=10)
        self.label4 = tk.Label(text = "in")
        self.label4.grid(row=1, column=3, padx=10, pady=10)
        self.label4 = tk.Label(text = "in 2010 you would have had")
        self.label4.grid(row=1, column=5, pady=10)
        self.label5 = tk.Label(text = "in 2017.")
        self.label5.grid(row=1, column=7, pady=10)

        self.label8 = tk.Label(text = "Google")
        self.label8.grid(row=3, column=8, padx = 10, pady=10)
        self.label9 = tk.Label(text = "Tesla")
        self.label9.grid(row=3, column=1, padx = 10, pady=10)

        self.label6 = tk.Label(text = self.data_analysis.get_df1_overview())
        self.label6.grid(row=4, column=6, rowspan = 5, columnspan = 5, padx = 10, pady=10)
        self.label7 = tk.Label(text = self.data_analysis.get_df2_overview())
        self.label7.grid(row=4, column=0, rowspan = 5, columnspan = 5, padx = 10, pady=10)
        
        self.dropDown1.grid(row=2, column=1, padx=10, pady=10)
        self.dropDown2.grid(row=2, column=2, padx=10, pady=10)
        self.dropDown3.grid(row=1, column=4, padx=10, pady=10)
    
        self.button1.grid(row=2,column=0, padx=10, pady=10)
        self.button2.grid(row=1, column=0, padx=10, pady=10)
        self.button3.grid(row=0, column=0, padx=10, pady=10)
        
        self.label2.grid(row=0,column=1,padx=10, pady=10)
    
    #These functions are called when a button is pressed
    def displayGraph(self):
        self.data_analysis.display_graph(self.clicked1.get(), self.clicked2.get())
    
    def calculate_new_amount(self):
        try:
            if self.clicked3.get() == "Tesla":
                self.label1.destroy()
                self.label1 = tk.Label(text = self.data_analysis.get_new_amount(float(self.entry1.get()), 2))
                self.label1.grid(row = 1, column = 6,  pady = 10)
            elif self.clicked3.get() == "Google":
                self.label1.destroy()
                self.label1 = tk.Label(text = self.data_analysis.get_new_amount(float(self.entry1.get()), 1))
                self.label1.grid(row = 1, column = 6, pady = 10)
        except:
            self.label1.destroy()
            self.label1 = tk.Label(text = "Enter a valid number!")
            self.label1.grid(row = 1, column = 6, padx = 10, pady = 10)

    def calc_average_difference_volume(self):
        self.label2.destroy()
        self.label2 = tk.Label(text = "Tesla traded " + self.data_analysis.get_avg_vol_diff() + " more shares than Google each day on average.")
        self.label2.grid(row=0,column=1, columnspan = 3, padx=10, pady=10)