from first import first_function

def second_function():
    print("second function called")

first_function()
second_function()

# siddharthasodariya@sf-cpu-213:~/python/Small-task/Circular import$ python3 first.py
# Traceback (most recent call last):
#   File "first.py", line 1, in <module>
#     from second import second_function
#   File "/home/siddharthasodariya/python/Small-task/Circular import/second.py", line 1, in <module>
#     from first import first_function
#   File "/home/siddharthasodariya/python/Small-task/Circular import/first.py", line 1, in <module>
#     from second import second_function
# ImportError: cannot import name 'second_function' from partially initialized module 'second' (most likely due to a circular import) (/home/siddharthasodariya/python/Small-task/Circular import/second.py)
# siddharthasodariya@sf-cpu-213:~/python/Small-task/Circular import$ python3 run.py
# Traceback (most recent call last):
#   File "run.py", line 1, in <module>
#     import first
#   File "/home/siddharthasodariya/python/Small-task/Circular import/first.py", line 1, in <module>
#     from second import second_function
#   File "/home/siddharthasodariya/python/Small-task/Circular import/second.py", line 1, in <module>
#     from first import first_function
# ImportError: cannot import name 'first_function' from partially initialized module 'first' (most likely due to a circular import) (/home/siddharthasodariya/python/Small-task/Circular import/first.py)