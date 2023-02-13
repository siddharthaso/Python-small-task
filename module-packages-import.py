""" here are actually three different ways to define a module in Python:
    A module can be written in Python itself.
    A module can be written in C and loaded dynamically at run-time, like the re (regular expression) module.
    A built-in module is intrinsically contained in the interpreter, like the itertools module.

Python Packages
Suppose you have developed a very large application that includes many modules. As the number of modules grows, it becomes difficult to keep track of them all if they are dumped into one location. This is particularly so if they have similar names or functionality. You might wish for a means of grouping and organizing them.

Packages allow for a hierarchical structuring of the module namespace using dot notation. In the same way that modules help avoid collisions between global variable names, packages help avoid collisions between module names.

Creating a package is quite straightforward, since it makes use of the operating system’s inherent hierarchical file structure. 
if the pkg directory resides in a location where it can be found (in one of the directories contained in sys.path), you can refer to the two modules with dot notation (pkg.mod1, pkg.mod2) and import them with the syntax you are already familiar with:

import <module_name>[, <module_name> ...]
from <module_name> import <name> as <alt_name>
from pkg.mod3 import * """

import datetime
from abc import ABC, abstractmethod
from math import *