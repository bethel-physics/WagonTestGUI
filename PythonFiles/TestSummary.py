import tkinter as tk

class TestSummary(tk.Frame):
    def __init__(self, parent, master_window):
        super().__init__(master_window, width=700, height=500, background='coral')

        # Adds the title to the TestSummary Frame
        self.title = tk.Entry(self,  width=13, fg='#0d0d0d',
                               font=('Arial',18,'bold'))
        self.title.insert(tk.END, "Test Summary Page")
        self.title.grid(row= 0, column= 1)
        
        
        # Creates the "table" as a frame object
        self.table = tk.Frame(self)

        # Creating the y - labels
        self.y_labels = []

        # Creating the x - labels
        self.x_labels = ["serial_num", "tester", "label_applied", "database_entry", "label_legibility", "power_cycle", "comments" ]


        # Determines the sizes of the rows and columns
        self.total_rows = len(self.y_labels) + 1
        self.total_columns = len(self.x_labels)
        


        # Add all of the entries from the database into the table
        for entry in self.get_entries_from_DB():
            self.add_entry_to_table(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6])
        



        # Adding in the x_labels to the table
        # Horizontal Labels
        for index in range(self.total_columns):
            self._entry= tk.Entry(self.table, width=13, fg='blue',
                               font=('Arial',12))
            self._entry.grid(row=0, column=index)
            self._entry.insert(tk.END, self.x_labels[index])


        # Adding dummy values to the DataBase

        self.table.grid(row = 1, column= 1)


        # Ensures the frame is the correct size
        self.grid_propagate(0)


    
    def add_entry_to_table(self, serial_num, tester, label_applied, database_entry, label_legibility, power_cycle, comments):
        
        list = [serial_num, tester, label_applied, database_entry, label_legibility, power_cycle, comments]
        
        for index in range(self.total_columns):
            self._entry= tk.Entry(self.table, width=13, fg='blue',
                               font=('Arial',12))
            self._entry.grid(row=self.total_rows, column=index)
            self._entry.insert(tk.END, list[index])

        self.total_rows = self.total_rows + 1


    def get_entries_from_DB(self):
        #TODO Implement this method with the Database
        
        return [["0100256", "Garrett Schindler", "0123", "Row=4, Col=180", "Good", "Good", "NONE" ]]

