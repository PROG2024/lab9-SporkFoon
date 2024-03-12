"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""

class Counter:

    def __init__(self):
        self.__count = 0


    def __str__(self):
        return f"{self.__count}"

    #TODO write count property
    #TODO write increment method
