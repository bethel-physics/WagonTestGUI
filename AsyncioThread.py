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