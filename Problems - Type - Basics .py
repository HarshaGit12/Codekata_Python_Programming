**1. Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'**

Sample Testcase :
INPUT
4 2
1 2 3 3
OUTPUT
yes

**CODE:**
S = list(map(int,input().split(" ")))
N = list(map(int,input().split(" ")))

n = S[0]
K = S[1]

if K in N:
  print("yes")
else:
  print("no")

**2. Given a number N, print 'yes' if it is composite else print 'no'.**

Sample Testcase :
INPUT
123
OUTPUT
yes

**CODE:**
num = int(input())

if num > 1:
  for i in range(2,num):
    if (num % i == 0):
      print("yes")
      break
  else:
    print("no")   
elif num == 0 or num == 1:
  print("no")
else:
  print("no")
  
**3. Write a code to get an integer N and print the even values from 1 till N in a separate line.**

Input Description:
A single line contains an integer N.

Output Description:
Print the even values from 1 to N in a separate line.

Sample Input :
6
Sample Output :
2
4
6

**CODE:**
n = int(input())

for i in range(1,n+1):
  if i%2 == 0:
    print(i)

**4. Write a code to get the input and print it 5 times.**

Input Description:
A single line contains an integer N.

Output Description:
Output contains 5 lines with each line having the value N.

Sample Input :
4
Sample Output :
4
4
4
4
4

**CODE:**
num = int(input())

for i in range(0,5):
    print(num)

**5. Given 3 numbers N , L and R. Print 'yes' if N is between L and R else print 'no'.**

Sample Testcase :
INPUT
3
2 6
OUTPUT
yes

**CODE:**
num = int(input())
t = list(map(int,input().split(" ")))

n = num
l = t[0]
r = t[1]

if (l<n<r):
  print("yes")
else:
  print("no")

**6. Given numbers A,B find A^B.**

Input Size : 1 <= A <= 5 <= B <= 50
Sample Testcase :
INPUT
3 4
OUTPUT
81

**CODE:**
p = list(input().split(" "))

a = int(p[0])
b = int(p[1])

if (1<=a<=5 and 1<=b<=50):
  print(a**b)

**7. Find the minimum among 10 numbers.**

Sample Testcase :
INPUT
5 4 3 2 1 7 6 10 8 9
OUTPUT
1

**CODE:**
l = list(map(int,input().split(" ")))

min1 = l[0]

for i in range(0, len(l)):
  if l[i]<min1:
    min1 = l[i]
print(min1)

**8. Given 2 numbers N and M add both the numbers and check whether the sum is odd or even.**

Sample Testcase :
INPUT
9 2
OUTPUT
odd

**CODE:**
S = list(map(int,input().split(" ")))

n = S[0]
m = S[1]

a = n+m

if a%2 == 0:
  print('even')
else:
  print('odd')

**9. Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.**

Sample Testcase :
INPUT
6 2
1 2 3 5 7 8
OUTPUT
0

**CODE:**
S = list(map(int,input().split(" ")))
N = list(map(int,input().split(" ")))

n = S[0]
K = S[1]

count = 0

for i in N: 
  if K == i:
    count = count + 1
print(count-1)

**10. Given base(B) and height(H) of a triangle find its area.**

Input Size : N <= 1000000
Sample Testcase :
INPUT
2 4
OUTPUT
4

**CODE:**
T = list(map(int,input().split(" ")))

B = T[0]
H = T[1]

A = (1/2)*B*H

print(A)

**11. Write a code to get an integer N and print the digits of the integer.**

Sample Input :
348
Sample Output :
3 4 8

**CODE:**
s = input()

dum = ""

for i in range(0,len(s)):
  if(i == len(s)-1):
    dum = dum + s[i]
  else:
    dum = dum + s[i] + " "

print(dum)

**12. Given a number N and an array of N elements, find the Bitwise OR of the array elements.**

Input Size : N <= 100000
Sample Testcase :
INPUT
2
2 4
OUTPUT
6

**CODE:**
n = int(input())

arr = list(map(int,input().split(" ")))

def find_or(arr):
  ans = arr[0]

  for i in range(1,len(arr)):
    ans = ans|arr[i]
  return ans

print(find_or(arr))

**13. Write a code to get a integer n as input and calculate the smallest perfect power of 2 greater than n.**

