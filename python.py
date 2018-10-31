def snake():
    # SNAKES GAME
    # Use ARROW KEYS to play, SPACE BAR for pausing/resuming and Esc Key for exiting

    import curses
    from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
    from random import randint


    curses.initscr()
    win = curses.newwin(20, 60, 0, 0)
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)

    key = KEY_RIGHT                                                    # Initializing values
    score = 0

    snake = [[4,10], [4,9], [4,8]]                                     # Initial snake co-ordinates
    food = [10,20]                                                     # First food co-ordinates

    win.addch(food[0], food[1], '*')                                   # Prints the food

    while key != 27:                                                   # While Esc key is not pressed
        win.border(0)
        win.addstr(0, 2, 'Score : ' + str(score) + ' ')                # Printing 'Score' and
        win.addstr(0, 27, ' SNAKE ')                                   # 'SNAKE' strings
        win.timeout(150 - int(len(snake)/5 + len(snake)/10)%120)       # Increases the speed of Snake as its length increases
        
        prevKey = key                                                  # Previous key pressed
        event = win.getch()
        key = key if event == -1 else event 


        if key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
            key = -1                                                   # one (Pause/Resume)
            while key != ord(' '):
                key = win.getch()
            key = prevKey
            continue

        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
            key = prevKey

        # Calculates the new coordinates of the head of the snake. NOTE: len(snake) increases.
        # This is taken care of later at [1].
        snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

        # If snake crosses the boundaries, make it enter from the other side
        if snake[0][0] == 0: snake[0][0] = 18
        if snake[0][1] == 0: snake[0][1] = 58
        if snake[0][0] == 19: snake[0][0] = 1
        if snake[0][1] == 59: snake[0][1] = 1

        # Exit if snake crosses the boundaries (Uncomment to enable)
        #if snake[0][0] == 0 or snake[0][0] == 19 or snake[0][1] == 0 or snake[0][1] == 59: break

        # If snake runs over itself
        if snake[0] in snake[1:]: break

        
        if snake[0] == food:                                            # When snake eats the food
            food = []
            score += 1
            while food == []:
                food = [randint(1, 18), randint(1, 58)]                 # Calculating next food's coordinates
                if food in snake: food = []
            win.addch(food[0], food[1], '*')
        else:    
            last = snake.pop()                                          # [1] If it does not eat the food, length decreases
            win.addch(last[0], last[1], ' ')
        win.addch(snake[0][0], snake[0][1], '#')
        
    curses.endwin()
    print("\nScore - " + str(score))


def prova1():
	print ("Hello Word!")
	print ('hello giangi')

	print(3 + 4)
	print(3/2)
	print(2* -3)
	print(3**3)
	print("END")
	a = 0.333333

	print(a *3)

	s = " hello, my name's Gianluca. I'm 24"
	print (s)

	name = input("enter your name: ")

	s = "doo"*2
	print(name)

	a = "HELLO"; b = "HELLO"; c ="CIAO"

	print(a == b)
	print(a == c)

	if a != b :
		print ("ESATTOOOO")
	elif a == c:
		print ("SCEMOOOOO")
	else :
		print (3)


	list = 1,2,4
	print(list)

	lista = [1,2]
	print(lista)

	lista2 = [3,4]

	matrice = [[1,2,3],[4,5,6],[7,8,9]]

	print (matrice[2][2])

	print(a[0] + a[2])

	lista3 = lista2 + lista
	print(lista3)

	print ( not 2 in lista2)

	a = input(name + " inserisci un valore intero: ")
	a = int(a)
	lista = [0,1,2,3,4]
	if a in lista:
		print ("elemento presente")
	else:
		print(	"elemento non presente")

	#aggiungi alla lista
	lista.append(5)

	# inserire elemento (indice, elemento)
	lista.insert(3,8)

	print (lista)

	#trovare elemento in lista
	i = lista.index(3)

	#max e min
	max1 = max(lista)
	min1 = min(lista)


	#rimuovere elemento 3
	lista.remove(3)

	#ordinare lista
	lista.sort()

	print(lista)

	#contare elementi lista
	print (len(lista))

	#quante volte elemento è prensete in lista
	lista.count(8)

	#reverse lista
	lista.reverse()

	#lista che va da range specifico
	for i in range(4,12):
		print(i)


	lista2 = []
	print(lista)
	n = len(lista)-1
	i = 0
	while i < n :
		lista2.append(lista[i]*2)
		i+=1
	print(lista2)

	for i in range(5):
		print("a soreta")

	for item in lista:
		lista2.append(item)

	print(lista2)

	#assegno ad una variabile la funzione
	fib1 = fibonacci
	print(fib1(5))



	#funzioni passate per parametro
	def mix(a,b):
		return (a*b)/2

	def foo(func,x,y):
		return func(x,y)

	print(foo(mix,2,3))



