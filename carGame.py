command = ""

while command.lower() != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car Started")
    elif command == "stop":
        print("Car Stopped")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit 
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that.")