Input Description:
A single line containing an integer,n.

Output Description:
Print the smallest perfect power of 2 greater than n.

Sample Input :
48
Sample Output :
64

**CODE:**
n = int(input())

for i in range(0,2**1000):
  if 2**i > n:
    print(2**i)
    break

**14. Write a code to get an integer N and print the values from N to 1.**

Input Description:
A single line contains an integer N.

Output Description:
Print the values from N to 1 in a separate line.

Sample Input :
10
Sample Output :
10
9
8
7
6
5
4
3
2
1

**CODE:**
s = int(input())

for i in range(0,s):
    i = s
    s = s-1
    print(i)

**15. Write a code to get 2 integers A and N. Print the integer A, N times in separate line.**

Input Description:
First line contains an integer A. Second line contains an Integer N.

Output Description:
Print the integer A, N times in a separate line.

Sample Input :
2 3
Sample Output :
2
2
2

**CODE:**
t = list(map(int,input().split(" ")))

for i in range(0,t[1]):
    print(t[0])

**16. Given a range of 2 numbers (i.e) L and R count the number of prime numbers in the range (inclusive of L and R ).**

Input Size : L <= R <= 100000(complexity O(n) read about Sieve of Eratosthenes)
Sample Testcase :
INPUT
2 5
OUTPUT
3

**CODE:**
l = list(map(int,input().split(" ")))

lower = l[0]
upper = l[1]

array = []

for num in range (lower, upper+1):
 if num>1:
  for i in range (2,num):
   if num % i==0:
    break
  else:
    array.append(num)
print (len(array))

**17. Given an array of N elements switch(swap) the element with the adjacent element and print the output.**

Sample Testcase :
INPUT
5
3 2 1 2 3
OUTPUT
2 3 2 1 3

**CODE:**
def swapTwo(x, y):
  x = x ^ y
  y = x ^ y
  x = x ^ y
  return x, y

def rearrangeArray(a, n):
  for i in range (0, n - 1, 2):
    a[i], a[i + 1] = swapTwo(a[i], a[i + 1])
  print(*a)

n = int(input())

arr = list(map(int,input().split(" ")))

rearrangeArray(arr, n)

**18. Given 3 numbers A,B,C process and print 'yes' if they can form the sides of a triangle otherwise print 'no'.**

Input Size : A,B,C <= 100000
Sample Testcase :
INPUT
3 4 5
OUTPUT
yes

**CODE:**
tr = list(map(int,input().split(" ")))

A = tr[0]
B = tr[1]
C = tr[2]

if A+B>C and B+C>A and C+A>B:
    print('yes')
else:
    print('no')

**19. Given 2 numbers N,M. Print 'yes' if their product is a perfect square else print 'no'.**

Sample Testcase :
INPUT
5 5
OUTPUT
yes

**CODE:**
import math

S = list(map(int,input().split(" ")))

N = S[0]
M = S[1]


def perfsq(x):
  if (math.ceil(math.sqrt(x)) == math.floor(math.sqrt(x))):
    print('yes')
  else:
    print('no')


x = N*M

perfsq(x)

**20. Given 3 numbers A,B,C print 'yes' if they can form the sides of a right angled triangle,otherwise 'no'.**

Input Size : A,B,C <= 100000
Sample Testcase :
INPUT
3 4 5
OUTPUT
yes

**CODE:**
tr = list(map(int,input().split(" ")))

A = tr[0]
B = tr[1]
C = tr[2]

if A**2+B**2==C**2 or B**2+C**2==A**2 or C**2+A**2==B**2:
    print('yes')
else:
    print('no')

**21. Given a string 'S' swap the even and odd characters starting from index 1(Assume the index starts from 0).**

Input Size : |s| <= 10000000(complexity O(n))
Sample Testcase :
INPUT
codekata
OUTPUT
ocedakat

**CODE:**
S = input()

output = ''

i = 0

while i < len(S):
  if i + 1 < len(S):
    output = output + S[i + 1]
    output = output + S[i]
    i = i + 2
print(output)

**22. Write a code to get 2 integers as input and find the HCF of the 2 integer without using recursion or Euclidean algorithm.**

Input Description:
A single line containing 2 integers separated by space.

Output Description:
Print the HCF of the integers.

Sample Input :
2 3
Sample Output :
1

