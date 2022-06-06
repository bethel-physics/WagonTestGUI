import tkinter as tk

class TestSummary(tk.Frame):
    def __init__(self, parent, master_window):
        super().__init__(master_window, width=700, height=500, background='coral')

        self.table = tk.Frame(self)

        self.y_labels = []
        self.x_labels = ["Speed", "Acceleration", "Resistance"]

        self.total_rows = len(self.y_labels) + 1
        self.total_columns = len(self.x_labels)
        


        # Add all of the entries from the database into the table
        for entry in self.get_entries_from_DB():
            self.add_entry_to_table(entry[0], entry[1], entry[2], entry[3])
        



        # Adding in the x_labels to the table
        # Horizontal Labels
        for index in range(self.total_columns):
            self._entry= tk.Entry(self.table, width=13, fg='blue',
                               font=('Arial',16,'bold'))
            self._entry.grid(row=0, column=index + 1)
            self._entry.insert(tk.END, self.x_labels[index])


        self.add_entry_to_table("Garrett's Value", 100, 200, "30 Ohms")
        self.add_entry_to_table("Andrew's Entry", 150, 200, "764 Ohms")

        self.table.grid()


        self.grid_propagate(0)


    
    def add_entry_to_table(self, _title, _speed, _acceleration, _resistance):
        
        list = [_title, _speed, _acceleration, _resistance]
        
        for index in range(self.total_columns + 1):
            self._entry= tk.Entry(self.table, width=13, fg='blue',
                               font=('Arial',16,'bold'))
            self._entry.grid(row=self.total_rows + 1, column=index)
            self._entry.insert(tk.END, list[index])

        self.total_rows = self.total_rows + 1


    def get_entries_from_DB(self):
        #TODO Implement this method with the Database
        
        return [["Sample_Test", "10 m/s", "15.2 m/s^2", "45 Ohms"]]

