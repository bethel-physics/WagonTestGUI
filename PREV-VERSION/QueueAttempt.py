#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# based on <https://stackoverflow.com/a/47920128/4865723>

from tkinter import *
import asyncio
import threading
import random
import queue


# Fancy child of a thread that can send data to and from the tkinter stuff
# Code works
# Must be commented and reformatted to work within our program
class AsyncioThread(threading.Thread):
    
    # Constructor
    # Parameters: the queue that is storing the "updates", the maximum amount of data that can go in
    def __init__(self, the_queue, max_data):
        
        # SPECIAL
        # asyncio.get_event_loop() is a special object from the asyncio import
        self.asyncio_loop = asyncio.get_event_loop()
        
        # Initializes the class attributes
        self.the_queue = the_queue
        self.max_data = max_data

        # Calls the thread (parent class) constructor
        threading.Thread.__init__(self)


    # Method that is called when the thread is started
    # Ran on the command "thread.start()"
    def run(self):

        # run_until_complete is a method for "asyncio.get_event_loop()" objects
        self.asyncio_loop.run_until_complete(self.do_data())


    # This is an "async def" function 
        # I don't know why it's special, but it is
    async def do_data(self):
        """ Creating and starting 'maxData' asyncio-tasks. """

        # List of tasks that should be completed
        tasks = [
            self.create_dummy_data(key)
            for key in range(self.max_data)
        ]


        # Wait until this is done
        # I don't really know what this does
        await asyncio.wait(tasks)



    # Creates the random numbers that are shown as "data"
    # Randomly does tasks 
    async def create_dummy_data(self, key):
        """ Create data and store it in the queue. """
        
        
        sec = random.randint(1, 10)
        data = '{}:{}'.format(key, random.random())
        await asyncio.sleep(sec)

        self.the_queue.put((key, data))



# Class that handles all of the tkinter stuff
# Creates an AsyncioThread within
class TheWindow:

    # Constructor
    def __init__(self, max_data):
        # thread-safe data storage
        self.the_queue = queue.Queue()

        # the GUI main object
        self.root = Tk()

        # create the data variable
        self.data = []
        for key in range(max_data):
            self.data.append(StringVar())
            self.data[key].set('<default>')

        # Button to start the asyncio tasks
        Button(master=self.root,
               text='Start Asyncio Tasks',
               command=lambda: self.do_asyncio()).pack()
        
        # Frames to display data from the asyncio tasks
        for key in range(max_data):
            Label(master=self.root, textvariable=self.data[key]).pack()
        
        # Button to check if the GUI is freezed
        Button(master=self.root,
               text='Freezed???',
               command=self.do_freezed).pack()


    # Recursive Method
    # Refreshes the data that will be put on the tkinter window
    def refresh_data(self):
        """
        """
        # do nothing if the aysyncio thread is dead
        # and no more data in the queue
        # Breaking statement of recursive loop
        if not self.thread.is_alive() and self.the_queue.empty():
            return

        # refresh the GUI with new data from the queue
        while not self.the_queue.empty():
            key, data = self.the_queue.get()
            self.data[key].set(data)

        print('RefreshData...')

        #  timer to refresh the gui with data from the asyncio thread
        self.root.after(1000, self.refresh_data)  # called only once!


    # What the "Freeze???" button does when clicked
    # Demonstrates that the GUI Window isn't frozen while the other data is parsed in
    def do_freezed(self):
        """ Button-Event-Handler to see if a button on GUI works.
            The GOAL of this example is to make this button clickable
            while the other thread/asyncio-tasks are working. """
        print('Tkinter is reacting. Thread-ID: {}'
              .format(threading.get_ident()))


    # Method that is run when the button is clicked
    def do_asyncio(self):
        """
            Button-Event-Handler starting the asyncio part in a separate
            thread.
        """
        # create fancy thread object
        # Parameters: the queue that is storing the "updates", the maximum amount of data that can go in
        self.thread = AsyncioThread(self.the_queue, len(self.data))

        #  timer to refresh the gui with data from the asyncio thread
        self.root.after(1000, self.refresh_data)  # called only once!

        # start the thread
        self.thread.start()


# Main Method
# What logic is run when this file is ran from the terminal
if __name__ == '__main__':

    # Creates the window
    # Parameter: number of labels to be filled with data
    window = TheWindow(10)

    # mainloop()
    window.root.mainloop()