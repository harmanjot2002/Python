"""
Python list comprehension provides a much more short syntax for creating a new list based on values of an existing list.
It is similar to for loops,diffrence is their performance.
Advantages of List Comprehension:
    -More time-efficient and space-efficient than loops.
    -Require fewer lines of code.
    -Transforms iterative statement into a formula.
"""

List=[character for character in [1,2,3]]
print(List)

list=[i for i in range(11) if i%2==0]
print(list)

matrix=[[j for j in range(3)] for i in range(3)]
print(matrix)

List=[]
for character in 'Welcome To Advanced Python Programming':
    List.append(character)
print(List)

"""
In the context of data storage,serialization is the process of translating data strutures or object state into a format that can be stored(e.g.in a memory buffer)or transmitted and reconstructed later.

In serialization,an object is transforemd into a format that can be stored,so as to be able to deserialize it later and recreate the original object from the serialized format.

Pickling is the process whereby a Python object heirarchy is converted into a byte stream(usually not a human readable)to be written to a file,this is also known as Serialization.

Unpicking is the reverse opearation,whereby a byte stream is converted back into a working Python object heirarchy.

Pickle is operationally simplest way to store the object.

Python Pickle module is an object-oriented way to store objects directly in a special storage format.

WHAT PICKLE CAN DO?
Pickle can store and reproduce dictionaries and lists very easily.
Stores object attributes and restores them back to same state.

WHAT PICKLE CAN'T DO?
It doesnot save an object's code.Only its attributes values.
It cannot store file handles or connection sockets/

The pickle interface provides four different methods:
1.dump():It serializes to an open file(file-like object)
2.dumps():Serializes to a string
3.load():Deserializes from an open-like object
4.loads():Deserializes from a string
"""
import pickle
class Animal:
    def __init__(self,number_of_legs,color):
        self.number_of_legs=number_of_legs
        self.color=color
        
class Cat(Animal):
    def __init__(self,color):
        Animal.__init__(self,4,color)

pussy=Cat("White")
print(str.format("My cat pussy is {0} and has {1} legs",pussy.color,pussy.number_of_legs))

pickled_pussy=pickle.dumps(pussy)
print("Would you like to see her pickled?Here she is?")
print(pickled_pussy)
"""
JSON:
JSON(JavaScript Object Notation) has been part of the Python standard library is a lightweight data-interchange format.
It is easy for humans to read and write.It is easy to parse and generate.
Because of its simplicity,JSON is a way by which we store and exchange data,which is accomplished through its JSON syntax,and is used in many web applications.
As it is in human readabe format,and this may be one of the reasons for using it in data transmission,in addition to its effectiveness when working with APIs.

JSON TO PYTHON:
    -Reading JSON means converting JSON into a Python value(object).
    -JSON library parses JSON into a dictionary or list in Python.
    -In order to do that,we use the loads() function (load from a string):
"""

import json
jsonData='{"EmployeeID":402040,"EmployeeName":"Zack","Department":"Financial Services"}'
jsonToPython=json.loads(jsonData)
print(jsonToPython)

