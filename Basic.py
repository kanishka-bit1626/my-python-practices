1.)Input and Output Practice
Write a program that reads one value of each type from the user in the following order:

Input Format:
First line: integer
Second line: float
Third line: character
Fourth line: long integer
Fifth line: double

Output Format:
Print each value on a separate line in the same order as input.

Smaple Input :
10
3.14
A
10000000000
2.71828

Smaple Output :
10
3.14
A
10000000000
2.71828

a= int(input())
b= float(input())
c= (input())
d=int(input())
e=float(input())
print(a)
print(b)
print(c)
print(d)
print(e)


2.)Progressive Float Execution
Write a program that reads a floating-point number and prints successively rounded values, reducing the number of decimal places by one each step.

Input Format:
A single floating-point number.

Output Format:
Print each step on a separate line.
Rounded to 5 decimal places
Rounded to 4 decimal places
Rounded to 3 decimal places
Rounded to 2 decimal places
Rounded to 1 decimal place
Integer part only

Smaple Input :
34.12345

Smaple Output :
34.12345
34.1235
34.123
34.12
34.1
34

import struct
a=float(input())
a=struct.unpack('f',struct.pack('f',a))[0]
print("%.5f" % a)
print("%.4f" % a)
print("%.3f" % a)
print("%.2f" % a)
print("%.1f" % a)
print("%.0f" % a)


3.)Problem: Sum, Difference, Product, Division and Modulo.
Given two integers A and B, print their sum, difference,product, quotient and remainder each on a new line.

Input Format:
Two integers A and B ,where B ≠ 0.

Output Format:
Line 1: A + B
Line 2: A - B
Line 3: A * B
Line 4: Quotient (A / B)
Line 5: Remainder (A % B)

Smaple Input :
4 5

Smaple Output :
9
-1
20
0
4


A,B=map(int,input().split())
print(A+B)
print(A-B)
print(A*B)
print(int(A/B))
if A<0 or B<0:
  mod=abs(A)%abs(B)
  print(-1*mod)
else:
  print(A%B)


  4.)ASCII
Write the program to execute conversion of other datatype.

Input Format:
A single integer n (0 ≤ n ≤ 127), representing an ASCII code.

Output Format:
Print the character corresponding to the ASCII value.

Smaple Input :
97

Smaple Output :
a

n=int(input())
print(chr(n))



 5.)Update Counter
You are given an integer counter. Perform the following operations in order:
Add 5
Multiply by 2
Subtract 3
Print the final value.

Input Format:
Single integer counter.

Output Format:
Final value after operations.

Smaple Input :
4

Smaple Output :
15

((4 + 5) * 2) - 3 = 15


a=int(input())
b=((a+5)*2)-3
print(b)


 6.)ODD or EVEN
Max Score: 10 | Difficulty: easy

Write a program that reads an integer and prints whether the number is Odd or Even using Ternary operator.

Input Format:

A single integer n.

Output Format:

Print “Odd” if the number is odd, otherwise print “Even”.

Smaple Input :
4

Smaple Output :
Even

n=int(input())
result="Even"if n%2==0 else "Odd"
print(result)

7.)Greatest Among Three Numbers
Write a program that reads an integer and print greatest among tree number using Ternary operator.

Input Format:
Three integers, each on a separate line.

Output Format:
Print the greatest integer among the three.

Smaple Input 1:
4
89
34

Smaple Output 1:
89

Smaple Input 2:
-5
-10
-3

Smaple Output 2:
-3


 a=int(input())
b=int(input())
c=int(input())
result=a if a>b and a>c else (b if b>c else c)
print(result)


8.)Character Digit to Integer
Write a program that reads a single character representing a digit ('0' to '9') and prints its integer value.

Input Format:
A single character representing a digit ('0' to '9').

Output Format:
Print the integer value of the character.

Smaple Input :
'7'

Smaple Output :
7

ch=input().strip()
result=int(ch)
print(result)

9.)Personalized Greeting
Write a program that asks the user to enter their name (a single word).
Then, print a personalized greeting using that name in a sentence.

Input Format:
A single word representing the name.

Output Format:
Print a sentence including the name exactly as shown in the example.

Smaple Input :
Peter

