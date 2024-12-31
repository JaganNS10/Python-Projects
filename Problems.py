"""To Find Highest Number towards its right side
arr = [16, 17, 4, 3, 5, 2]
arr = [10, 4, 2, 4, 1]
arr = [5, 10, 20, 40]
start=arr[0]
i = 0
Result = []
while i<len(arr)-1:
    Right = arr[i+1:]
    Max = max(Right)
    if start>=Max:
        Result.append(start)
    i+=1
    start = arr[i]
Result.append(arr[i])
print(Result)"""

""" Repeating and Missing
arr = [2,2]
repeating = 0
s = set(i for i in range(1, len(arr) + 1))
for a in arr:
    if a in s:
        s.remove(a)
    else:
        repeating = a
if s:
    missing = s.pop()
else:
    missing = 0"""

"""arr = [-1, 0, 1, 2, -1, -4]
arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
arr.sort()
d={}
l=[]
print(arr)
for i in arr:
    if -i in d and d[-i]>0:
        l.append([-i,i])
        d[-i]-=1
    else:
        d[i]=1
print(sorted(l,key=lambda x:x[0]))"""

# To Find Subset
'''
a= [11, 7, 1, 13, 21, 3, 7, 3]
b= [11, 3, 7, 1, 7]
a = [1, 1, 2, 3]
b = [1, 1, 1]
Count = 0
for i in b:
    if i in a:
        Count+=1
        a.remove(i)
if len(b)==Count:
    print(True)
else:
    print(False)

a={10,5,2,23,19}
b={19,5,3}
print(b.issubset(a))'''

# Frequencies of Limited Range Array Elements
"""arr = [2, 3, 2, 3, 5]
n = len(arr)
Result = []
for i in range(1,n+1):
    Count = arr.count(i)
    Result.append(Count)
print(Result) """

# First Repeating Element
"""def First_Repeating_Element(arr):
    for i in range(len(arr)):
        Count = arr.count(arr[i])
        if Count>1:
            return i+1
    return -1
arr = [1, 5, 3, 4, 3, 5, 6]
Object = First_Repeating_Element(arr)
print(Object)"""

# Move All Zeroes to End

"""arr = [1, 2, 0, 4, 3, 0, 5, 0]
arr=[10,10,10]
zeros = arr.count(0)
for i in range(zeros):
    arr.remove(0)
    arr.append(0)
print(arr)"""

# Remove Duplicates Sorted Array
"""arr = [2,2,2,2,2]
arr = [32,40,43,60,72,78,82,82,82,99]
i=0
j=1
while j<len(arr):
    if arr[i]!=arr[j]:
        i+=1
        arr[i]=arr[j]
    j+=1
print(i+1)"""


# Minimum distance in an Array
"""arr = [10, 3, 5, 6, 2]
arr = [3,9,7,7,3,1,8,6,5,7,5]
Pro = []
for i in range(len(arr)):
    Product = 1
    for j in range(len(arr)):
        if i!=j:
            Product*=j
    Pro+=[Product]
print(Pro)"""

# At Least K Occurrences

"""def Function(arr,k):
    Dict = {}
    if k==1:
        return arr[0]
    
    for i in arr:
        if i not in Dict:
            Dict[i]=1
        else:
            Dict[i]+=1
            if Dict[i]>=k:
                return i
    return -1
arr= [1, 7, 4, 3, 4, 8, 7]
k = 2
arr= [3, 1, 3, 4, 5, 1, 3, 3, 5, 4]
k=3
print(Function(arr,k))"""

# Three way partitioning

"""arr= [1, 4, 3, 6, 2, 1]
a = 1
b = 3
arr = [1, 2, 3, 3, 4]
a = 1
b = 2
Copy = []
for i in arr:
    if i<a:
        Copy.append(i)
for j in arr:
    if j>=a and j<=b:
        Copy.append(j)
for k in arr:
    if k>b:
        Copy.append(k)
for r in range(len(arr)):
    arr[r] = Copy[r]
print(arr,Copy)"""


# Find all pairs with a given sum

"""target = 9
arr1= [1, 2, 4, 5, 7, 4]
arr2= [5, 6, 3, 4, 8, 4]
pairs = []
for i in arr1:
    for j in arr2:
        if i+j==target:
            pairs.append((i,j))

pairs.sort()
print(pairs)"""

