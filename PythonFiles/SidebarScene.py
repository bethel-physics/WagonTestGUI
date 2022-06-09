from msvcrt import LK_NBLCK
import tkinter as tk


class SidebarScene(tk.Frame):
    def __init__(self, parent, sidebar_frame, data_holder):
        super().__init__(sidebar_frame, width=213, height = 500, bg = 'green')

        self.data_holder = data_holder

        self.update_sidebar(parent)

    def update_sidebar(self, parent):

        # Create a set of labels for the side bar

        lbl_login = tk.Label(
            self, 
            text = 'Login Page'
            )
        lbl_login.grid(column = 0, row = 0)

        lbl_scan = tk.Label(
            self, 
            text = 'Scan Page'
            )
        lbl_scan.grid(column = 0, row = 1)

        lbl_test1 = tk.Label(
            self, 
            text = 'Test 1'
            )
        lbl_test1.grid(column = 0, row = 2)

        lbl_test2 = tk.Label(
            self, 
            text = 'Test 2'
            )
        lbl_test2.grid(column = 0, row = 3)

        lbl_test3 = tk.Label(
            self, 
            text = 'Test 3'
            )
        lbl_test3.grid(column = 0, row = 4)

        lbl_test4 = tk.Label(
            self, 
            text = 'Test 4'
            )
        lbl_test4.grid(column = 0, row = 5)

        lbl_summary = tk.Label(
            self, 
            text = 'Test Summary'
            )
        lbl_summary.grid(column = 0, row = 6)

        btn_login = tk.Button(
            self, 
            text = 'GO',
            command = lambda: self.login_btn_action(parent)
            )
        btn_login.grid(column = 2, row = 0)

        btn_scan = tk.Button(
            self, 
            text = 'GO',
            command = lambda: self.scan_btn_action(parent)
            )
        btn_scan.grid(column = 2, row = 1)

        btn_test1 = tk.Button(
            self, 
            text = 'GO',
            command = lambda: self.test1_btn_action(parent)
            )
        btn_test1.grid(column = 2, row = 2)

        btn_test2 = tk.Button(
            self, 
            text = 'GO',
            command = lambda: self.test2_btn_action(parent)
            )
        btn_test2.grid(column = 2, row = 3)

        btn_test3 = tk.Button(
            self, 
            text = 'GO',
            command = lambda: self.test3_btn_action(parent)
            )
        btn_test3.grid(column = 2, row = 4)

        btn_test4 = tk.Button(
            self, 
            text = 'GO',
            command = lambda: self.test4_btn_action(parent)
            )
        btn_test4.grid(column = 2, row = 5)

        btn_summary = tk.Button(
            self, 
            text = 'GO',
            command = lambda: self.summary_btn_action(parent)
            )
        btn_summary.grid(column = 2, row = 6)

        self.grid_propagate(0)
    
    def login_btn_action(self, _parent):
        _parent.set_frame(_parent.login_frame)

    def scan_btn_action(self, _parent):
        _parent.set_frame(_parent.scan_frame)

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