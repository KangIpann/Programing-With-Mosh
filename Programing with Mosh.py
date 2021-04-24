# Bikin Engine Car Games
# Programing with Mosh
command = ""
started = False
max_start = 2
max_stop = 2
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print('Car is already started!')
        else:
            started = True
            print('Car Started...')
    elif command == 'stop':
        if not started:
            print('Your car is already stopped!')
        else:
            started = False
            print('Car Stopped')
    elif command == 'help':
        print('''
type 'start' to start the car
type 'stop' to stop the car
type 'quit' to quit from apps
        ''')
    elif command == 'quit':
        break
    else:
        print("I don't understand")
