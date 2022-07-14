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
