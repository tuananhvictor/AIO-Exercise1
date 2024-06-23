# -*- coding: utf-8 -*-
class MyStack:
  def intialization(self, capacity):
    self.capacity = [' ' for i in range(capacity)]
  def is_empty(self):
    for i in self.capacity:
      if i != ' ':
        return False
    return True
  def is_full(self):
    count = 0
    for i in self.capacity:
      if i != ' ':
        count += 1
    if count == len(self.capacity):
      return True
    else:
      return False
  def push(self,number):
    for i in range(len(self.capacity)):
      if self.capacity[i]== ' ':
        self.capacity[i] = number
        break
  def pop(self):
    for i in range(len(self.capacity)-1,-1,-1):
      if self.capacity[i] != ' ':
        self.capacity[i] = ' '
        break
  def top(self):
    for i in range(len(self.capacity) - 1, -1, -1):
      if self.capacity[i] != ' ':
        return self.capacity[i]