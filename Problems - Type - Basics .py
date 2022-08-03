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

