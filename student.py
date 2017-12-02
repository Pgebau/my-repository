from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades= {}

    def add_module(self,title):
        self.modules.append(title.title)
        self.grades[title.title] = title.get_grade()

    def get_list_modules(self):
        for i in self.modules:
            print(i)


    def get_grades(self):
        for k, v in self.grades.items():
            print(k + ": " + str(v))


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
