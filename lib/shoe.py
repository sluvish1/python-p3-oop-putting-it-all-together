#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,size):
        self.brand = brand
        self._size = size
    
    def get_shoe_size(self):
        return self._size

    def set_shoe_size(self,size):
        if size != int:
            print("size must be an integer")
        else:
            self._size == int
    size = property(get_shoe_size,set_shoe_size)
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")