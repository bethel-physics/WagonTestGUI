import time
from tkinter import *
import asyncio
import threading
import random
import queue

from TestScriptEx import TestScriptEx


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
        threading.Thread.__init__(self, daemon= True)


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
            self.run_test_script(key)
            for key in range(self.max_data)
        ]


        # Wait until this is done
        # I don't really know what this does
        await asyncio.wait(tasks)



    # Creates the random numbers that are shown as "data"
    # Randomly does tasks 
    async def run_test_script(self, key):
        """ Create data and store it in the queue. """

        test_script_object = TestScriptEx("test1")
        await asyncio.sleep(1)
        test_script_object.run_inc_thread()

        
        while self.is_alive :
            
            time.sleep(0.75)
            
            data = test_script_object.get_current_status()

            self.the_queue.put((key, data))
        