**CODE:**
p = list(input().split(" "))

x = int(p[0])
y = int(p[1])

if x > y:
  smaller = y  
else:
  smaller = x
for i in range(1,smaller + 1):
  if((x % i == 0) and (y % i == 0)):
    hcf = i 
print(hcf) 

**23. Write a code to get 2 integers as input and add the integers without any carry.**

Input Description:
A single line containing 2 integers.

Output Description:
Print sum of the 2 integers without carry

Sample Input :
44 66
Sample Output :
0

**CODE:**
import math
 
def xSum(n, m) :
  res = 0
  multiplier = 1
  bit_sum = 0
  while (n or m) :
    bit_sum = ((n % 10) + (m % 10))
    bit_sum = bit_sum % 10
    res = (bit_sum * multiplier) + res
    n = math.floor(n / 10)
    m = math.floor(m / 10)
    multiplier = multiplier * 10
  return res

d = list(map(int,input().split(" ")))

n = d[0]
m = d[1]

print(xSum(n, m))

**24. Let P represent Paper, R represent Rock and S represent Scissors. Given 2 out of the 3 determine which one wins. If its a draw print 'D'.**

Sample Testcase :
INPUT
R P
OUTPUT
P

**CODE:**
s = list(map(str,input().split(" ")))

l = s[0]
r = s[1]

if l==r:
  print("D")
elif (l=='R' and r=='P') or (l=='P' and r=='R'):
  print("P")
elif (l=='P' and r=='S') or (l=='S' and r=='P'):
  print("S")
elif (l=='S' and r=='R') or (l=='R' and r=='S'):
  print("R")

**25. Write a program to get a string as input and reverse the string without using temporary variable.**

Input Description:
A single line containing a string.

Output Description:
Print the reversed string.

Sample Input :
GUVI
Sample Output :
IVUG

**CODE:**
s = input()

print(s[::-1])

**26. Given a number N, print the Bitwise NOT of that number.**

Input Size : 1 <= N <= 10000
Sample Testcase :
INPUT
5
OUTPUT
-6

**CODE:**
n = int(input())

def find_not(n):
  ans = ~n
  return ans

print(find_not(n))

**27. Write a code get an integer number as input and print the sum of the digits.**

Input Description:
A single line containing an integer.

Output Description:
Print the sum of the digits of the integer.

Sample Input :
124
Sample Output :
7

**CODE:**
d = input()

s = 0

for i in d:
  s = s + int(i)

print(s)

**28. Write a code to get an integer N and print values from 1 till N in a separate line.**

Input Description:
A single line contains an integer N.

Output Description:
Print the values from 1 to N in a separate line.

Sample Input :
5
Sample Output :
1
2
3
4
5

**CODE:**
num = int(input())

for i in range(1,num+1):
  print(i)

**29. Write a program to print the sum of the first K natural numbers.**

Input Size : n <= 100000
Sample Testcase :
INPUT
3
OUTPUT
6

**CODE:**
n = int(input())

dum = 0

for i in range(1,n+1):

  dum = dum + i

print(dum)

**30. The Caesar Cipher technique is one of the earliest and simplest method of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a 
given text is replaced by a letter some fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. 
The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.For the given input string(S) and shift print the encrypted string.**

Sample Testcase :
INPUT
ABCdEFGHIJKLMNOPQRSTUVWXYz 23
OUTPUT
XYZaBCDEFGHIJKLMNOPQRSTUVw

**CODE:**
def encrypt(text,s):
  result = ""
   
  for i in range(len(text)):
    char = text[i]
    if (char.isupper()):
      result += chr((ord(char) + s-65) % 26 + 65)
    else:
      result += chr((ord(char) + s - 97) % 26 + 97)
  return result

t = list(map(str,input().split(" ")))

text = t[0]
s = int(t[1])

print(encrypt(text,s))


** 31. Write a code get an integer number as input and print the odd and even digits of the number separately.**

Sample Input :
1234
Sample Output :
2 4
1 3

**CODE:**

A = list(map(int,input()))

A.sort()

def splitevenodd(A): 
   evenlist = [] 
   oddlist = [] 
   for i in A: 
      if (i % 2 == 0): 
         evenlist.append(i) 
      else: 
         oddlist.append(i)
   print(*evenlist) 
   print(*oddlist)  

