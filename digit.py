1.)Count the number of digits

Write a program to count the number of digits in a given integer.

📥 Input
A single integer N

📤 Output
Print the number of digits

✅ Example
Input:
12345

Output:
5

Input:
0

Output:
1


n = int(input())

if n == 0:
    print(1)
else:
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    print(count)


2.)Sum of Even Digits

💻 Problem Statement
Write a program to find the sum of all even digits in a given number.

📥 Input Format
A single integer N

📤 Output Format
Print the sum of even digits

🧾 Constraints
0 ≤ N ≤ 10^9

✅ Example
Input:
1234
Output:
6

Input:
137
Output:
0

👉 Explanation: Even digits = 2, 4 → 2 + 4 = 6


n = int(input())
Evensum = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        Evensum = Evensum + digit
    n = n // 10

print(Evensum)


3.)Product of Digits

💻 Problem Statement
Write a program to find the product of all digits of a given integer.
📥 Input
A single integer N

📤 Output
Print the product of digits

✅ Example
Input:
123

Output:
6

Explanation :
Take number: 123
Digits are:
1, 2, 3
Now multiply:
1 × 2 × 3 = 6
So output = 6


n = int(input())
product = 1

while n > 0:
    digit = n % 10
    product = product * digit
    n = n // 10

print(product)



4.)Reverse a Number

💻 Problem Statement
Write a program to reverse a given integer.

📥 Input
A single integer N

📤 Output
Print the reversed number

✅ Example
Input:
1234

Output:
4321


n=int(input())
rev=0
while n>0:
  last=n%10
  rev=rev*10+last
  n=n//10
print(rev)


5.)Palindrome Number
Max Score: 10 | Difficulty: easy

💻 Problem Statement
Write a program to check whether a given number is a palindrome or not.
A number is a palindrome if it remains the same when its digits are reversed.

🔍 Examples
121 → reverse → 121 ✅ Palindrome
123 → reverse → 321 ❌ Not Palindrome
444 → reverse → 444 ✅ Palindrome

📥 Input Format
A single integer N

📤 Output Format
Print "Palindrome" if the number is same when reversed
Otherwise print "Not Palindrome"

🧾 Constraints

0 ≤ N ≤ 10^9

✅ Example
Input:
121

Output:
Palindrome

Input:
123

Output:
Not Palindrome

n=int(input())
temp=n
rev=0
while n>0:
  rev=rev*10+n%10
  n=n//10
if rev==temp:
  print("Palindrome")
else:
  print("Not Palindrome")


6.)First Digit of a Number

💻 Problem Statement
Write a program to find the first digit of a given number.

📥 Input Format
A single integer N

📤Output Format
Print the first digit of the number

🧾Constraints
0 ≤ N ≤ 10^9

✅ Example
Input:
9876

Output:
9

👉 Explanation: First digit of 9876 is 9



n=int(input())
while n>9:
  n=n//10
print(n)


7.)Count Zeros in a Number

💻 Problem Statement
Write a program to count how many zeros (0s) are present in a given number.

📥 Input Format
A single integer N

📤 Output Format
Print the count of zeros in the number

🧾 Constraints
0 ≤ N ≤ 10^9

✅ Example
Input:
10020
Output:
3
👉 Explanation:Zeros are 0, 0, 0 → count = 3

Input:
0
Output:
1


n=input().strip()
count=n.count("0")
print(count)


8.Armstrong Number

Problem Statement
Write a program to check whether a given number is an Armstrong number or not.
Explanation :
An Armstrong number is a number where the sum of each digit raised to the power of total number of digits is equal to the original number.
Example:
For 3-digit (153):
Digits = 3
1³ + 5³ + 3³ = 153 ✅

For 4-digit (9474):
Digits = 4
9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474 ✅

📥 Input
A single integer N

📤 Output
Print "Armstrong" or "Not Armstrong"

🧾 Constraints

0 ≤ N ≤ 10^9

✅ Example
Input:
153
Output:
Armstrong



n = int(input())
temp = n
digit = 0

while n > 0:
    n = n // 10
    digit += 1

n = temp
sum = 0

while n > 0:
    last = n % 10
    sum = sum + last ** digit
    n = n // 10

if sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")

9.)Check Perfect Number

💻 Problem Statement
Write a program to check whether a given number is a Perfect number or not.

👉 A number is called Perfect if the sum of its proper divisors (excluding itself) is equal to the number.
Explanation:
Perfect number :
Factors of 6 = 1, 2, 3
Sum = 1 + 2 + 3 = 6

Not Perfect Number:
10 → 1 + 2 + 5 = 8 ≠ 10 → Not Perfect

📥 Input Format
A single integer N
📤 Output Format
Print "Perfect" if the number is perfect
Otherwise print "Not Perfect"

🧾 Constraints
1 ≤ N ≤ 10^6

✅ Example
Input:
6
Output:
Perfect
Input:
10
Output:
Not Perfect

n=int(input())
total=0

for i in range(1,n):
      if n % i == 0:
        total += i
        
if total == n:
    print("Perfect")
else:
    print("Not Perfect")































































































































































































































































