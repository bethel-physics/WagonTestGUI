import tkinter as tk
from PIL import ImageTk as iTK
from PIL import Image
import tkinter.font as font


class SidebarScene(tk.Frame):
    def __init__(self, parent, sidebar_frame, data_holder):
        super().__init__(sidebar_frame, width=213, height = 500, bg = '#808080', padx = 10, pady=10)

        self.data_holder = data_holder

        self.update_sidebar(parent)

    def update_sidebar(self, parent):

        # List for creating check marks with for loop
        self.list_of_pass_fail = [
            self.data_holder.test1_pass, 
            self.data_holder.test2_pass, 
            self.data_holder.test3_pass, 
            self.data_holder.test4_pass
            ]

        # For loop to create checkmarks based on pass/fail
        for index in range(len(self.list_of_pass_fail)):
            if(self.list_of_pass_fail[index] == True):
                # Create a photoimage object of the QR Code
                Green_Check_Image = Image.open("./PythonFiles/GreenCheckMark.png")
                Green_Check_Image = Green_Check_Image.resize((50,50), Image.ANTIALIAS)
                Green_Check_PhotoImage = iTK.PhotoImage(Green_Check_Image)
                GreenCheck_Label = tk.Label(self, image=Green_Check_PhotoImage, width=50, height=50, bg = '#808080')
                GreenCheck_Label.image = Green_Check_PhotoImage

                GreenCheck_Label.grid(row=index + 2, column=1)

        # Variables for easy button editing
        btn_height = 3
        btn_width = 18
        btn_font = ('Arial', 10)
        btn_pady = 5

        self.btn_login = tk.Button(
            self,
            pady = btn_pady,
            text = 'LOGIN PAGE',
            height = btn_height,
            width = btn_width,
            font = btn_font
        )
        self.btn_login.grid(column = 0, row = 0)

        self.btn_scan = tk.Button(
            self,
            pady = btn_pady,
            text = 'SCAN PAGE',
            height = btn_height,
            width = btn_width,
            font = btn_font
        )
        self.btn_scan.grid(column = 0, row = 1)

        self.btn_test1 = tk.Button(
            self, 
            pady = btn_pady,
            text = 'GEN. RESIST. TEST',
            height = btn_height,
            width = btn_width,
            font = btn_font,
            command = lambda: self.test1_btn_action(parent)
            )
        self.btn_test1.grid(column = 0, row = 2)

        if self.data_holder.test1_pass == True:
            self.btn_test1.config(state = 'disabled')


        self.btn_test2 = tk.Button(
            self,
            pady = btn_pady, 
            text = 'ID RESISTOR TEST',
            height = btn_height,
            width = btn_width,
            font = btn_font,
            command = lambda: self.test2_btn_action(parent)
            )
        self.btn_test2.grid(column = 0, row = 3)

        if self.data_holder.test2_pass == True:
            self.btn_test2.config(state = 'disabled')

        self.btn_test3 = tk.Button(
            self, 
            pady = btn_pady,
            text = 'I2C COMM. TEST',
            height = btn_height,
            width = btn_width,
            font = btn_font,
            command = lambda: self.test3_btn_action(parent)
            )
        self.btn_test3.grid(column = 0, row = 4)

        if self.data_holder.test3_pass == True:
            self.btn_test3.config(state = 'disabled')

        self.btn_test4 = tk.Button(
            self, 
            pady = btn_pady,
            text = 'BIT RATE TEST',
            height = btn_height,
            width = btn_width,
            font = btn_font,
            command = lambda: self.test4_btn_action(parent)
            )
        self.btn_test4.grid(column = 0, row = 5)
        if self.data_holder.test4_pass == True:
            self.btn_test4.config(state = 'disabled')

        self.btn_summary = tk.Button(
            self, 
            pady = btn_pady,
            text = 'TEST SUMMARY',
            height = btn_height,
            width = btn_width,
            font = btn_font,
            command = lambda: self.summary_btn_action(parent)
            )
        self.btn_summary.grid(column = 0, row = 6)

        self.grid_propagate(0)

    def test1_btn_action(self, _parent):
        _parent.set_frame(_parent.test1_frame)

    def test2_btn_action(self, _parent):
        _parent.set_frame(_parent.test2_frame)

    def test3_btn_action(self, _parent):
        _parent.set_frame(_parent.test3_frame)

    def test4_btn_action(self, _parent):
        _parent.set_frame(_parent.test4_frame)

    def summary_btn_action(self, _parent):
        _parent.set_frame(_parent.testing_finished_frame)

    def disable_all_buttons(self):
        self.btn_login.config(state = 'disabled')
        self.btn_scan.config(state = 'disabled')
        self.btn_test1.config(state = 'disabled')
        self.btn_test2.config(state = 'disabled')
        self.btn_test3.config(state = 'disabled')
        self.btn_test4.config(state = 'disabled')
        self.btn_summary.config(state = 'disabled')

    def disable_all_but_log_scan(self):
        self.btn_test1.config(state = 'disabled')
        self.btn_test2.config(state = 'disabled')
        self.btn_test3.config(state = 'disabled')
        self.btn_test4.config(state = 'disabled')
        self.btn_summary.config(state = 'disabled')

    def disable_all_btns_but_login(self):
        self.btn_scan.config(state = 'disabled')
        self.btn_test1.config(state = 'disabled')
        self.btn_test2.config(state = 'disabled')
        self.btn_test3.config(state = 'disabled')
        self.btn_test4.config(state = 'disabled')
        self.btn_summary.config(state = 'disabled')

    def disable_login_button(self):
        self.btn_login.config(state = 'disabled')

    def disable_scan_button(self):
        self.btn_scan.config(state = 'disabled')