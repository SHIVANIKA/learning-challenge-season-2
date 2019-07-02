//CAR GAME USING WHILE LOOP

command = ""
started = False
while True:
  command =  input( "> ").lower()
  if command == "start":
      if started:
          print("car already started")
      else:
          started = True
          print("car started ...")
  elif command ==  "stop":
      if not started:
          print("car is already stopped")
      else:
          started = False
          print("car stoped ....")
  elif command == "help":
    print("""
      to start = start
      to stop = stop
      to quit = quit

      """ )
  elif command == "quit":
    break
  else:
    print("sorry i did not understand")

//OUTPUT OF CARGAME
> start
car started ...
> start
car already started
> stop
car stoped ....
> stop
car is already stopped
> help

      to start = start
      to stop = stop
      to quit = quit

      
> quit

Process finished with exit code 0

