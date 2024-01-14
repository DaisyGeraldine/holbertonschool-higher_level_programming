# Python - Inheritance

## Resources
**Read or watch:**
- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Multiple inheritance](https://www.python-course.eu/python3_multiple_inheritance.php)
- [Inheritance in Python](https://realpython.com/inheritance-composition-python/)
- [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=3ohzBxoFHAY)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions

## Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Python Test Cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- Do not use the words import or from inside your comments, the checker will think you are trying to import some modules

## Tasks
### 0. Lookup (mandatory)
Write a function that returns the list of available attributes and methods of an object:

### 1. My list (mandatory)
Write a class `MyList` that inherits from list:

### 2. Exact same object (mandatory)
Write a function that returns True if the object is exactly an instance of the specified class; otherwise False.

### 3. Same class or inherit from (mandatory)
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.

### 4. Only sub class of (mandatory)
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.

### 5. Geometry module (mandatory)
Write an empty class `BaseGeometry`.

### 6. Improve Geometry (mandatory)
Write a class `BaseGeometry` (based on 5-base_geometry.py).

### 7. Integer validator (mandatory)
Write a class `BaseGeometry` (based on 6-base_geometry.py).

### 8. Rectangle (mandatory)
Write a class `Rectangle` that inherits from `BaseGeometry` (7-base_geometry.py).

### 9. Full rectangle (mandatory)
Write a class `Rectangle` that inherits from `BaseGeometry` (7-base_geometry.py). (task based on 8-rectangle.py)

### 10. Square #1 (mandatory)
Write a class `Square` that inherits from `Rectangle` (9-rectangle.py):

### 11. Square #2 (mandatory)
Write a class `Square` that inherits from `Rectangle` (9-rectangle.py). (task based on 10-square.py).

### 12. My integer (#advanced)
Write a class `MyInt` that inherits from `int`.

### 13. Can I? (#advanced)
Write a function that adds a new attribute to an object if it’s possible: