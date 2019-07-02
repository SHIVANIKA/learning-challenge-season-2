//IF LOOP
CHALLENGE TO FIND HOT,COLD OR LOVELY DAY USING IF LOOP

is_hot = False
is_cold = False
if is_hot :
 print("It's a hot day ")
 print("drint plenty of water")
elif is_cold:
    print("it's a cold day")
    print("wear warm clothes")
else:
    print("it's a lovely day")

print("enjoy your day")


//CHALLENGE TO FIND HOUSE PRICE WITH IF LOOP
price_of_house = 1000000
is_goodcredit = True
if is_goodcredit:
    amount1 = price_of_house/ 10
    print(f"amount : {amount1}")

else:
    amount2 = price_of_house/20
    print(f"amout : {amount2}")


//CHALLENGE TO FIND LOAN ELGIBLE
has_high_income =True
has_good_credit = False
if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("not elgible")
has_high_income1 = True
has_good_credit1 = False
if has_high_income1 or has_good_credit1:
        print("Eligible for loan")
else:
    print("not elgible")

//CHALLENGE TO FIND LENGTH OF NAME
name = "shivanika"
if len(name)<3:
    print("name must be atleast of 3 characters")
elif len(name)>50:
    print("name can be maximum of 50 characters")
else:
    print("name looks good")

//CHALLENGE TO CONVERT WEIGHJTS USING INPUT AND IF LOOP 
weight = input("weight:")
unit = input("(L)bs or (K)g:")
if unit.upper() == 'L':
  converted= int( weight)*0.45
  print(f"you are {converted} kilos ")
else:
    converted = int(weight)/0.45
    print(f'you are { converted} pounds')





//OUTPUT OF FINDING DAY
it's a lovely day
enjoy your day

//OUTPUT OF HOUSE PRICE
 amount : 100000.0

//OUT OF LOAN ELGIBLE
not elgible
Eligible for loan

//OUT OF NAMES
name looks good

//OUT OF WEIGHT CONVERSION
weight:104
(L)bs or (K)g:L
you are 46.800000000000004 kilos 

Process finished with exit code 0
