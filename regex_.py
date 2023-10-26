
# Given an array of ints, return true if the array contains two 7’s next to each other, or there are two 7’s separated by one element.
# Ex1: [1, 7, 7] → true
# Ex2: [1, 7, 1, 7] → true
# Ex3: [1, 7, 1, 1, 7] → false

def check7(l):
    for i in range(len(l)):
        if i <= len(l)- 2 and l[i]==l[i+1]==7:
            return True
        elif i <= len(l) - 3 and l[i]==l[i+2]==7!=l[i+1]:
            return True
    return False

print(check7([1, 7, 7])) 
print(check7([1, 7, 1, 7])) 
print(check7([1, 7, 1, 1, 7])) 
print(check7([7, 7, 1, 1, 7])) 
print(check7([9, 0, 5, 1, 7])) 
print(check7([7, 7, 7, 7, 7]))


# Return the sum of the numbers in the array,a: Return 0 for an empty array.
# b: Number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
# Ex1: [1, 2, 2, 1] → 6
# Ex2: [1, 1] → 2
# # Ex3: [1, 2, 2, 1, 13] → 6
# def sumwithout13(l):
#     sum = 0
#     i = 0
#     if len(l)==0:
#         return 0
#     while i <= len(l):
#         if l[i]==13 and l[i+1]!=13:
#             i +=2
#             continue
#         elif l[i]==13 and l[i+1]!=13:
#                 i+=1
#                 continue
#         else:
#             sum += l[i]
#             i += 1
# print(sumwithout13([13, 2, 5, 8, 13, 4]))
def sum13(n):
    Total=0
    for i in range (len(n)):
        if(n[i]==13 or n[i-1]==13 and i!=0):
            Total=Total 
        else:
            Total=Total+n[i]
    return Total
print(sum13([13, 2, 5, 8, 13, 4]))



#  Given 2 strings, a and b, return a new string made of the first char of a and the last char of b. 
# If either string is length 0, use ‘@’ for its missing char.
# Ex. (“last”, “chars”) → “ls”
# Ex. (“yo”, “java”) → “ya”

def comb(a, b):
    ans = ""
    if len(a)==0:
        ans += "@"
    else:
        ans += a[0]
    if len(b)==0:
        ans += "@"
    else:
        ans += a[0]
    return
# def fristlast(s1,s2):
# if len(s1)>0 and len(s2)>0:
# return s1[0]+s2[-1]
# #elif len(s1<0) or len(s2)<0:
# elif len(s1)>0 and len(s2)<=0:
# return str(s1[0])+'@'
# elif len(s1)<=0 and len(s2)>0:
# return '@'+str(s2[-1])
# elif len(s1)<=0 and len(s2)<=0:
# return '@@'
# print(fristlast('last','chars'))
print(comb('last','chars'))



"""

import re
import uuid

# try:


# [a-zA-Z]+.\d+ 
s = "((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]).){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"
# ((([0-9a-fA-F]){1,4}):){7}([0-9a-fA-F]){1,4}


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.chrome()
driver.maximize_window()
driver.get("www.google.com")
driver.find_element(By.XPATH, "//button[text()='Login']")
driver.get_element_by_id("username").send_keys("bhumi")
driver.get_element_by_id("password").send_keys("abc")
driver.get_element_by_id("login").send_keys(Keys.ENTER)

assert "No results found." not in driver.page_source driver.close()


"""


"""
>>> import re
>>> 
>>> str= " Corona virus disease"
>>> 
>>> MyVar = re.sub("\s", "-", str)
>>> 
>>> print(MyVar)
-Corona-virus-disease
>>> x = re.split('[a-c]', '0a3Bc6')
>>> 
>>> print(x)
['0', '3B', '6']
>>> str = "technpogy is the world"
>>> 
>>> MyVar = re.findall("^tech", str)
>>> bool(MyVar)
True
>>> MyVar
['tech']
>>> str = "i am a techie in python technology"
>>> 
>>> x = re.split("\s", txt, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'txt' is not defined
>>> 
>>> x = re.split("\s", str, 3)
>>> print(x)
['i', 'am', 'a', 'techie in python technology']
>>> #re.purge() is used to 
>>> #Clear the cache
>>> 
>>> re.sub('technology', 'limited', 'wipro technology')
'wipro limited'
>>> str = "now a days techies are available in different technologies"
>>> 
>>> Myvar = re.findall("tech", str)
>>> 
>>> print(Myvar)
['tech', 'tech']
>>> re.search("s", "siddharths")
<re.Match object; span=(0, 1), match='s'>
>>> re.findall("s", "siddharths")
['s', 's']
>>> re.sub("s","f", "siddharths")
'fiddharthf'
>>> re.split("d", "siddharths",2)
['si', '', 'harths']
>>> re.split("d", "siddharths",1)
['si', 'dharths']
>>> re.findall(r"\Bain","The rain in Spain")
['ain', 'ain']
>>> p =re.compile("d")
>>> p.search("door")
<re.Match object; span=(0, 1), match='d'>
>>> p.search("doord")
<re.Match object; span=(0, 1), match='d'>
>>> re.findall("hello world","hello", 1)
[]
>>> re.search("aaaa","alohaaaa")
<re.Match object; span=(4, 8), match='aaaa'>
>>> sentence = 'we are humans'
>>> matched = re.match(r'(.*) (.*?) (.*)', sentence)
>>> print(matched.groups())
('we', 'are', 'humans')
>>> sentence = 'we are humans'
>>> matched = re.match(r'(.*) (.*?) (.*)', sentence)
>>> print(matched.group())
we are humans
>>> #https://stackoverflow.com/questions/9347950/whats-the-difference-between-groups-and-group-in-the-re-module
>>> sentence = 'we are humans'
>>> matched = re.match(r'(.*) (.*?) (.*)', sentence)
>>> print(matched.group(2))
are
>>> sentence = 'horses are fast'
>>> regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
>>> matched = re.search(regex, sentence)
>>> print(matched.groupdict())
{'animal': 'horses', 'verb': 'are', 'adjective': 'fast'}
>>> sentence = 'horses are fast'
>>> regex = re.compile('(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
>>> matched = re.search(regex, sentence)
>>> print(matched.group(2))
are
>>> 
"""


