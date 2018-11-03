# definizione di varie fuzioni

#Gioco di snake
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


#varie prove I/O e varie utilizzi di liste
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



#Calcolo dell' n-esimo numero della sequenza di Fibonacci
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

#matematica
def matematica():
	"""
	min() – questa funzione restituisce il valore minimo all’interno di una sequenza o una lista di numeri
	max() – questa funzione restituisce il valore massimo all’interno di una sequenza o una lista di numeri
	abs() – calcola il valore assoluto di un numero
	round() – questa funzione arrotonda il numero per un certo numero di cifre decimali
	sum() – calcola la somma di una lista di numeri
	"""

	n1 = min(1,5,0,3,4,6)
	print(n1)
	n2 = max([1,5,0,3,4,6])
	print(n2)
	n3 = abs(-12)
	print(n3)
	n4 = round(3.145,1)
	print(n4)
	n5 = sum([1.3,5.2,-0.6,3.1,4.4,6.9])
	print(n5)

import math as m
def rad(y):
	"""
	HELP:
		This function return the square root of input parameter
	"""
	return m.sqrt(y)


# fuzione con gestione di eccezioni
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


#generare numeri random
def randomiz():
	import random as r
	for i in range(10):
		print(r.randint(1,100))

	#oppure singola funzione solo
	from random import randint
	print(randint(1,120))

#lettura e scrittura su file .txt
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

#utilizzo di dizonari
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

def setExample():
	set1 = set()
	set1.add(1)
	set1.add(4)
	set1.add(6)
	print(set1)
	print(set1.pop())
	print(set1)
	set1.remove(6)
	print(set1)

	set2 = set(["“Uno”","”Due”","”Tre”"])
	print(3 in set1)
	print("“Uno”" in set2)

	#operazione su set
	A = {1,4,6,3}
	B = {4,5,9,2}
	print(A | B) # 1 2 3 4 5 9
	print(A & B) # 4
	print(A - B) # 1 3 6
	print(A ^ B) # 1 2 3 5 6 9

#utilizzo liste
def lista():
	lista = [9,8,7,6,5,4,3,2,1]
	print(lista[1-5])
	print(lista[1:-2])
	print(lista[::-1])
	print(lista[1:6:2])
	import random
	lista = [i**2 for i in range(random.randint(5,39)) if i**2 % 2 == 0]
	print(lista)

	#all() restituirà True solo se tutti gli elementi soddisferanno tale condizione
	#any() è sufficiente che almeno uno la soddisfi
	lista = [33,14,22,64,36]
	if all([i > 10 for i in lista]):
		print("Tutti i numeri sono maggiori di 10")

	if any([i > 50 for i in lista]):
		print("Nella lista ci sono elementi maggiori di 50")


	#La funzione enumerate() per effettuare un’iterazione per tutti gli elementi di una lista,
	# avendo sia gli indici che i valori come variabili da gestire.

	lista = [33,14,22,64,36]
	for i in enumerate(lista):
		print(i[0],i[1])

	def incrementa(x):
		return x + 1

	print("\nfumzione map e filter\n")
	lista = [2,6,12,3,5]
	#map riceve una funzione e un obj iterabile e appica la funzione a ogni elemento
	res = list(map(incrementa,lista))
	print(res)
	ris=list(filter(lambda y: y<5,lista))
	print(ris)
		

#utilizzo stringhe
def string():

	num1 = 12
	num2 = 24
	msg = "Il numero {0} è la metà di {1}".format(num1, num2)
	print(msg)

	msg1 = "Il mio nome è {name} e il mio cognome {surname}".format(name=7,surname=5)
	print(msg1)

	"""
	join() – concatena una lista di stringhe con un carattere separatore
	replace() – sostituisce una substringa con un’altra
	startswith() – verifica se la stringa inizia con una particolare sequenza di caratteri
	endswith() – verifica se la stringa finisce con una particolare sequenza di caratteri
	upper() – converte tutti i caratteri della stringa in maiuscolo
	lower() – converte tutti i caratteri della stringa in minuscolo
	split() – suddivide una stringa in una lista di stringhe in corrispondenza di un carattere separatore
	
	"""

	str1 = ",".join(["Uno","Due","Tre"])
	print(str1)

	str2 = "Questa è bella".replace("Questa","Quella")
	print(str2)

	bool1 = "Questa è una frase".startswith("Questa")
	print(bool1)

	bool2 = "Questa è una frase".endswith("frase")
	print(bool2)

	str3 = "Frase in maiuscolo".upper()
	print(str3)

	str4 = "FRASE IN MINUSCOLO".lower()
	print(str4)

	lista = "Uno,Due,Tre".split(",")
	print(lista)


def decoratore(func):
	def wrap():
		print("Estensione della funzione originale")
		func()
	return wrap

@decoratore
def saluta():
	print("Hello World!")
	deco = decoratore(saluta)




def fattoriale(fact):
	if fact == 1:
		return 1
	else:
		return fact*fattoriale(fact-1)