Smaple Output :
Hi Peter, welcome to the programming class!

 name=input()
print(f"Hi {name}, welcome to the programming class!")


 10.)Calculate Total and Average Marks
John wants to learn how to calculate the total and average marks of a student in programming.
Write a program that reads the student's name and marks in five subjects. Then calculate and print:
Total marks (sum of all five subjects)
Average marks (sum divided by 5, rounded to two decimal places)

Input Format:
First input: student’s name (string)
Second input: marks in subject 1 (integer)
Third input: marks in subject 2 (integer)
Fourth input: marks in subject 3 (integer)
Fifth input: marks in subject 4 (integer)
Sixth input: marks in subject 5 (integer)

Output Format:
First line: Student Name: <name>
Second line: Total Marks: <total>
Third line: Average Marks: <average> (rounded to 2 decimal places)

Smaple Input :
Venkades
45
78
62
55
80

Smaple Output :
Student Name: Venkades
Total Marks: 320
Average Marks: 64.00


name = input()
m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
m5 = int(input())

total = m1 + m2 + m3 + m4 + m5
average = total / 5

print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", format(average, ".2f"))


11.)Shape Area Calculation
Veena wants to learn how to calculate the area of different shapes (Square, Rectangle, Circle, Triangle) and implement it in programming.
Write a program to calculate the area of each shape based on the given inputs.

Formulas:
Square:Area=a×a
Rectangle:Area=l×b
Circle:Area=πr^2 (Use π = 3.14, round to 2 decimal places)
Triangle:Area=(1/2)×b×h

Input Format:
First input: Integer for side of square (a)
Second and third input: Integers for length (l) and breadth (b) of rectangle
Fourth input: Integer for radius (r) of circle
Fifth and sixth input: Integers for base (B) and height (h) of triangle
Constraints:
No constraints

Output Format:
Print the area of each shape in the following format:
Area of Square=...
Area of Rectangle=...
Area of Circle=...
Area of Triangle=...
  
Sample Input 0:
2
3
2
3
6
5

Sample Output 0:
Area of Square=4
Area of Rectangle=6
Area of Circle=28.26
Area of Triangle=15


  a = int(input())
l = int(input())
b = int(input())
r = int(input())
B = int(input())
h = int(input())

print("Area of Square=%d"%(a*a))
print("Area of Rectangle=%d"%(l*b))
print("Area of Circle=%.2f"%(3.14*r*r))
print("Area of Triangle=%d"%(int((0.5)*B*h)))


12.)Shape Perimeter Calculation Program
Max Score: 10 | Difficulty: easy

Veena wants to learn how to calculate the perimeter of different shapes — Square, Rectangle, Circle, and Triangle — to implement them in programming.
Write a program that reads the required dimensions and calculates the perimeter of each shape using the given formulas:

Square: 4 × a
Rectangle: 2 × (l + w)
Circle: 2 × π × r(round to 2 decimal places)
Triangle: side + base + side
Input Format:

First input: integer for side of the square
Second and third input: integers for length and width of rectangle
Fourth input: integer for radius of circle
Fifth, sixth, and seventh input: integers for side1, side2, and base of triangle
Output Format:
Print only the perimeter values, each on a new line, in this order:
Square → Rectangle → Circle → Triangle

Sample Input :
9
8
7
6
5
4
3

Sample Output :
36
30
37.68
12


a = int(input())
length=int(input())
width=int(input())
radius=int(input())
side1=int(input())
side2=int(input())
base=int(input())
print(4*a)
print(2*(length+width))
print("%.2f"%(2*3.14*radius))
print(side1+base+side2)


13.)Handling Mixed Inputs

Priya is writing a program that needs to take two kinds of input from the user — first an integer, and then a sentence on the next line.
However, after entering the integer, when she tries to type the sentence, the program immediately skips the input line and prints an empty output.
Write a program that correctly reads both the integer and the sentence, and then prints them on separate lines.

Input Format:
First line: An integer
Second line: A string (can contain spaces)

Output Format:
Print the integer on the first line
Print the string on the second line

Sample Input:
7
Learning program is fun

Sample Output:
7
Learning program is fun


    a=int(input())
b=input()
print(a)
print(b)


