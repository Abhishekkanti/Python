#Find ASCII Value of a character 'X' and 'x'

c = "X"

  print("The ASCII value of " + c+ ' is' ,ord(c))

#Python program to check if the input number is odd
num = int(input("Enter a number: "))

if (num % 2) == 0: 

     print("/n It is a Even Number ",format (num))

else:

     print( "It is a Odd Number ",format(num))
    
    #Write programm to calculate monthly simple intrest

p=161258

t=30

r=5

print('The principal is', p)

print('The time period is', t) 

print('The rate of interest is',r)
si = (p * t * r)/100
      

print('The Simple Interest is', si)
      
      #Python program to find the quotient and remainder

h=7

m=2

q=h/m

print("quotient :", int(q))

r=h%m

print("remainder :",r)


#Python program to swap two variables

x = 5

y = 10


print("\n value of x Before Swapping is :",x)

print("\n value of y Before Swapping is :",y)

temp=x

x=y

y=temp

print("\n value of x After Swapping is  :",x)

print("\n value of y After Swapping is :",y)

#Program to calculate GST i.e. 18% on base price 34900/-
baseprice = 34900

GST =0.18 * baseprice

print("GST =",GST)


#Check whether an alphabet is vowel or consonant using if..else statement - a,b,e,o

a=input("Input a letter of the alphabet: ")

if a in ('a', 'e', 'i', 'o', 'u'):

	 print("%s is a vowel." % a)     
	    
else:
     print("%s is a consonant." % a)
     
     #Program to generate equated monthly instalments (EMI)(intrest 5%/Month) of 3 year and 5 year of amount 161258/-

a=16125   #instalments for 3 years
    
e3=a/36   #instalments for 5 years
 
e5=a/60    #instalments for 3 years with 5% intrest
    
emi=e3+(0.05*e3)  #instalments for 5 years with 5% intrest

emi=e5+(0.05*e5)

print("EMI for 3 years with 5% intrest",emi)
     
print("EMI for 5 years with 5% intrest",emi)


