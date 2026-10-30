1.)Identify the Nature of a Number

Take an integer as input and return "POSITIVE" if the integer is positive, "NEGATIVE" if the integer is negative and "ZERO" if the integer is zero.

Constraints:
-10000 <= input <= 10000

Input Format:
A single integer

Output Format:
A single line containing a string "POSITIVE" if the input is positive, "NEGATIVE" if the input is negative and "ZERO" if the input is zero.

Sample Input:
12

Sample Output:
POSITIVE

n=int(input())
if n > 0:
    print("POSITIVE")
elif n < 0:
    print("NEGATIVE")
else:
    print("ZERO")

2.)Explore Math Functions

Kumar wants to know how the math functions are working in programming. Could you please help him write a program to understand the behavior of some mathematical functions like floor, ceil, round, sqrt, and power.

Constraints:
-1000 <= input <= 1000

Input Format :
First input corresponds to a float value (used for floor, ceil, and round).
Second input corresponds to an integer (used for square root).
Third input corresponds to an integer (used as base value).
Fourth input corresponds to an integer (used as power value).

Output Format :
Execute and display the results in the following order:
Floor value of the float
Ceil value of the float
Rounded value of the float
Square root of the given integer
Base raised to the power of exponent

Sample Input:
67.6734
16
5
2

Sample Output:
67
68
68
4
25

import math
a=float(input())
b=int(input())
base=int(input())
power=int(input())
print(math.floor(a))
print(math.ceil(a))
print(int(round(a,0)))
print(int(math.sqrt(b)))
print(int(math.pow(base,power)))


3.)Smallest of Four Numbers

Write a program to read four integers and determine the minimum (smallest) number among them.

Input Format :
First line contains an integer (first number).
Second line contains an integer (second number).
Third line contains an integer (third number).
Fourth line contains an integer (fourth number).

Output Format :
Print the minimum of the four numbers.

Sample Input 0 :
12
45
7
23

Sample Output 0 :
7

a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(min(a,b,c,d))

4.)Truncate to Two Decimal Places

Write a program that takes a floating-point number as input and prints the value truncated (cut off) to two decimal places without rounding.

Input Format :
Input consists of a single floating-point number.

Constraints
No Constraints

Output Format :
Print the number truncated to two decimal places.

Sample Input 0:
45.678

Sample Output 0:
45.67

import math
a=float(input())
print(math.trunc(a*100)/100)


5.)Find Second Maximum Number

Write a program that reads three integers and finds the second largest number among them using if-else statements.
If all three numbers are equal, print: No second max.

Sample Input:
10
20
15

Sample Output:
15

a=int(input())
b=int(input())
c=int(input())
if a == b == c:
    print("No second max")
elif a >= b and a >= c:
    if b >= c:
        print(b)
    else:
        print(c)
elif b >= a and b >= c:
    if a >= c:
        print(a)
    else:
        print(c)
else:
    if a >= b:
        print(a)
    else:
        print(b)



6.)Triangle Angle Validation

Take three integers A, B, C which denote the angles of a triangle.
Print "VALID" if the angles can form a triangle.
Print "NOT VALID" if they cannot form a triangle.
If the triangle is valid, also print its type on the second line:
"EQUILATERAL" → All three angles are equal (each 60°).
"ISOSCELES" → Exactly two angles are equal.
"SCALENE" → All three angles are different.

Constraints:
0 <= A, B, C <= 180

Input Format:
Three integers, each on a separate line, representing the angles of a triangle.

Output Format:

First line: "VALID" or "NOT VALID"
Second line: Triangle type if valid ("EQUILATERAL", "ISOSCELES", or "SCALENE"). Leave the second line empty if the triangle is not valid.
Sample Input:
30
60
90

Sample Output:
VALID
SCALENE

a = int(input())
b = int(input())
c = int(input())
if a + b + c == 180 and a > 0 and b > 0 and c > 0:
    print("VALID")
    if a == b == c:
        print("EQUILATERAL")
    elif a == b or b == c or a == c:
        print("ISOSCELES")
    else:
        print("SCALENE")
else:
    print("NOT VALID")
    print()


