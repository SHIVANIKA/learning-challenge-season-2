//LISTS

names = ["shiva", "shivani" , "shivanika" ,"pravalika"]
names[0] = "siva"
print(names[0:3])
print(names[:])


// LIST CHALLENGE TO FIND MAXIMUM NUMBER

list = [10,20,70,67,90]
max = list[0]
for number in list:
    if number >max:
        max = number
print(max)


// 2D LISTS

matrix=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
]
print(matrix[0][2])
for row in matrix:
    for item in row:
        print(item)

//LIST METHODS

numbers = [4,8,9,2,4,6]
numbers.append(20)
numbers.insert(0,5)
numbers.remove(9)
numbers.pop()
numbers.sort()
numbers.reverse()
print(numbers)

number1 = [7,5,5,3,1]
uniques = []
for number in number1:
    if number not in uniques:
        uniques.appemd(number)
print(uniques)


//OUTPUT OF LISTS
['siva', 'shivani', 'shivanika']
['siva', 'shivani', 'shivanika', 'pravalika']

//OUTPUT OF MAXIMUM NUMBER
90

//OUTPUT OF 2D LISTS
3
1
2
3
4
5
6
7
8
9

//OUTPUT OF LISTMETHODS
[8, 5, 4, 4, 2]

Process finished with exit code 1