splitevenodd(A)

** 32. The Romans have attacked again. This time they are much more than the Persians but Shapur is ready to defeat them. He says: 'A lion is never afraid of a hundred sheep'.

Nevertheless Shapur has to find weaknesses in the Roman army to defeat them. So he gives the army a weakness number.

In Shapur's opinion the weakness of an army is equal to the number of triplets i, j, k such that i < j < k and ai > aj > ak where ax is the power of man standing at position x. The Roman army has one special trait — powers of all the people in it are distinct.

Help Shapur find out how weak the Romans are.

The first line of input contains a single number n, the number of men in Roman army. Next line contains n different positive integers powers of men in the Roman army.**
Input Size : N<=100000

Sample Testcase :
INPUT
3
3 2 1
OUTPUT
1

**CODE:**

from bisect import bisect_left as lower_bound
def update(BIT, n, i, val):
  while i <= n:
    BIT[i] += val
    i += (i & -i)
def query(BIT, i):
  summ = 0
  while i > 0:
    summ += BIT[i]
    i -= (i & -i)
  return summ
def convert(arr, n):
  temp = [0] * n
  for i in range(n):
    temp[i] = arr[i]
 
  temp.sort()
 
  for i in range(n):
    arr[i] = lower_bound(temp, arr[i]) + 1
def getCount(arr, n):
  convert(arr, n)
 
  BIT = [0] * (n + 1)
  smaller_right = [0] * (n + 1)
  greater_left = [0] * (n + 1)
  for i in range(n - 1, -1, -1):
    smaller_right[i] = query(BIT, arr[i] - 1)
    update(BIT, n, arr[i], 1)
  for i in range(n + 1):
    BIT[i] = 0
  for i in range(n):
    greater_left[i] = i - query(BIT, arr[i])
    update(BIT, n, arr[i], 1)
  ans = 0
  for i in range(n):
    ans += greater_left[i] * smaller_right[i]
  return ans
n = int(input())
arr = list(map(int,input().split(" ")))
print(getCount(arr, n))

**33. Check whether the given 4 points form a square or not.**

Sample Testcase :
INPUT
10 10
10 20
20 20
20 10
OUTPUT
yes

**CODE:**
class Point:
     
  def __init__(self, x, y):
    self.x = x
    self.y = y
def distSq(p, q):
  return (p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y)

def isSquare(p1, p2, p3, p4):
 
  d2 = distSq(p1, p2) 
  d3 = distSq(p1, p3) 
  d4 = distSq(p1, p4)

  if d2 == 0 or d3 == 0 or d4 == 0:   
    return False 
  if d2 == d3 and 2 * d2 == d4 and \
                    2 * distSq(p2, p4) == distSq(p2, p3):
    return True
  if d3 == d4 and 2 * d3 == d2 and \
                    2 * distSq(p3, p2) == distSq(p3, p4):
    return True
  if d2 == d4 and 2 * d2 == d3 and \
                    2 * distSq(p2, p3) == distSq(p2, p4):
    return True
 
  return False

a = list(map(int,input().split(" ")))
b = list(map(int,input().split(" ")))
c = list(map(int,input().split(" ")))
d = list(map(int,input().split(" ")))

if __name__=="__main__":
  p1 = Point(a[0], a[1])
  p2 = Point(b[0], b[1])
  p3 = Point(c[0], c[1])
  p4 = Point(d[0], d[1])
     
  if isSquare(p1, p2, p3, p4):
    print('yes')
  else:
    print('no')
    
**34. Given a number N followed by N numbers.Find the smallest number and largest number and print both the indices(1 based indexing).**
Input Size : N <= 100000 

Sample Testcase :
INPUT
5
1 2 3 4 5
OUTPUT
1 5  

**CODE:**

n = int(input())

arr = list(map(int,input().split(" ")))
a = min(arr)
b = max(arr)
print(1+arr.index(a),1+arr.index(b))

** 35. Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. Find the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), if it is not possible to select coins in such a way that they sum up to S then print '-1'.
Example: Given coins with values 1, 3, and 5. And the sum S is 11.
Output: 3, 2 coins of 3 and 1 coin of 5**
Input Size : N<=10000
  
Sample Testcase:
INPUT
3 11
1 3 5
OUTPUT
3  

** CODE:**
  
