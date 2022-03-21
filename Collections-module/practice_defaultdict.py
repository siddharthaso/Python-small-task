""" Input Format

The first line contains integers,
and separated by a space.
The next lines contains the words belonging to group .
The next lines contains the words belonging to group

Output Format
Output
lines.
The line should contain the -indexed positions of the occurrences of the word separated by spaces.

Sample Input

STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b

Sample Output

1 2 4
3 5"""

from collections import defaultdict,OrderedDict

n,m = map(int,input().split(' '))

nl=defaultdict(list)
ans =  OrderedDict(defaultdict(list))
ml=[]

for i in range(n):
    nl[input()].append(i+1)

for i in range(m):
    ml.append(input())
    temp=ml[i]
    if nl[temp]: ans[temp] = nl[temp]
    else:   ans[temp] = [-1]

for i in ml:
    print(' '.join(map(str,ans[i])))

""" 
    5 2

    a

    a

    b

    a

    b

    a

    b

Your Output (stdout)

    1 2 4 

    3 5  """