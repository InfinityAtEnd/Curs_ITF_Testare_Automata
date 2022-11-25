# TEMA 6 - OOP - Clase si Obiecte

# ATENTIE - pentru exercitiile care necesita imput de la user, anulati comenturile(caracterul "#") de la toate liniile de cod
# 			doar pentru exercitiul pe care doriti sa-l verificati.
###################################################################################
# Diferite importuri necesare
# from math import pi
# from datetime import date
# from tabulate import tabulate

###################################################################################

# Exercitii Recomandate - done

###################################################################################
# Exercitii obligatorii - grad de dificultate: Usor spre Mediu
###################################################################################

# 1.
# class Cerc:  # anulati comentul de la importul lui pi - linia 7
# 	def __init__(self, raza, culoare):
# 		self.raza = raza
# 		self.culoare = culoare
#
# 	def descrie_cerc(self):
# 		print(f'\tculoarea: {self.culoare}')
# 		print(f'\traza: {self.raza}')
#
# 	def aria(self):
# 		return pi * self.raza ** 2
#
# 	def diametru(self):
# 		return self.raza * 2
#
# 	def circumferinta(self):
# 		return 2 * pi * self.raza
#
# moneda = Cerc(2, 'bronz')
# soare = Cerc(190000000, 'orbitoare')
# print(f"Moneda are forma de cerc cu urmatoarele specificatii:")
# moneda.descrie_cerc()
# print(f"\taria: {moneda.aria()}")
# print(f"\tdiametrul: {moneda.diametru()}")
# print(f"\tcircumferinta: {moneda.circumferinta()}")
# print(f"Soarele are forma de cerc cu urmatoarele specificatii:")
# soare.descrie_cerc()
# print(f"\taria: {soare.aria()}")
# print(f"\tdiametrul: {soare.diametru()}")
# print(f"\tcircumferinta: {soare.circumferinta()}")

# 2.
# class Dreptunghi:
# 	def __init__(self, lungime, latime, culoare):
# 		self.lungime = lungime
# 		self.latime = latime
# 		self.culoare = culoare
#
# 	def descrie(self):
# 		print(f"Acesta este un dreptungi de culoare {self.culoare} avand lungimea {self.lungime} si latimea {self.latime}")
#
# 	def aria(self):
# 		print(f"Aria dreptunghiului este: {self.latime * self.lungime}")
#
# 	def perimetru(self):
# 		print(f"Perimetrul dreptunghiului este: {self.latime * 2 + self.lungime * 2}")
#
# 	def schimba_culoarea(self, noua_culoare):
# 		self.culoare = noua_culoare
#
# usa = Dreptunghi(200,60,'Zaffre')
# stadion = Dreptunghi(100,45,'verde')
# usa.descrie()
# usa.aria()
# usa.perimetru()
# stadion.descrie()
# stadion.aria()
# stadion.perimetru()
# stadion.schimba_culoarea('maro')
# stadion.descrie()

# 3.
# class Angajat:
# 	def __init__(self, nume, prenume, salariu):
# 		self.nume = nume
# 		self.prenume = prenume
# 		self.salariu = salariu
#
# 	def descrie(self):
# 		print(f"Angajatul {self.nume} {self.prenume} castiga {self.salariu} pe luna.")
#
# 	def nume_complet(self):
# 		print(f"Numele complet al angajatului este: {self.nume} {self.prenume}")
#
# 	def salariu_lunar(self):
# 		print(f"Angajatul castiga {self.salariu} lunar")
#
# 	def salariu_anual(self):
# 		print(f"Angajatul castiga {self.salariu * 12} anual")
#
# 	def marire_salariu(self, procent):
# 		self.salariu += self.salariu * procent/100
# 		print(f"Salariul a fost marit cu {procent} procente si este acum {self.salariu}")
#
# ion = Angajat('Ion', 'Avasilicai', 1800)
# gheorghe = Angajat('Gheorghe', 'Dej', 2200)
# ion.descrie()
# ion.nume_complet()
# ion.salariu_lunar()
# ion.salariu_anual()
# gheorghe.descrie()
# gheorghe.nume_complet()
# gheorghe.salariu_lunar()
# gheorghe.salariu_anual()
# gheorghe.marire_salariu(50)
# gheorghe.descrie()

# 4.
# class Cont:
# 	def __init__(self, iban, titular_cont, sold):
# 		self.iban = iban
# 		self.titular_cont = titular_cont
# 		self.sold = sold
#
# 	def afisare_sold(self):
# 		print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.")
#
# 	def debitare_cont(self, suma):
# 		if suma > self.sold:
# 			print(f"Sorry! Nu poti retrage mai mult decat ai.")
# 		elif suma <= 0:
# 			print(f"Sorry! Nu poti retrage o suma egala sau mai mica decat 0")
# 		else:
# 			self.sold -= suma
# 			print(f"Tocmai ai retras {suma} lei. Nu cumparata de toti bani acadele!")
#
# 	def creditare_cont(self, suma):
# 		if suma <= 0:
# 			print(f"Sorry! Nu poti depune o suma negativa sau egala cu 0")
# 		else:
# 			self.sold += suma
# 			print(f"Contul tau tocmai a fost incarcat cu inca {suma} lei.")
#
# al_meu = Cont('RO2000', 'Marian Laurentiu', 10)
# al_sotiei = Cont('RO2002', 'Pacostea Mea', 10000)
# al_meu.afisare_sold()
# al_meu.debitare_cont(2)
# al_meu.creditare_cont(5)
# al_meu.afisare_sold()
# al_sotiei.afisare_sold()
# al_sotiei.debitare_cont(1000000) # este foarte cheltuitoare
# al_sotiei.creditare_cont(0) # atat merita sa ii 'transfer' :)
# al_sotiei.afisare_sold()

