#print("Hellow world")

print("Welcome to tip calculator!")
bill =float (input("what was the total bill? ₹"))
tip =int (input("what percentage tip would to give ? 10 12 15"))
people = int(input("how many people to split the bill ?"))
bill_with_tip = tip/100 * bill + bill
print (bill_with_tip)



