# -*- coding: utf-8 -*-
class MyQueue:
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
  def enqueue(self, number):
    for i in range(len(self.capacity)):
      if self.capacity[i]== ' ':
        self.capacity[i] = number
        break
  def dequeue(self):
    for i in range(len(self.capacity)):
      if self.capacity[i] != ' ':
        self.capacity[i] = ' '
        return self.capacity[i]
  def font(self):
    for i in range(len(self.capacity)):
      if self.capacity[i] != ' ':
        return self.capacity[i]
        break