7.)Number to Word
Max Score: 10 | Difficulty: easy

Write a program that reads a single-digit number (0–9) as input and prints its word representation.

Input Format:

A single integer n (0 ≤ n ≤ 9)

Output Format:

Print the corresponding word for the input number in lowercase.

Sample Input:
7

Sample Output:
seven

n = int(input())

words = ["zero", "one", "two", "three", "four",
         "five", "six", "seven", "eight", "nine"]

print(words[n])


8.)  Vowel or Consonant

Write a program that reads a single character as input and prints whether it is a vowel or a consonant.

Consider a, e, i, o, u (both lowercase and uppercase) as vowels.

All other alphabets are consonants.

Input Format:

A single character ch (alphabet a–z or A–Z)

Output Format:

Print "vowel" if the character is a vowel.

Print "consonant" if the character is a consonant.

Sample Input:
a

Sample Output:
vowel

ch = input()

if ch in "aeiouAEIOU":
    print("vowel")
else:
    print("consonant")

9.)Leap Year Checker

Write a program that reads a year as input and prints whether it is a leap year or not.
Print "yes" if the year is a leap year.
Print "no" if the year is not a leap year.
A leap year occurs every 4 years, but some years are not leap years even if divisible by 4. Some special years are also leap years. Your program should determine this correctly based on the input year.

Input Format:
A single integer representing the year.

Output Format:
Print "yes" if it is a leap year.
Print "no" if it is not a leap year.

Sample Input:
2000

Sample Output:
yes


year = int(input())

if year % 400 == 0:
    print("yes")
elif year % 100 == 0:
    print("no")
elif year % 4 == 0:
    print("yes")
else:
    print("no")

10.)Fun Grade Calculator

Write a program that reads marks in five subjects and calculates the average. Based on the average, return a fun and encouraging grade according to the following rules:

Average ≥ 90 → "Excellent!"
Average ≥ 80 and < 90 → "Great Job!"
Average ≥ 70 and < 80 → "Good Effort!"
Average ≥ 50 and < 70 → "Keep Trying!"
Average < 50 → "Better Luck Next Time!"
Constraints:
0 <= marks in each subject <= 100

Input Format:
Five integers, each on a separate line, representing marks in five subjects.

Output Format:
A single line containing the fun grade.

Sample Input:
100
90
80
70
60

Sample Output:
Great Job!

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

avg = (a + b + c + d + e) / 5

if avg >= 90:
    print("Excellent!")
elif avg >= 80:
    print("Great Job!")
elif avg >= 70:
    print("Good Effort!")
elif avg >= 50:
    print("Keep Trying!")
else:
    print("Better Luck Next Time!")

11.)Train Berth Type Finder

Write a program to determine the berth type based on the seat number.
In a train coach, each seat number corresponds to a specific berth type. For a given seat number, your task is to determine which berth type it is. The seat allocation in most Indian Sleeper (SL) and 3AC coaches follows a repeated pattern of 8 seats:

1 → LB (Lower Berth)
2 → MB (Middle Berth)
3 → UB (Upper Berth)
4 → LB (Lower Berth)
5 → MB (Middle Berth)
6 → UB (Upper Berth)
7 → SL (Side Lower)
0 → SU (Side Upper)
Constraints:
1 ≤ Seat Number ≤ 72 — Valid seat numbers in a coach

Input Format:
First line contains a single integer T lines each contain one integer — the seat number.

Output Format:
For each test case, print the corresponding berth type in uppercase:
LB, MB, UB, SL, SU

Sample Input:
1

Sample Output:
LB


n = int(input())
r = n % 8

if r == 1 or r == 4:
    print("LB")
elif r == 2 or r == 5:
    print("MB")
elif r == 3 or r == 6:
    print("UB")
elif r == 7:
    print("SL")
else:
    print("SU")


12.)Electricity Bill Calculator

Write a program to calculate the electricity bill based on the number of units consumed.

The billing rules are as follows:

For the first 50 units, Rs 1 per unit.
For the next 100 units (51–150), Rs 2 per unit.
For the next 100 units (151–250), Rs 3 per unit.
For units above 250, Rs 4 per unit.
If the total bill exceeds Rs 150, add an additional surcharge of 20% of the total bill.

