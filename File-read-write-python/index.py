
# read
f = open('/home/siddharthasodariya/python/Small-task/File-read-write-python/text.txt')
print(f)            #<_io.TextIOWrapper name='/home/siddharthasodariya/python/Small-task/File-read-write-python/text.txt' mode='r' encoding='UTF-8'>
print(f.read())     #print alll
print(f.mode)       #show permission mode r w a
print(f.tell())     #135
print(f.seek(10))   #10
print(f.tell())     #10

f.close()       #prevent leak

print(f)        #<_io.TextIOWrapper name='/home/siddharthasodariya/python/Small-task/File-read-write-python/text.txt' mode='r' encoding='UTF-8'>  
# print(f.read()) #I/O operation on closed file.



""" 
with open('/home/siddharthasodariya/python/Small-task/File-read-write-python/text.txt', 'r') as rf:
    pass
print(rf.read())    #error """


with open('/home/siddharthasodariya/python/Small-task/File-read-write-python/text.txt', 'r') as rf:

    # print(rf.readlines)     #<built-in method readlines of _io.TextIOWrapper object at 0x7f98145311e0>
    
    print(rf.readlines())
    # ['This is the test file\n', 'Multiple lines\n', 'first line\n', 'second line\n', 'third line\n', 'four line\n', 'fifth line\n', 'six line\n', 
    # 'seven line\n', 'eighth line\n', 'ninth line ']
    
    print("-----------------------------")
    
    rf.seek(0)                      #otherwise below line print blank line
    print(rf.readline(), end=" ")   #if not end then \n + print's new line =one blank line

    rf.seek(0)
    for i in rf:
        print(i,end=" ")

    rf.seek(0)
    rf.read(100)        #print only 100 character 


""" with open('/home/siddharthasodariya/python/Small-task/File-read-write-python/text.txt', 'r') as rf:
    print(rf.write("Hello"))        #Exception has occurred: UnsupportedOperation  not writable """



#if put 'rw' then :ValueError must have exactly one of create/read/write/append mode
with open('/home/siddharthasodariya/python/Small-task/File-read-write-python/text.txt', 'w') as wf:
    print(wf.write("Hello"))    #5 number of char
    # print(wf.read())            #not readable

    wf.seek(0)
    print(wf.write("F"))        #1
    with open('/home/siddharthasodariya/python/Small-task/File-read-write-python/text.txt', 'r') as rf:
        print(rf.read())
    #print Hello because of change don't happen untill close the ..

with open('/home/siddharthasodariya/python/Small-task/File-read-write-python/text.txt', 'r') as rf:
        print(rf.read())
        #print Fello

# append
with open('/home/siddharthasodariya/python/Small-task/File-read-write-python/text.txt', 'a') as wf:
    print(wf.write("'This is the test file\n', 'Multiple lines\n', 'first line\n', 'second line\n', 'third line\n', 'four line\n', 'fifth line\n', 'six line\n', 'seven line\n', 'eighth line\n', 'ninth line '"))    #5 number of char
with open('/home/siddharthasodariya/python/Small-task/File-read-write-python/text.txt', 'r') as rf:
    print(rf.read())


#for image we do binary rb, wb, ab

""" This is the test file
Multiple lines
first line
second line
third line
four line
fifth line
six line
seven line
eighth line
ninth line  """