import sys
def minCoins(coins, m, V):
  if (V == 0):
    return 0
  res = sys.maxsize
  for i in range(0, m):
    if (coins[i] <= V):
      sub_res = minCoins(coins, m, V-coins[i])
      if (sub_res != sys.maxsize and sub_res + 1 < res):
        res = sub_res + 1  
  return res
arr = list(map(int,input().split(" ")))
m = arr[0]
V = arr[1]
coins = list(map(int,input().split(" ")))
print(minCoins(coins, m, V))

** 36. Given a string S consisting of 2 words reverse the order of two words **
Input Size : |S| <= 10000000

Sample Testcase :
INPUT
hello world
OUTPUT
world hello

**CODE:**

S = list(input().split(" "))

a = S[0]
b = S[1]

temp = a
a = b
b = temp

print(a,b)

** 37. Write a code to get an integer N and print the sum of  values from 1 to N.**
Sample Input :
10
Sample Output :
55

**CODE:**

n = int(input())

dum = 0

for i in range(1,n+1):
    
    dum = dum + i
    
print(dum)

**38. Given a number N and an array of N elements ,find the Bitwise AND of the array elements.**
Input Size N <= 100000

Sample Testcase :
INPUT
4
4 3 2 1
OUTPUT
0

**CODE:**
  
n = int(input())

arr = list(map(int,input().split(" ")))

def find_and(arr):
  ans = arr[0]

  for i in range(1,n):
    ans = ans&arr[i]
  return ans

print(find_and(arr))

**39. Kabali is a brave warrior who with his group of young ninjas moves from one place to another to fight against his opponents. Before Fighting he just calculates one thing, the difference between his ninja number and the opponent's ninja number. From this difference he decides whether to fight or not. Kabali's ninja number is never greater than his opponent.
Input
The input contains two numbers in every line. These two numbers in each line denotes the number ninjas in Kabali's clan and his opponent's clan . print the absolute difference of number of ninjas between Kabali's clan and his opponent's clan. Each output should be in seperate line.**

Sample Testcase :
INPUT
100 200
OUTPUT
100

**CODE:**

K = list(map(int,input().split(" ")))
ad = abs(K[0]-K[1])
print(ad)

**40. Given 2 numbers N,M find the GCD of N and M.If it cannot be found for given number(s) then print -1**

Sample Testcase :
INPUT
10 5
OUTPUT
5

**CODE:**

import math

p = list(map(int,input().split(" ")))

n = p[0]
m = p[1]

g = math.gcd(n,m)

if n==0 or m==0:
  print(-1)
else:
  print(g)

**41. You are given with an array. For each element present in the array your task is to print the next smallest than that number. If it is not smallest print -1**

Sample Input :
7
10 7 9 3 2 1 15
Sample Output :
7 3 3 2 1 -1 -1

**CODE**

n = int(input())
arr = list(map(int,input().split(" ")))
nxtsmall = []
for i in range(0,n-2):
  if arr[i+1] < arr[i]:
    nxtsmall.append(arr[i+1])
  elif arr[i+2] < arr[i]:
    nxtsmall.append(arr[i+2])
  else:
    nxtsmall.append(-1)
for j in range(n-2,n):
  if j == n-2:
    if arr[j+1] < arr[j]:
      nxtsmall.append(arr[j+1])
    else:
      nxtsmall.append(-1)
  if j == n-1:
    if arr[j] < arr[j-1]:
      nxtsmall.append(arr[j])
    else:
      nxtsmall.append(-1)    
print(*nxtsmall)

**42. You are given an array. Your task is to sort the array in given manner. Print the elements in increasing order of the frequency. If frequency is same print smaller one first.**

Sample Input :
4
1 1 3 2
Sample Output :
2 3 1

**CODE**

from collections import defaultdict

def sortByFreq(arr, n):
    d = defaultdict(lambda: 0)
    for i in range(n):
        d[arr[i]] += 1
    arr.sort(key=lambda x: (d[x], x))
 
    return (arr)
    
    
n = int(input())
arr = list(map(int,input().split()))

solution = sortByFreq(arr, n)

freq = []
for char in solution:
    if char not in freq:
        freq.append(char)

print(*freq)

**43. You are given with array of numbers.you have to find whether array is beautiful or not. A beautiful array is an array whose sum of all numbers is divisible by 2, 3 and 5**