###################################################################################
# Exercitii optionale - grad de dificultate: Mediu spre greu: may need Google
###################################################################################

# 1.
# class Factura:  # anulati comentul de la liniile 8 si 9... import datetime si import tabulate
# 	seria = 'F2FIG004'
# 	def __init__(self, numar, nume_produs, cantitate, pret_buc):
# 		self.numar = numar
# 		self.nume_produs = nume_produs
# 		self.cantitate = cantitate
# 		self.pret_buc = pret_buc
#
# 	def schimba_cantitatea(self, cantitate):
# 		self.cantitate = cantitate
#
# 	def schimba_pretul(self, pret):
# 		self.pret_buc = pret
#
# 	def schimba_nume_produs(self, nume):
# 		self.nume_produs = nume
#
# 	def genereaza_factura(self): # install package tabulate si from tabulate import tabulate
# 		print(f"Factura seria {self.seria} numar {self.numar}")
# 		print(f"Data: {date.today()}")
# 		print(tabulate([[self.nume_produs, self.cantitate, self.pret_buc, self.pret_buc * self.cantitate]],
# 					   headers=['Produs', 'cantitate', 'pret bucata', 'Total']))
#
# emag = Factura(10112022, 'Bilute colorate', 250, 0.5)
# metro = Factura(2233451, 'Apa Plata 2l', 30, 2.68)
# emag.genereaza_factura()
# print()
# metro.genereaza_factura()
# print()
# emag.schimba_cantitatea(600)
# emag.schimba_pretul(10)
# emag.schimba_nume_produs('Sine de tren din lemn')
# emag.genereaza_factura()


# 2.
# class Masina:
# 	culoare = 'gri'
# 	viteza_actuala = 0
# 	culori_disponibile = {'alb', 'albastru', 'rosu', 'negru', 'galben', 'verde'}
# 	marca = 'Dacia'
# 	inmatriculate = False
# 	def __init__(self, model, viteza_maxima):
# 		self.model = model
# 		self.viteza_maxima = viteza_maxima
#
# 	def descrie(self):
# 		print(f"Masina marca {self.marca}, model {self.model}, culoare {self.culoare}, viteza maxima "
# 			  f"{self.viteza_maxima}, status inmatriculare {self.inmatriculate}, merge cu {self.viteza_actuala} km/h")
#
# 	def inmatriculare(self):
# 		if self.inmatriculate == True:
# 			print(f"Masina este deja inmatriculata!")
# 		else:
# 			self.inmatriculate = True
# 			print(f"Masina a fost inmatriculata cu success")
#
# 	def vopseste(self, culoare):
# 		assert culoare in self.culori_disponibile, f"Culoarea aleasa nu se afla in lista noastra!"
# 		self.culoare = culoare
#
# 	def accelereaza(self, viteza):
# 		assert viteza > 0, f"Nu poti accelera cu o viteza negativa!"
# 		if viteza >= self.viteza_maxima:
# 			self.viteza_actuala = self.viteza_maxima
# 		else:
# 			self.viteza_actuala = viteza
#
# 	def franeaza(self):
# 		self.viteza_actuala = 0
# 		print(f"Masina s-a oprit!")
#
# my_car = Masina('MCV', 180)
# my_car.descrie()
# my_car.vopseste('negru')
# my_car.inmatriculare()
# my_car.accelereaza(80)
# my_car.descrie()
#
# your_car = Masina('Duster', 220)
# your_car.descrie()
# your_car.accelereaza(-10)

# 3.
# class TodoList:
# 	todo = {}
#
# 	def adauga_task(self, nume, descriere):
# 		self.todo[nume] = descriere
#
# 	def finalizeaza_task(self, nume):
# 		if nume not in self.todo.keys():
# 			print(f"Task-ul {nume} nu se afla in lista Todo")
# 		else:
# 			self.todo.pop(nume)
#
# 	def afiseaza_todo_list(self):
# 		print(f"Task-urile ramase sunt: ", end='')
# 		print(', '.join(self.todo.keys()))
#
# 	def afiseaza_detalii_suplimentare(self, nume_task):
# 		if nume_task in self.todo.keys():
# 			print(f"Detaliile suplimentare alea task-ului {nume_task} sunt: {self.todo[nume_task]}")
# 		else:
# 			user_choice = input((f"Acest task nu este in lista Todo! Doriti sa il adaugam in lista?(y/n) "))
# 			if user_choice.lower() == 'y':
# 				description = input(f"Te rog introdu descrierea pentru noul task! : ")
# 				self.todo[nume_task] = description
#
#
# dream_plan = TodoList()
# dream_plan.adauga_task('activitate zilnica', 'sa invat programare OOP')
# dream_plan.adauga_task('in fiecare seara', 'sa rezolv cu success task-urile primite')
# dream_plan.afiseaza_todo_list()
# dream_plan.afiseaza_detalii_suplimentare('dezvoltare profesionala')
# dream_plan.finalizeaza_task('test')
# dream_plan.finalizeaza_task('in fiecare seara')
# dream_plan.afiseaza_todo_list()
