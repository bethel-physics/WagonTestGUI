from Tkinter import *
import ttk
from tkFileDialog import askopenfilename
from read_barcode import read_barcode
from board_requests import add_board_info, add_initial_tests, add_general_test, get_test_list, verify_person
import os

# Need to make inspection its own test

class TestEntryGUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createInitWidgets()

    def clearWindow(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def on_back(self, master=None):
        self.clearWindow()
        self.__init__()

    def open_file(self):
        self.attach = askopenfilename(title="Select Attachment")
        self.attach_btn_lbl["text"] = self.attach
        self.attach_btn_lbl.pack(side = LEFT)
        self.update()

    def createTopBar(self, lbl):
        self.frm_tb = Frame(master = self.master, width = 1200)

        self.lbl_tb = Label(font=("Arial Bold", 30), width = 30, height=2, text=lbl, master=self.frm_tb)
        self.QUIT = Button(text = "X", fg="red", command=self.quit, master=self.frm_tb)

        self.QUIT.pack(side=LEFT, padx = 10)
        self.lbl_tb.pack(side=LEFT)

        self.frm_tb.pack(side=TOP)

    def createInitWidgets(self):
        tb_label = "HGCAL Wagon QC Test"
        self.createTopBar(tb_label)

        self.btn_frm = Frame(master = self.master, padx = 50, pady = 50, width = 1200, height =600)

        self.info_btn = Button(master=self.btn_frm, text="Register New Wagon", width=20, height = 10, command=self.createInfoWidgets)
        self.info_btn.pack(side="left", padx = 50)

        #self.init_test_btn = Button(master = self.btn_frm, text="Add Initial Board Test", width = 20, height = 10, command=self.createInitialTestWidgets)
        #self.init_test_btn.pack(side="left", padx = 50)

        self.test_btn = Button(master = self.btn_frm, text="Run Wagon Test", width = 20, height = 10, command=self.createGeneralTestWidgets)
        self.test_btn.pack(side="left", padx = 50)

        self.btn_frm.pack(expand=True)

    def createInfoWidgets(self):
        self.clearWindow()

        lbl_new = "Register New Wagon"
        self.createTopBar(lbl_new)

        self.back = Button(master=self.frm_tb, text = "Back", command = self.on_back )
        self.back.pack(side=LEFT, padx=10)
        
        self.frm_tb.pack(side=TOP)
        
        self.main_info_frm = Frame(master=self.master, width = 1200, height = 1000, padx = 20, pady=20)

        self.general_frm = Frame(master = self.main_info_frm, width = 500, height = 200, relief=RAISED, borderwidth=5)

        self.general_lbl = Label(master = self.general_frm, text="General Info", font = ("Arial Bold", 20))
        self.general_lbl.pack(side=TOP, pady = 10)

        self.serial_num_frm = Frame(master = self.general_frm, padx=10, pady=10)
        self.serial_num_lbl = Label(master=self.serial_num_frm, text = "Serial Number (or scan barcode)")
        self.serial_num_ent = Entry(master=self.serial_num_frm)

        self.serial_num_lbl.pack(side=LEFT, padx=5)
        self.serial_num_ent.pack(side=LEFT, padx=5)
        self.serial_num_frm.pack(side=TOP)

        self.location_frm = Frame(master = self.general_frm, padx=10, pady=10)
        self.location_lbl = Label(master=self.location_frm, text = "Location")
        self.location_ent = Entry(master=self.location_frm)

        self.location_lbl.pack(side=LEFT, padx=5)
        self.location_ent.pack(side=LEFT, padx=5)
        self.location_frm.pack(side=LEFT)

        self.engine_frm = Frame(master = self.main_info_frm, width=500, height = 400, relief=RAISED, borderwidth = 5 )
        
        self.engine_lbl = Label(master = self.engine_frm, text="Engine Info", font = ("Arial Bold", 20))
        self.engine_lbl.pack(side=TOP, pady = 10)
        
        self.daq_frm = Frame(master = self.engine_frm, padx=10, pady=10)
        self.daq_lbl = Label(master=self.daq_frm, text = "DAQ Chip ID")
        self.daq_ent = Entry(master=self.daq_frm)

        self.daq_lbl.pack(side=LEFT, padx=5)
        self.daq_ent.pack(side=LEFT, padx=5)
        self.daq_frm.pack(side=TOP)

        self.trig1_frm = Frame(master = self.engine_frm, padx=10, pady=10)
        self.trig1_lbl = Label(master=self.trig1_frm, text = "Trigger Chip 1 ID")
        self.trig1_ent = Entry(master=self.trig1_frm)

        self.trig1_lbl.pack(side=LEFT, padx=5)
        self.trig1_ent.pack(side=LEFT, padx=5)
        self.trig1_frm.pack(side=TOP)
        
        self.trig2_frm = Frame(master = self.engine_frm, padx=10, pady=10)
        self.trig2_lbl = Label(master=self.trig2_frm, text = "Trigger Chip 2 ID")
        self.trig2_ent = Entry(master=self.trig2_frm)

        self.trig2_lbl.pack(side=LEFT, padx=5)
        self.trig2_ent.pack(side=LEFT, padx=5)
        self.trig2_frm.pack(side=TOP)
        
        self.general_frm.pack(side=TOP, padx = 20)
        #self.engine_frm.pack(side=LEFT, padx = 20)
        
        self.comments_frm = Frame(master = self.master, padx = 50, pady = 10, relief=RAISED, borderwidth=5)
        self.comments_lbl = Label(master = self.comments_frm, text = "Comments", font=("Arial Bold", 20))
        self.comments_txt = Text(master = self.comments_frm, height = 3, width = 50)

        self.comments_lbl.pack(side = TOP)
        self.comments_txt.pack(side = LEFT)

        self.main_info_frm.pack(side=TOP, expand=True, fill=X)
        self.comments_frm.pack(pady = 20, padx = 20)

        self.submit_btn = Button(text="Submit", command=self.submit_info)
        self.submit_btn.pack(pady=10, padx=10)
        
        barcode = None

        while not barcode:
            barcode = read_barcode()

        self.serial_num_ent.insert(0, barcode)

    def submit_info(self):
        info = {"serial_num": None, "board_id": None, "location": None, "daq_chip_id": 0, "trigger_chip_1_id": 0, "trigger_chip_2_id": 0, "comments": None}
        
        info["serial_num"] = self.serial_num_ent.get()
        info["location"] = self.location_ent.get()

        if self.daq_ent.get():
            info["daq_chip_id"] = self.daq_ent.get()
        else:
            info["daq_chip_id"] = 0
            
        if self.trig1_ent.get():
            info["trigger_chip_1_id"] = self.trig1_ent.get()
        else:
            info["trigger_chip_1_id"] = 0
            
        if self.trig2_ent.get():
            info["trigger_chip_2_id"] = self.trig2_ent.get()
        else:
            info["trigger_chip_2_id"] = 0

        info["comments"] = self.comments_txt.get("1.0", END)

        add_board_info(info)

    def createGeneralTestWidgets(self):
        self.clearWindow()
        
        lbl_new = "Run Wagon Test"
        self.createTopBar(lbl_new)

        self.back = Button(master=self.frm_tb, text = "Back", command = self.on_back )
        self.back.pack(side=LEFT, padx=10)
        
        self.frm_tb.pack(side=TOP)
        
        self.main_info_frm = Frame(master=self.master, width = 1200, height = 1000, padx = 20, pady=20)

        self.general_frm = Frame(master = self.main_info_frm, width = 500, height = 200, relief=RAISED, borderwidth=5)

        self.general_lbl = Label(master = self.general_frm, text="General Info", font = ("Arial Bold", 20))
        self.general_lbl.pack(side=TOP, pady = 10)

        self.serial_num_frm = Frame(master = self.general_frm, padx=10, pady=10)
        self.serial_num_lbl = Label(master=self.serial_num_frm, text = "Serial Number (or scan barcode)")
        self.serial_num_ent = Entry(master=self.serial_num_frm)

        self.serial_num_lbl.pack(side=LEFT, padx=5)
        self.serial_num_ent.pack(side=LEFT, padx=5)
        self.serial_num_frm.pack(side=TOP)

        self.tester_frm = Frame(master = self.general_frm, padx=10, pady=10)
        self.tester_lbl = Label(master=self.tester_frm, text = "Tester")
        self.tester_ent = Entry(master=self.tester_frm)

        self.tester_lbl.pack(side=LEFT, padx=5)
        self.tester_ent.pack(side=LEFT, padx=5)
        self.tester_frm.pack(side=TOP)

        self.test_frm = Frame(master = self.main_info_frm, width=500, height = 400, relief=RAISED, borderwidth = 5 )
        
        self.test_lbl = Label(master = self.test_frm, text="Test", font = ("Arial Bold", 20))
        self.test_lbl.pack(side=TOP, pady = 10)

        self.test_name = StringVar(master = self)

        self.test_menu_name = Label(master = self.test_frm, text="Test Name: ")
        self.test_menu_name.pack(side = LEFT, pady=10, padx = 5)

        self.tests = get_test_list()
        self.test_names = [x[0] for x in self.tests]
        self.test_types = [x[1] for x in self.tests]

        self.test_menu = ttk.Combobox(master = self.test_frm, textvariable = self.test_name, values = self.test_names)
        self.test_menu.pack(side = LEFT, pady = 10, padx = 5)

        #self.t1 = BooleanVar()

        self.check_frm = Frame(master = self.test_frm)
        #self.test1_chk = Checkbutton(master = self.check_frm, variable = self.t1, text="Successful?")
        #self.test1_chk.pack(side=LEFT, padx=10, pady=10)

        self.check_frm.pack()
        
        self.general_frm.pack(side=LEFT, padx = 20)
        self.test_frm.pack(side=LEFT, padx = 20, expand = True)
        
        self.main_info_frm.pack(side=TOP, expand=True, fill=X)
        '''self.comments_frm = Frame(master = self.master, padx = 50, pady = 10, relief=RAISED, borderwidth=5)
        self.comments_lbl = Label(master = self.comments_frm, text = "Comments", font=("Arial Bold", 20))
        self.comments_txt = Text(master = self.comments_frm, height = 3, width = 50)

        self.comments_lbl.pack(side = TOP)
        self.comments_txt.pack(side = LEFT)

        self.comments_frm.pack(pady = 20, padx = 20)

        self.attach = None

        self.attach_frm = Frame(master = self.master, padx = 50, pady = 10, relief=RAISED, borderwidth=5)
        self.attach_desc_txt = Text(master = self.attach_frm, height = 1, width = 50)
        self.attach_desc_txt.insert("1.0", "Attachment Description")
        self.attach_com_txt = Text(master = self.attach_frm, height = 3, width = 50) 
        self.attach_com_txt.insert("1.0", "Attachment Comments")
        self.attach_lbl = Label(master = self.attach_frm, text = "Attachemnt", font=("Arial Bold", 20))
        
        self.attach_lbl.pack(pady = 10, padx = 10)
        self.attach_desc_txt.pack(pady = 10, padx = 10)
        self.attach_com_txt.pack(pady = 10, padx = 10)

        self.attach_btn_lbl = Label(master = self.attach_frm, text = "")
        self.attach_btn_lbl.pack(side = LEFT, padx = 10, pady = 10)
        self.attach_btn = Button(master = self.attach_frm, text="Add Attachment", command=self.open_file)
        self.attach_btn.pack(pady=10, padx=10)

        self.attach_frm.pack(side = TOP, padx = 10, pady = 10)
        '''
        self.submit_btn = Button(text="Run Test", command=self.submit_test)
        self.submit_btn.pack(expand = True, padx = 10, pady = 10)

        self.update()

        barcode = None

        while not (self.serial_num_ent.get() or barcode):
            barcode = read_barcode()

        self.serial_num_ent.insert(0, barcode)

    def submit_test(self):
        info = {"serial_number": None, "board_id": None, "person_id": None, "test_type": None, "sucess": 0, "comments": None, "attachdesc1": None, "attachcomment1": None}

        files = {"attach1": None}

        info["serial_number"] = self.serial_num_ent.get()
        person_id = verify_person(self.tester_ent.get())

        if person_id:
            info["person_id"] = person_id
        else:
            info["person_id"] = 0
        info["success"] = 1 if self.t1.get() else 0
        info["test_type"] = self.test_types[self.test_names.index(self.test_name.get())]
        info["comments"] = self.comments_txt.get("1.0", END)

        if self.attach:
            files["attach1"] = open(self.attach,'rb')
            info["attachdesc1"] = self.attach_desc_txt.get("1.0", END)
            info["attachcomment1"] = self.attach_com_txt.get("1.0", END)

        print(info)
        print(files)

        add_general_test(info, files)

    def createInitialTestWidgets(self):
        self.clearWindow()
        
        lbl_new = "Add Initial Board Test"
        self.createTopBar(lbl_new)

        self.back = Button(master=self.frm_tb, text = "Back", command = self.on_back )
        self.back.pack(side=LEFT, padx=10)
        
        self.frm_tb.pack(side=TOP)
        
        self.main_info_frm = Frame(master=self.master, width = 1200, height = 1000, padx = 20, pady=20)

        self.general_frm = Frame(master = self.main_info_frm, width = 500, height = 200, relief=RAISED, borderwidth=5)

        self.general_lbl = Label(master = self.general_frm, text="General Info", font = ("Arial Bold", 20))
        self.general_lbl.pack(side=TOP, pady = 10)

        self.serial_num_frm = Frame(master = self.general_frm, padx=10, pady=10)
        self.serial_num_lbl = Label(master=self.serial_num_frm, text = "Serial Number (or scan barcode)")
        self.serial_num_ent = Entry(master=self.serial_num_frm)

        self.serial_num_lbl.pack(side=LEFT, padx=5)
        self.serial_num_ent.pack(side=LEFT, padx=5)
        self.serial_num_frm.pack(side=TOP)

        self.tester_frm = Frame(master = self.general_frm, padx=10, pady=10)
        self.tester_lbl = Label(master=self.tester_frm, text = "Tester")
        self.tester_ent = Entry(master=self.tester_frm)

        self.tester_lbl.pack(side=LEFT, padx=5)
        self.tester_ent.pack(side=LEFT, padx=5)
        self.tester_frm.pack(side=TOP)

        self.test_frm = Frame(master = self.main_info_frm, width=500, height = 400, relief=RAISED, borderwidth = 5 )
        
        self.test_lbl = Label(master = self.test_frm, text="Initial Tests", font = ("Arial Bold", 20))
        self.test_lbl.pack(side=TOP, pady = 10)

        self.t1 = BooleanVar()
        self.t2 = BooleanVar()
        self.t3 = BooleanVar()
        self.t4 = BooleanVar()

        self.check_frm = Frame(master = self.test_frm)
        self.test1_chk = Checkbutton(master = self.check_frm, variable = self.t1, text="Label Applied")
        self.test1_chk.grid(row = 0, column=0, sticky=W, padx=10, pady=10)
        self.test2_chk = Checkbutton(master = self.check_frm, variable = self.t2, text="Database Entry")
        self.test2_chk.grid(row = 0, column=1, sticky=W, padx=10, pady=10)
        self.test3_chk = Checkbutton(master = self.check_frm, variable = self.t3, text="Label Legibility")
        self.test3_chk.grid(row = 1, column=0, sticky=W, padx=10, pady=10)
        self.test4_chk = Checkbutton(master = self.check_frm, variable = self.t4, text="Power Cycle")
        self.test4_chk.grid(row = 1, column=1, sticky=W, padx=10, pady=10)

        self.check_frm.pack()

        self.general_frm.pack(side=LEFT, padx = 20)
        self.test_frm.pack(side=LEFT, padx = 20)
        
        self.comments_frm = Frame(master = self.master, padx = 50, pady = 10, relief=RAISED, borderwidth=5)
        self.comments_lbl = Label(master = self.comments_frm, text = "Comments", font=("Arial Bold", 20))
        self.comments_txt = Text(master = self.comments_frm, height = 3, width = 50)

        self.comments_lbl.pack(side = TOP)
        self.comments_txt.pack(side = LEFT)

        self.main_info_frm.pack(side=TOP, expand=True, fill=X)
        self.comments_frm.pack(pady = 20, padx = 20)

        self.attach_btn = Button(text="Add Attachment", command=lambda:askopenfilename(title="Select test attachment"))
        self.attach_btn.pack(pady=10, padx=10)

        self.submit_btn = Button(text="Submit", command=self.submit_tests)
        self.submit_btn.pack(pady=10, padx=10)

        self.update()

        barcode = None

        while not (self.serial_num_ent.get() or barcode):
            barcode = read_barcode()

        self.serial_num_ent.insert(0, barcode)
    
    def submit_tests(self):
        info = {"serial_num": None, "board_id": None, "tester": None, "label_applied": 0, "database_entry": 0, "label_legibility": 0, "power_cycle": 0, "comments": None}

        info["serial_num"] = self.serial_num_ent.get()
        info["tester"] = self.tester_ent.get()
        info["label_applied"] = 1 if self.t1.get() else 0
        info["database_entry"] = 1 if self.t2.get() else 0
        info["label_legibility"] = 1 if self.t3.get() else 0
        info["power_cycle"] = 1 if self.t4.get() else 0
        info["comments"] = self.comments_txt.get("1.0", END)
        
        add_initial_tests(info)

root = Tk()
#root.geometry('1000x500')
app = TestEntryGUI(master=root)
app.master.title("Initial Board Entry Tests")
app.mainloop()