Input Description:
You are given a number ‘n’ denoting the size of array.Next line contains n space separated numbers.
Output Description:
Print 1 if array is beautiful and 0 if it is not

Sample Input :
5
5 25 35 -5 30
Sample Output :
1

**CODE**

import math

def LCMofArray(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//math.gcd(lcm, a[i])
  return lcm

arr1 = [2,3,5]
n = int(input())
arr = list(map(int,input().split(" ")))
s = sum(arr)
L = LCMofArray(arr1)

if s%L == 0:
  print(1)
else:
  print(0)
  
**44. Assume you are a student studying in school.You are given a task to find first negative integer for each and every window of size k.**

Input Description:
First line contains an integer n denoting the size of the array. The next line contains n space separated integers forming the array. The last line contains the window size k.
Output Description:
Print the first negative integer in that window.If all the numbers are positive print 0

Sample Input :
7
1 -2 -3 -4 5 6 -7
3
Sample Output :
-2 -2 -3 -4 -7

**CODE**

def printFirstNegativeInteger(arr, n, k):
    for i in range(0, (n - k + 1)):
        flag = False
        for j in range(0, k):
            if (arr[i + j] < 0):
                if i+j == n-1:
                    print(arr[i + j], end = "")
                    flag = True
                else:    
                    print(arr[i + j], end = " ")
                    flag = True
                    break
                
        if (not(flag)):
            if i+j == n-1:
                print(0, end = "")
                    
            else:    
                print(0, end = " ")
                
                    
n = int(input())
arr = list(map(int,input().split()))
k = int(input())
printFirstNegativeInteger(arr, n, k)    

**45. You are given with an circular array .Your task is calculate the difference between two consecutive number. And if difference is greater than ‘k’, print 1 else print 0**

Input Description:
You are given two numbers ‘n’, ’m’. Next line contains n space separated integers.
Output Description:
Print 1 if the difference is greater than ‘m’.

Sample Input :
5 15
50 65 85 98 35
Sample Output :
0 1 0 1 0

**CODE**

arn = list(map(int,input().split(" ")))
arr = list(map(int,input().split(" ")))
n = arn[0]
m = arn[1]
diff = []
for i in range(1,n+1):
  if i == n:
    if abs(arr[0]-arr[i-1]) > m:
      diff.append(1)
    else:
      diff.append(0)
  elif abs(arr[i]-arr[i-1]) > m:
    diff.append(1)
  else:
    diff.append(0)
print(*diff)

** 46. You are given with two arrays. Your task is to merge the array such that first array is in ascending order and second one in descending order.**

Input Description:
First line contains two integer ‘n’ and ‘m’. ‘n’ denotes length of array 1 and ‘m’ of array 2.Next line contains n space separated numbers and third line contains ‘m’ space separated numbers
Output Description:
Print a single array in desired order

Sample Input :
3 3
23 15 16
357 65 10
Sample Output :
15 16 23 357 65 10

**CODE**

l = list(map(int,input().split(" ")))
ar1 = list(map(int,input().split(" ")))
ar2 = list(map(int,input().split(" ")))
ar1.sort()
ar2.sort(reverse=True)
ar1.extend(ar2)
print(*ar1)

** 47. You are given with an array of numbers, Your task is to print the difference of indices of largest and smallest number.All number are unique.**

Input Description:
First line contains a number ‘n’. Then next line contains n space separated numbers.
Output Description:
Print the difference of indices of largest and smallest array

Sample Input :
5
1 6 4 0 3
Sample Output :
-2

**CODE**

n = int(input())
arr = list(map(int,input().split(" ")))
diff = arr.index(max(arr)) - arr.index(min(arr))
print(diff)

**48. You are provided with an array in which all elements are repeated thrice except one which is repeated twice.Your task is to print that number.**

Input Description:
First line contains a number denoting size of array ‘n’.Next line contains n space separated numbers
Output Description:
Print the number which is repeated twice

Sample Input :
5
13 12 13 12 13
Sample Output :
12

**CODE**

import collections

def CountFrequency(arr):
    return collections.Counter(arr)  

n = int(input())
arr1 = list(map(str,input().split(" ")))

freq = CountFrequency(arr1)

for (key, value) in freq.items():
    if value == 2:
        print(key)


