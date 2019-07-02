//EXAMPLE OF WHILE LOOP
i = 1
while i<= 5:

 print("*" * i)
 i = i+1
print("done")



//NUMBER GUESSING GAME USING WHILE AND IF LOOP

secret_number = 8
guess_count = 0
guess_limit = 3
SSwhile guess_count < guess_limit :
    guess =int(input("guess :"))
    guess_count += 1
    if guess == secret_number:
        print("you guessed number")
        break
else:
    print("you failed")


//OUTPUT OF WHILE LOOP
*
**
***
****
*****
done

//OUTPUT OF NUMBER GUESSING GAME
guess :4
guess :98
guess :8
you guessed number

Process finished with exit code 0
