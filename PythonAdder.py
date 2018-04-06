#Write a program that takes a single input line of the form «number1»+«number2», 
#where both of these represent positive integers, and outputs the sum of the two numbers. 
#For example on input 5+12 the output should be 17. 

S = input()
for plusPosition in range (0,len (S)):
   if S[plusPosition] == '+':
      beforePlus = int (S[0:plusPosition])
      afterPlus = int (S[plusPosition: len(S)])
      print (beforePlus + afterPlus)