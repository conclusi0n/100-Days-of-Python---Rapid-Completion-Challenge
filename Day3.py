#Control Flow with if / else and Conditional Operators
age_1= 69
if age_1 >= 18:
    print("you are good , Go in ")
else:
    print("No you too young for it ")

age_2= 100
age_3 = 200
if age_2 > age_3:
    print("you are elder thatn 3")
else:
    print("You are younger than 3 ")

    #Modulo Operator
#The modulo operator (%) gives the remainder of a division.
number =10
if number % 2 ==0 :
    print ("is even")
else:
    print ("is odd ")

    #Nested if Statements and elif Statements

age_4=20
age_5 = 20
citizen = True
if age_4 >= 18 :
    if citizen:
        print("can vote")
    else:
        print ("can't vote ")
else:
    print("You are an idiot")

marks = 100
if marks >= 95:
    print("A")
elif marks >=70:
    print ("B")
elif marks >= 30:
    print ("C")
else:
    print ("F")


    #Multiple if Statements in Succession
  #Already done before

  #Logical Operators
green = 20
Nepali = False
if green >=18 and Nepali:
    print("can vote")
elif green < 18 and Nepali:
    print ("Yoo young ")
elif not Nepali:
    print( "Leave Nepal as fast as possible")

