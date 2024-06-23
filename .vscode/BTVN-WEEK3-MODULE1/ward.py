# -*- coding: utf-8 -*-
"""Ward.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eiIrHI2zadpHzcfTdfdTnAjwZbq_945c
"""

class Student():
  def __init__(self, name, yob, grade):
    self.name = name
    self.yob = int(yob)
    self.grade = grade
  def describe(self):
    print(f'Student - Name: {self.name}, Year of birth: {self.yob}, Grade: {self.grade}')
class Teacher():
  def __init__(self, name, yob, subject):
    self.name = name
    self.yob =int(yob)
    self.subject = subject
  def describe(self):
    print(f'Teacher - Name: {self.name}, Year of birth: {self.yob}, Subject: {self.subject}')
class Doctor():
  def __init__(self, name, yob, specialty):
    self.name = name
    self.yob =int(yob)
    self.specialty = specialty
  def describe(self):
    print(f'Doctor - Name: {self.name}, Year of birth: {self.yob},Specialty: {self.specialty}')
class Ward:
  def __init__(self, name):
    self.name = name
    self.person = []
  def add_person(self, person):
    self.person.append(person)
  def remove_person(self, person):
    self.person.remove(person)
  def describe(self):
    print(f'Ward: {self.name}')
    for person in self.person:
      person.describe()
  def count(self):
    count = 0
    for person in self.person:
      if isinstance(person,Doctor):
        count += 1
    return count
  def sort(self):
    self.person.sort(key = lambda x: x.yob , reverse = True)
  def compute_average(self):
    total = 0
    count = 0
    for person in self.person:
      if isinstance(person,Teacher):
        total += person.yob
        count += 1
    return total/count