#fibonacci
def fibonacci(x):
	"""	
	HELP:
		This function return the n-th numeber of Fibonacci's sequence
	"""
	i=1; n1=0; n2=1
	#print(n1 + n2)
	while i < x:
		n = n1 + n2
		#print(n)
		n1 = n2
		n2 = n
		i+=1
	return n2


import math as m
def rad(y):
	"""
	HELP:
		This function return the square root of input parameter
	"""
	return m.sqrt(y)


def trymode():
	"""
	HELP:
		This function return the divison by parameter a and b
	"""
	a = input("\nInserisci il primo numero: ")
	b = input("\nInserisci il secondo numero: ")
	try:
		a = int(a); b = int(b)
		print("\nRisultato: "+ a+"/"+b+" ="+ a/b)
	except Exception as e:
		print("Errore!")



def randomiz():
	import random as r
	for i in range(10):
		print(r.randint(1,100))

	#oppure singola funzione solo
	from random import randint
	print(randint(1,120))


def file():

	"""
		w – in scrittura (wrtiting)
		r – in lettura (reading)
		a – in append (aggiunge in fondo al programma)
		b – file binario
	"""

	myfile = open("filename.txt","r")
	testo = myfile.read()
	print(testo)

	#legge linea per linea
	testoline = myfile.readline()
	print(testoline)

	#oppure
	for line in myfile:
		print(line)

	#legge e mette in lista le linee
	content = myfile.readlines()
	print(content)

	myfile.close()

	try:
		file = open("file1.txt","w")
		file.write("Questo è il nuovo testo\n")
		numbit = file.write("Hello\n")
		print(numbit)
	finally:
		file.close()


def dizionari():
	diz = {"key1":"val", "casa":120000, 5:5}

	print(diz["casa"])
	print(diz[5])

	print("d" not in diz)
	print(diz.get("mainglia","errore non presente"))
	print(diz.get("casa","errore non presente"))

	#esistono pure le tuble NON modificabili
	tupla = (1,2,3)
	print(tupla[0])

	tupla1 = (1,(55,66,77),3,4)
	print(tupla1[1])
	print(tupla1[1][2])


def lista():
	lista = [9,8,7,6,5,4,3,2,1]
	print(lista[1-5])
	print(lista[1:-2])
	print(lista[::-1])
	print(lista[1:6:2])
	import random
	lista = [i**2 for i in range(random.randint(5,39)) if i**2 % 2 == 0]
	print(lista)


def string():

	num1 = 12
	num2 = 24
	msg = "Il numero {0} è la metà di {1}".format(num1, num2)
	print(msg)

	msg1 = "Il mio nome è {name} e il mio cognome {surname}".format(name=7,surname=5)
	print(msg1)

scelta = 1
while (scelta != 0 ):
	
	scelta = input("\n\n\n\nCosa vuoi fare?\n  1) Fibonacci\n  2) Radice Quadrata\n  3) Divisione\n  4) Liste\n  5) Rand\n  6) File\n  7) Dizionari\n  8) Stringhe\n  99)Snake\n  0) Esci\n\nScelta: ")
	scelta = int(scelta)
	assert (scelta <= 8 or scelta == 99), "scelta non valida"

	if(scelta == 1):
		print("\n"+fibonacci.__doc__)
		input()
		x = input("Inserire n-esimo numero di interesse per Fibonacci: ")
		x = int(x)
		print("\nRisultato: " + str(fibonacci(x)))
		input()

	elif(scelta == 2):
		print("\n"+rad.__doc__)
		input()
		y = input("Radice quadrata di: ")
		y = int(y)
		ris = str(rad(y))
		print("\n\nRisutato: " + ris)
		input("")

	elif(scelta == 3):
		print("\n"+trymode.__doc__)
		input()
		trymode()

	elif(scelta == 4):
		lista()

	elif(scelta == 5):
		randomiz()

	elif(scelta == 6):
		file()

	elif(scelta == 7):
		dizionari()

	elif(scelta == 8):
		string()

	elif(scelta == 99):
		snake()

	else:
		print("\nArrivederci!")