# Move all negative elements to end

"""arr= [1, -1, 3, 2, -7, -5, 11, 6 ]
Copy_of_arr = arr.copy()
for i in Copy_of_arr:
    if i<0:
        arr.append(i)
        arr.remove(i)
print(arr)

arr[:] = [num for num in arr if num >=0] + [num for num in arr if num<0]
print(arr)
"""

# Smallest subarray with sum greater than x

"""arr = [1, 4, 45, 6, 0, 19]
x=51
n = len(arr)
Size  = {}
for start in range(n):
    for end in range(start,n):
        subarray = arr[start:end+1]
        if sum(subarray)>x:
            Size[len(subarray)] = subarray
if Size:
    print(min(Size.keys()))
else:
    print(0)"""


# floor and ceil problem 

# The largest element in the array that is less than or equal to x
# If x is smaller than the smallest element in the array, then there is no floor for 𝑥
# x (it doesn’t exist).
# The smallest element in the array that is greater than or equal to 𝑥
# If x is greater than the largest element in the array, then there is no ceiling for x
# x (it doesn’t exist).

"""x = 7 
arr= [5, 6, 8, 9, 6, 5, 5, 6]
x = 37
arr=[17,23]
Result = []



if min(arr)<x:
    Res1 = []
    arr.sort(reverse=True)
    for i in arr:
        if i<=x:
            Res1.append(i)
    Result.append(Res1[0])
else:
    Result.append(-1)

if max(arr)>x:
    Res2 = []
    arr.sort()
    for j in arr:
        if j>=x:
            Res2.append(j)
    Result.append(Res2[0])
else:
    Result.append(-1)
print(Result)"""

#Longest substring 

"""s = "geeksforgeeks"
s = "aaa"
Dict = {}
for i in range(len(s)):
    for j in range(i,len(s)):
        substring = s[i:j+1]
        Set = set(substring)
        if len(substring)==len(Set):
            Dict[substring] = len(substring)

Max = max(Dict,key=Dict.get)
print(Max)"""

#Rotate an array

"""arr = [-1, -2, -3, 4, 5, 6, 7]
d = 2
for i in range(d):
    values = arr.pop(0)
    arr+=[values]
print(arr)"""


#More than n/k Occurrences
"""arr = [3, 1, 2, 2, 1, 2, 3, 3]
k = 4
Dictionary = {}
for i in arr:
    if i not in Dictionary:
        Dictionary[i]=1
    else:
        Dictionary[i]+=1
count = 0
for j in Dictionary:
    if Dictionary[j]>len(arr)//k:
        count+=1
print(count)"""

#Maximum no.of.character in lexogical order

"""s = "output"
s = "zxcvcvzx"
List_of_s = sorted(s)
Maximum = ""
Size = 0
for i in List_of_s:
    count = s.count(i)
    if count>Size:
        Size = count
        Maximum = i
print(Maximum)"""

#Reverse the givem array

"""arr = [1, 4, 3, 2, 6, 5]
Copy = list(reversed(arr))
for i in range(len(Copy)):
    arr[i] = Copy[i]
print(arr)"""

"""class one:
    def __init__(self,name=None,age=None):
        self.Name = name
        self.Age = age
    def disp(self):
        print(self.Name,self.Age)
class two(one):
    def __init__(self,dob=None,**kwargs):
        self.DOB = dob
        super().__init__(**kwargs)
        print(kwargs)
class three(two):
    def __init__(self,phno=None,**kwargs):
        self.Phno = phno
        super().__init__(**kwargs)
        print(kwargs)
Object = three(phno=985670901,dob='10-01-2005',name='Jagan',age=19)"""
# Object.disp()

# Nearest multiple of 10
"""str = 29
String = int(str)
Dict = {}
for i in range(10,String+2):
    if i%10==0:
        Result = max(String,i)-min(String,i)
        Dict[i] = Result
Get = min(Dict,key=Dict.get)"""

# Remove Consecutive Characters
"""s = "aabaa"
s = "abcddcba"
start = s[0]
for i in range(1,len(s)):
    if start[-1]!=s[i]:
        start+=s[i]
print(start)"""


















 



