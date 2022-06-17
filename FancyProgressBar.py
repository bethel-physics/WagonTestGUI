#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# restrict to Python3.5 or higher because of asyncio syntax

# based on <https://stackoverflow.com/a/47920128/4865723>

from tkinter import *
import asyncio
import threading
import random


class AsyncioThread(threading.Thread):
    def __init__(self, asyncio_loop, theWindow):
        self.asyncio_loop = asyncio_loop
        self.theWindow = theWindow
        self.maxData = len(theWindow.varData)
        threading.Thread.__init__(self)


    def run(self):
        self.asyncio_loop.run_until_complete(self.do_data())


    async def do_data(self):
        """ Creating and starting 'maxData' asyncio-tasks. """
        tasks = [
            self.create_dummy_data(number)
            for number in range(self.maxData)
        ]
        completed, pending = await asyncio.wait(tasks)
        results = [task.result() for task in completed]
        print('\n'.join(results))


    async def create_dummy_data(self, number):
        """ One task. """
        sec = random.randint(1, 3)
        data = '{}:{}'.format(number, random.random())
        await asyncio.sleep(sec)

        # IS THIS SAVE?
        self.theWindow.varData[number].set(data)
        print('Thread-ID: {}\tsec: {}\n\t{}' \
               .format(threading.get_ident(), sec, data))

        return data


class TheWindow:
    def __init__(self, maxData):
        # asyncio loop will run in an extra Thread
        self.asyncio_loop = asyncio.get_event_loop()

        # the GUI main object
        self.root = Tk()

        # create the data variable
        self.varData = []
        for i in range(maxData):
            self.varData.append(StringVar())
            self.varData[i].set('<default>')

        # Button to start the asyncio tasks
        Button(master=self.root,
               text='Start Asyncio Tasks',
               command=lambda:self.do_asyncio()).pack()
        # Frames to display data from the asyncio tasks
        for i in range(maxData):
            Label(master=self.root, textvariable=self.varData[i]).pack()
        # Button to check if the GUI is freezed
        Button(master=self.root,
               text='Freezed???',
               command=self.do_freezed).pack()

    def do_freezed(self):
        """ Button-Event-Handler to see if a button on GUI works.
            The GOAL of this example is to make this button clickable
            while the other thread/asyncio-tasks are working. """
        print('Tkinter is reacting. Thread-ID: {}'
              .format(threading.get_ident()))


    def do_asyncio(self):
        """ Button-Event-Handler starting the asyncio part in a separate thread. """
        thread = AsyncioThread(self.asyncio_loop, self)
        thread.start()


if __name__ == '__main__':
    window = TheWindow(11)
    window.root.mainloop()