from math import sqrt


class Vector3:
    def __init__(self,x,y,z):
        self._data = [x,y,z]
    def __str__(self):
        return f"<{self._data[0]},{self._data[1]},{self._data[2]}>"
    def __add__(self, other): #other may be a vector3 or a single number
        if type(other) is Vector3:
            to_return = Vector3(self._data[0]+other._data[0],
                                self._data[1]+other._data[1],
                                self._data[2]+other._data[2])
        else:
            to_return = Vector3(self._data[0]+other,
                                self._data[1]+other,
                                self._data[2]+other)
        return to_return
    def add(self,other):
        to_return = Vector3(self._data[0]+other._data[0],
                            self._data[1]+other._data[1],
                            self._data[2]+other._data[2])
        return to_return
    def __getitem__(self,location):
        return self._data[location]
    def __len__(self):
        return len(self._data)
    def length(self):
        return sqrt(self._data[0]**2+self._data[1]**2+self._data[2]**2)
    def scale(self,scalar):
        self._data = [x*scalar for x in self._data]
        # for i in range(len(self._data)):
        #     self._data[i] *= scalar

        return self
    def dot(self,other):
        toReturn = 0
        for i in range(len(self._data)):
            toReturn += self._data[i]+other._data[i]
        return toReturn