Constraints:
0 <= number of units <= 1000

Input Format:
A single integer or float denoting the number of electricity units consumed.

Output Format:
Print the total electricity charge (including surcharge if applicable).

Sample Input:
120

Sample Output:
228

Explanation:
First 50 units → 50 × 1 = 50
Next 70 units → 70 × 2 = 140
Total = 190 > 150 → add 20% surcharge = 38
Total bill = 190 + 38 = 228


units = float(input())

if units <= 50:
    bill = units * 1
elif units <= 150:
    bill = 50 + (units - 50) * 2
elif units <= 250:
    bill = 50 + 200 + (units - 150) * 3
else:
    bill = 50 + 200 + 300 + (units - 250) * 4

if bill > 150:
    bill = bill + bill * 0.20

print(int(bill) if bill == int(bill) else bill)


 13.)Thala vs Thalapathy Game

Write a program that takes a number as input and prints a famous Tamil cinema reference based on divisibility:

If the number is divisible by 3 only, print "Thala"
If the number is divisible by 5 only, print "Thalapathy"
If the number is divisible by both 3 and 5, print "ThalaThalapathy"
If the number is divisible by neither 3 nor 5, print the number itself
Constraints:
1 <= n <= 1000

Input Format:
A single integer n.

Output Format:
Print "Thala", "Thalapathy", "ThalaThalapathy", or the number itself, based on the rules above.

Sample Input:
30

Sample Output:
ThalaThalapathy


 n = int(input())

if n % 3 == 0 and n % 5 == 0:
    print("ThalaThalapathy")
elif n % 3 == 0:
    print("Thala")
elif n % 5 == 0:
    print("Thalapathy")
else:
    print(n)


 14.)Train Fare Calculator
Max Score: 10 | Difficulty: easy

Write a program to calculate the train fare based on the passenger’s age and distance to travel. The fare rules are:

Children (age < 12): 50% of standard fare per km
Adults (12 ≤ age ≤ 59): 100% of standard fare per km
Seniors (age ≥ 60): 75% of standard fare per km
Standard fare per km: Rs 5
The program should calculate the total fare based on distance and age category.

Constraints:
1 <= age <= 120
1 <= distance <= 1000

Input Format:

First line: An integer denoting age of the passenger
Second line: An integer denoting distance in km
Output Format:
Print the total fare in rupees as an integer or float.

Sample Input:
10
100

Sample Output:
250

Explanation:
Age < 12 → 50% of fare
Standard fare = 100 × 5 = 500
Discounted fare = 500 × 0.5 = 250


age = int(input())
distance = int(input())

fare = distance * 5

if age < 12:
    fare = fare * 0.5
elif age >= 60:
    fare = fare * 0.75

print(int(fare) if fare == int(fare) else fare)


 15.)Average Marks Calculator

Write a program that reads marks in five subjects and calculates the average.

If the average is a whole number, print it as an integer.

If the average is not a whole number, print it with exactly two digits after the decimal point.

Constraints:
0 <= marks in each subject <= 100

Input Format:
Five integers, each on a separate line, representing marks in five subjects.

Output Format:
Print the average marks following the rules above.

Sample Input:
50
50
50
50
50

Sample Output:
50

Sample Input:
45
93
23
45
65

Sample Output:
54.20



a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

avg = (a + b + c + d + e) / 5

if avg.is_integer():
    print(int(avg))
else:
    print(f"{avg:.2f}")
 

16.)Fun Character Case Converter

Write a program that takes a single character as input and performs the following:

If the character is a lowercase letter, convert it to uppercase.

If the character is an uppercase letter, convert it to lowercase.

If the character is not an alphabet, print a funny Tamil-style sentence like "abcd theriyatha?"

Constraints:
Input is a single character

Input Format:
A single character

Output Format:
Converted character (upper/lower) or "abcd theriyatha?" if the input is not a letter

Sample Input:
a

Sample Output:
A


ch = input()

if ch.islower():
    print(ch.upper())
elif ch.isupper():
    print(ch.lower())
else:
    print("abcd theriyatha?")
