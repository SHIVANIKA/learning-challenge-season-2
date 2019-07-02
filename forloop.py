//FOR LOOP

price = [10,20,30]
total = 0
for item in price:
    total += item
print(f"total:{total}")

//NESTED LOOP TO FIND RANGE OF X AND Y COORDINATES

for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

//CHALLENGE OF NESTED LOOP TO PRINT OUTPUT
numbers = [5,2,5,2,2]
for x_count in numbers:
    output =""
    for count in range (x_count):
        output += "x"
    print(output)



// OUTPUT OF FOR LOOP
total:60

//OUTPUT OF X AND Y COORDINATES
(0,0)
(0,1)
(0,2)
(1,0)
(1,1)
(1,2)
(2,0)
(2,1)
(2,2)
(3,0)
(3,1)
(3,2)
(4,0)
(4,1)
(4,2)

//CHALLENGE OF NESTED LOOP TO PRINT THIS OUTPUT
xxxxx
xx
xxxxx
xx
xx

Process finished with exit code 0