def is_even(x):
	if x == 0:
		return True
	else:
		return is_odd(x-1)

def is_odd(x):
	return not is_even(x)
	print(is_odd(23))


def iterator():
	from itertool import count
	for i in count(4):
		if i > 10:
			break
		print(i)
		#La funzione count() comincia a contare da un determinato valore.
		#La funzione cycle() effettua una iterazione infinita su di un oggetto iterable
		#La funzione repeat() ripete un oggetto, sia infinte volte che per un determinato valore di volte.
		#takewhile() – prende gli elementi di un oggetto iterabile finchè una funzione predicato rimane True
		#chain() – combina diversi oggetti iterabili in un’unico oggetto iterabile
		#accumulate() – restituisce il numero totale di valori in un oggetto iterabile.

	from itertools import accumulate, takewhile, chain
	lista1 = list(accumulate(range(7)))
	print(lista1)
	lista2 = list(takewhile(lambda x: x<5, lista1))
	print(lista2)
	print(list(chain(lista1,lista2)))

	#procuct() prodotto cartesiano
	#permutation() combinazioni o permutazioni
	from itertools import permutations, product
	lettere = ("A","B","C")
	prodotto = list(product(lettere,lettere))
	combinazioni = list(permutations(lettere))
	print(prodotto)
	print(combinazioni)






def classi():

	#esempio auto
	class Auto:
		nazione = "Italia"
		def __init__(self,colore,prezzo):
			self.colore = colore
			self.prezzo = prezzo

		def compra(self):
			print("L'auto {0} è tua per {1} euro".format(self.colore,self.prezzo))


	bmw = Auto("rosso",40000)
	panda = Auto("verde", 6000)

	print(bmw.colore)
	print(panda.prezzo)

	print(bmw.nazione)
	bmw.compra()



	class Figura:
		def __init__(self,colore,area):
			self.colore = colore
			self.area = area

		def assegna(self):
			print("“Sono una figura”")

		

	class Triangolo(Figura):
		def assegna(self):
			print("“Sono un triangolo”") 

	class Quadrato(Figura):
		def assegna(self):
			print("“Sono un quadrato”")
			super().assegna()	
	
	scaleno = Triangolo("rosso",120)
	quadro = Quadrato("giallo",16)
	quadro.assegna()
	print(quadro.colore)

	scaleno.assegna()
	print(scaleno.colore)



	#metodi classmethod per cambiare numero paramentri
	class Rectangle:
		def __init__(self, width, height):
			self.width = width
			self.height = height

		def calculate_area(self):
			return self.width * self.height 

		@classmethod
		def new_square(cls, side_length):
			return cls(side_length, side_length)

	#esempio costruttore quadraro solo con paramereo lato		
	square = Rectangle.new_square(5)
	print(square.calculate_area())


	class Pizza:
		def __init__(self, toppings):
			self.toppings = toppings

		@property
		def pineapple_allowed(self):
			return False

		@staticmethod
		def validate_topping(topping):
			if topping == "pineapple":
				raise ValueError("No pineapple")
			else:
				Trueingredients = ["cheese","onions","tomato"]
				return Trueingredients


	ingredients = ["cheese","onions"]
	#controllo prima di una nuova istanziazione con metodo static
	if all(Pizza.validate_topping(i) for i in ingredients):
		Pizza = Pizza(ingredients)

	#pizza = Pizza(["cheese","tomato"])
	print(Pizza.pineapple_allowed)		
	Pizza.pineapple_allowed = True


#MAIN
scelta = 1
while (scelta != 0 ):
	
	scelta = input("\n\n\n\nCosa vuoi fare?\n  1) Fibonacci & Matematica\n  2) Classi\n  3) Divisione\n  4) Liste\n  5) Rand\n  6) File\n  7) Dizionari & Set\n  8) Stringhe\n  9) Decoratori\n 10)itertools\n  99)Snake\n  0) Esci\n\nScelta: ")
	scelta = int(scelta)
	assert (scelta <= 10 or scelta == 99), "scelta non valida"

	if(scelta == 1):
		print("\n"+fibonacci.__doc__)
		input()
		x = input("Inserire n-esimo numero di interesse per Fibonacci: ")
		x = int(x)
		print("\nRisultato: " + str(fibonacci(x)))
		input()

		print("\n"+rad.__doc__)
		input()
		y = input("Radice quadrata di: ")
		y = int(y)
		ris = str(rad(y))
		print("\n\nRisutato: " + ris)
		input("")
		matematica()
		fact = input("inserire intero per il calcolo del fattoriale: ")
		fact = int(fact)
		print(fattoriale(fact))
		print(is_even(23))

	elif(scelta == 2):
		classi()

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
		print("\nE ora i set\n")
		setExample()

	elif(scelta == 8):
		string()

	elif(scelta == 9):
		saluta()

	elif(scelta == 10):
		iterator()
			
	elif(scelta == 99):
		snake()

	else:
		print("\nArrivederci!")




