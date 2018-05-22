#This is a class that depicts the runway. It allows for later expansion, hopefully, and also is useful in clearing the runway should the need arise.

#Take off and climb out takes 10 mins, and assume that it is abortable for the first five mins. Assume descent and taxiing takes 12 mins regardless of holding or approaching altitude, and also assume that a go around can be executed upto 9 mins.
#Incoming planes which cannot enter the queue are diverted, except for critical cases. In such a scenario, the plane with the most amount of fuel in the holding queue is diverted.

# from Controller import Controller
from planes import Planes
from threading import *
import threading
import time
import datetime

class Runway(threading.Thread):
    #isFree=None

    def timestamp(self):
        print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

    # def run(self):
    #     pass

    def __init__(self):
        threading.Thread.__init__(self)
        self.lock = threading.Lock()

    def clearRunway(self):
        self.lock.release()
        print("Runway cleared\n")
        self.timestamp()
        # self.lock.notify()

    def landingComplete(self, plane):
        self.lock.acquire()
        # landingClear = Timer(6, self.clearRunway)
        # landingClear.start()
        time.sleep(6)
        print("Plane %s has successfully landed\n" %plane.name)
        self.timestamp()
        self.clearRunway()

    def takeOffComplete(self, plane):
        # The runway is locked so no other threads can interfere with the operation
        self.lock.acquire()
        # takeoffClear = Timer(10, self.clearRunway)
        # takeoffClear.start()
        time.sleep(10)
        print("Plane %s has successfully taken off\n" %plane.name)
        self.timestamp()
        self.clearRunway()
