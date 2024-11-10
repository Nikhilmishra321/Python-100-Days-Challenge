print("Welcome to roller coaster")
height = int (input("what is your height"))

if height  >= 120:
    print("you can ride roller coaster")
    age =int (input("what is your age"))
    if age <=12 :
        print("please pay ₹20")
    elif age <=18 :
        print("please pay ₹50 ")
    else :
        print("pay ₹100")  
else :
         print("sorry you have grow taller to ride")
   