# python debugger: instead of print line every where
"""set break points in the code where you can:
        -examine variables
        -step forward line-by-line
        -show code as it executes

debugger at command line
n: execute next line
c: complete execution
l: list 3 line before and after current line
s: step into function call
b: show all list of breakpoints
b[int]: set break point at line number(eg b10)
v[fun]: break at function name
cl: clear all break point
cl[int]: clear break point at line number(eg cl10)
p: print
"""

#pylint: disable=trailing-whitespace

import pdb

def printer_one( arg ):
    """pdb-Pylint.py:22:0: C0116: Missing function or 
    method docstring (missing-function-docstring)"""
    return print (arg)

def printer_two( arg ):
    """pdb-Pylint.py:22:0: C0116: Missing function or 
    method docstring (missing-function-docstring)"""
    print(arg)

#pylint: disable=forgotten-debug-statement
pdb.set_trace()

print(printer_one("FDfd"))
A=454

breakpoint()

A += 4

printer_two("ffffff")

A += 10

#pylint: disable= pointless-string-statement

""" siddharthasodariya@sf-cpu-213:~/python/Small-task$ python3 pdb-Pylint.py
> /home/siddharthasodariya/python/Small-task/pdb-Pylint.py(30)<module>()
-> print(printer_one("FDfd"))
(Pdb) l
 25  	def printer_two( arg ):
 26  	    print(arg)
 27  	
 28  	pdb.set_trace()
 29  	
 30  ->	print(printer_one("FDfd"))
 31  	a=454
 32  	
 33  	breakpoint()
 34  	
 35  	a += 4
(Pdb) n
FDfd
None
> /home/siddharthasodariya/python/Small-task/pdb-Pylint.py(31)<module>()
-> a=454
(Pdb) n
> /home/siddharthasodariya/python/Small-task/pdb-Pylint.py(33)<module>()
-> breakpoint()
(Pdb) a
(Pdb) p(a)
454
(Pdb) b
(Pdb) b 35
Breakpoint 1 at /home/siddharthasodariya/python/Small-task/pdb-Pylint.py:35
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at /home/siddharthasodariya/python/Small-task/pdb-Pylint.py:35
(Pdb) b printter_two
*** The specified object 'printter_two' is not a function or was not found along sys.path.
(Pdb) b printer_two
Breakpoint 2 at /home/siddharthasodariya/python/Small-task/pdb-Pylint.py:25
(Pdb) b
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at /home/siddharthasodariya/python/Small-task/pdb-Pylint.py:35
2   breakpoint   keep yes   at /home/siddharthasodariya/python/Small-task/pdb-Pylint.py:25
(Pdb) s
--Call--
> /usr/lib/python3.8/pdb.py(1609)set_trace()
-> def set_trace(*, header=None):
(Pdb) cl
Clear all breaks? y
Deleted breakpoint 1 at /home/siddharthasodariya/python/Small-task/pdb-Pylint.py:35
Deleted breakpoint 2 at /home/siddharthasodariya/python/Small-task/pdb-Pylint.py:25
(Pdb) n
> /usr/lib/python3.8/pdb.py(1610)set_trace()
-> pdb = Pdb()
(Pdb) n
> /usr/lib/python3.8/pdb.py(1611)set_trace()
-> if header is not None:
(Pdb) c
> /home/siddharthasodariya/python/Small-task/pdb-Pylint.py(35)<module>()
-> a += 4
(Pdb) """



#pylint: disable=line-too-long

"""Pylint

pip install pylint
pylint pdb-Pylint.py

siddharthasodariya@sf-cpu-213:~/python/Small-task$ pylint pdb-Pylint.py
************* Module pdb-Pylint
pdb-Pylint.py:46:3: C0303: Trailing whitespace (trailing-whitespace)
pdb-Pylint.py:48:3: C0303: Trailing whitespace (trailing-whitespace)
pdb-Pylint.py:51:3: C0303: Trailing whitespace (trailing-whitespace)
pdb-Pylint.py:53:3: C0303: Trailing whitespace (trailing-whitespace)
pdb-Pylint.py:99:0: C0305: Trailing newlines (trailing-newlines)
pdb-Pylint.py:1:0: C0103: Module name "pdb-Pylint" doesn't conform to snake_case naming style (invalid-name)
pdb-Pylint.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
pdb-Pylint.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
pdb-Pylint.py:28:0: W1515: Leaving functions creating breakpoints in production code is not recommended (forgotten-debug-statement)
pdb-Pylint.py:31:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
pdb-Pylint.py:33:0: W1515: Leaving functions creating breakpoints in production code is not recommended (forgotten-debug-statement)
pdb-Pylint.py:40:0: W0105: String statement has no effect (pointless-string-statement)

-----------------------------------
Your code has been rated at 0.77/10

siddharthasodariya@sf-cpu-213:~/python/Small-task$ pylint pdb-Pylint.py
************* Module pdb-Pylint
pdb-Pylint.py:1:0: C0103: Module name "pdb-Pylint" doesn't conform to snake_case naming style (invalid-name)
pdb-Pylint.py:34:0: W1515: Leaving functions creating breakpoints in production code is not recommended (forgotten-debug-statement)
pdb-Pylint.py:37:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
pdb-Pylint.py:39:0: W1515: Leaving functions creating breakpoints in production code is not recommended (forgotten-debug-statement)
pdb-Pylint.py:48:0: W0105: String statement has no effect (pointless-string-statement)
pdb-Pylint.py:111:0: W0105: String statement has no effect (pointless-string-statement)

------------------------------------------------------------------
Your code has been rated at 5.71/10 (previous run: 4.29/10, +1.43)

siddharthasodariya@sf-cpu-213:~/python/Small-task$ pylint pdb_pylint.py
************* Module pdb_pylint
pdb_pylint.py:34:0: W1515: Leaving functions creating breakpoints in production code is not recommended (forgotten-debug-statement)
pdb_pylint.py:39:0: W1515: Leaving functions creating breakpoints in production code is not recommended (forgotten-debug-statement)

------------------------------------------------------------------
Your code has been rated at 8.57/10 (previous run: 7.86/10, +0.71)

siddharthasodariya@sf-cpu-213:~/python/Small-task$ pylint pdb_pylint.py

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 8.57/10, +1.43)
"""
