print("Welcome to roller coaster")
height = int (input("what is your height"))

if height  >= 120:
    print("you can ride roller coaster")
    age =int (input("what is your age"))
    if age <=12 :
        print("child ticket price : ₹20")
    elif age <=18 :
        print("youth ticket price : ₹50 ")
    else :
        print("Adult ticket price : ₹100") 
    input("Do you want to have a  photo take ? Type y for yes and n for No . ")     
else :
        print("sorry you have grow taller to ride")