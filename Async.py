# -------------------------------------------------------------------------------concurrency--------------------------------------------------------------------

import time
""" 
start_time = time.time()
# main()
print("--- %s seconds ---" % (time.time() - start_time)) 
"""

"""Sync: python follow single path of executing top to bottom in single thread
Asnc : change the flow  according to the requirements
"""
# asyncio is a library to write concurrent code using the async/await syntax.
import asyncio
loop = asyncio.get_event_loop()

# @asyncio.coroutine                 
"""DeprecationWarning: "@coroutine" decorator is deprecated since Python 3.8, use "async def" instead
  def tt():
"""

async def tt():
    print("Hello")
    yield asyncio.sleep(1)
    print("world")

print(loop)         #<_UnixSelectorEventLoop running=False closed=False debug=False>
# loop.run_un6til_complete(tt())   #An asyncio.Future, a coroutine or an awaitable is required

print("------------------------------------------------------------------------------------------------------------------------------------")
# There are three main types of awaitable objects: coroutines, Tasks, and Futures.
""" A Future is a special low-level awaitable object that represents an eventual result of an asynchronous operation.
When a Future object is awaited it means that the coroutine will wait until the Future is resolved in some other place.
Future objects in asyncio are needed to allow callback-based code to be used with async/await.
Normally there is no need to create Future objects at the application level code.
Future objects, sometimes exposed by libraries and some asyncio APIs, can be awaited:
async def main():
    await function_that_returns_a_future_object()
    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    ) """

def test():
    print("from test")

async def test1():                          #wrapper around the function and return co-routine to execute await
    print("from test1")

test()      #from test

# test1()     
""" RuntimeWarning: coroutine 'test1' was never awaited
  test1()
RuntimeWarning: Enable tracemalloc to get the object allocation traceback """

print(test1)                #<function test1 at 0x7fc3195cef70>

# print(test1())              
"""
<coroutine object test1 at 0x7fe46ab8fa40>
/home/siddharthasodariya/python/Small-task/Async.py:27: RuntimeWarning: coroutine 'test1' was never awaited
  print(test1())              #RuntimeWarning: coroutine 'test1' was never awaited print(test1())
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
"""

asyncio.run(test1())        #from test1

# asyncio.run(test1)                  #a coroutine was expected, got <function test1 at 0x7fe82c1d9f70>
    # a coroutine function: an async def function;
    # a coroutine object: an object returned by calling a coroutine function.
""" asyncio.run(coro, *, debug=False)
    Execute the coroutine coro and return the result. """

"""from test
<function test1 at 0x7f4e6474ef70>
from test1"""

print("------------------------------------------------------------------------------------------------------------------------------------")

start_time = time.time()

def test0():
    print("from test0")
    # await test1()           #SyntaxError: 'await' outside async function

async def test():
    print("from test")
    await test1()
    print("Finished")

async def test1():
    print("from test1")
    # asyncio.sleep(10)         #RuntimeWarning: coroutine 'sleep' was never awaited  asyncio.sleep(10)
    await asyncio.sleep(1)      #asyncio.sleep(1) return coroutine and await runs it.

# await test1()       #SyntaxError: 'await' out side function
"""bcs of event Loop
The event loop is the core of every asyncio application. Event loops run asynchronous tasks and callbacks, perform network IO operations, and run subprocesses.
Application developers should typically use the high-level asyncio functions, such as asyncio.run(), and should rarely need to reference the loop object or 
call its methods. This section is intended mostly for authors of lower-level code, libraries, and frameworks, who need finer control over the event loop behavior."""
# await can only be called inside the async fun

asyncio.run(test())
asyncio.run(test1())            #test1 return coroutine and asyncio.run() runs it. asyncio create event loop and add coroutine into it.


print("--- %s seconds ---" % (time.time() - start_time))
"""
from test
from test1
Finished
from test1
--- 2.00720477104187 seconds ---"""

print("------------------------------------------------------------------------------------------------------------------------------------")
# using task to run other part while one part is in sleep
start_time = time.time()

async def test():
    print("from test")
    # task = asyncio.create_task(await test1())           #a coroutine was expected, got None

    task = asyncio.create_task(test1())                 
    #tells that i want to run this task but cannot run untill the execution of whatever function or thing it currently doing OR untill whaterver its doing it takes break and stop
    
    # await task                      #wait untill task is done
    """ from test
    from test1
    from test1.1
    Finished
    Finished 2
    --- 3.0081489086151123 seconds --- """

    print("Finished")
    await asyncio.sleep(1)
    print("Finished 2")

async def test1():
    print("from test1")
    await asyncio.sleep(1)
    print("from test1.1")
    await asyncio.sleep(1)  

asyncio.run(test())

print("--- %s seconds ---" % (time.time() - start_time))
"""from test
Finished
from test1
Finished 2
from test1.1
--- 1.005518913269043 seconds ---"""

#reason when task is called then it goes to sleep for 1 sec that's why program switch back and run next line
#whwnever sleep then change the flow.....


print("------------------------------------------------------------------------------------------------------------------------------------")
start_time = time.time()

async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2) 
    print("done fetching")
    return {'data': 1}

async def print_num():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data())       #future value
    task2 = asyncio.create_task(print_num())

    # value = task1
    # print(value)
    """<Task pending name='Task-11' coro=<fetch_data() running at /home/siddharthasodariya/python/Small-task/Async.py:127>>"""
    #at start

    value = await task1                                     #Future in python OR promise in java-script
    print(value)

    task2.cancel()
    await task2

asyncio.run(main())

print("--- %s seconds ---" % (time.time() - start_time))

"""
start fetching
0
1
2
3
4
5
6
7
done fetching
{'data': 1}
8
9
--- 2.511863946914673 seconds ---"""
print("------------------------------------------------------------------------------------------------------------------------------------")

""" async def async_generator():
    for i in range(3):
        await asyncio.sleep(1)
        yield i*i
async def main():
    async for i in async_generator():
        print(i)
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.run_until_complete(loop.shutdown_asyncgens())  # see: https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.shutdown_asyncgens
    loop.close() """

""" async def createGenerator():
    mylist = range(3)
    for i in mylist:
        await asyncio.sleep(1)
        yield i*i
async def start():
    async for i in createGenerator():
        print(i)
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(start())
except KeyboardInterrupt:
    loop.stop()
    pass """

"""
Python code runs at exactly the same speed whether it is written in sync or async style. Aside from the code, there are two factors 
that can influence the performance of a concurrent application: context-switching and scalability.

Keeping all of this in mind, we can say that async could be faster than sync for a given scenario only when:
    There is high load (without high load there is no advantage in having access to high concurrency)
    The tasks are I/O bound (if the tasks are CPU bound, then concurrency above the number of CPUs does not help)
    You look at average number of requests handled per unit of time. If you look at individual request handling times you will
     not see a big difference, and async may even be slightly slower due to having more concurrent tasks competing for the CPU(s).


An async application will only do better than a sync equivalent under high load.
Thanks to greenlets, it is possible to benefit from async even if you write normal code and use traditional frameworks such as Flask or Django.
"""