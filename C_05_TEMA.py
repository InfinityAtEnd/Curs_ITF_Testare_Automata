# TEMA 5 - Functii

# ATENTIE - pentru exercitiile care necesita imput de la user, anulati comenturile(caracterul "#") de la toate liniile de cod
# 			doar pentru exercitiul pe care doriti sa-l verificati.

###################################################################################

# Exercitii Recomandate - done

###################################################################################
# Exercitii obligatorii - grad de dificultate: Usor spre Mediu
###################################################################################
# 1.
# def my_sum(a, b):
# 	return a + b
#
# print(my_sum(4,7))

# 2.
# def parity_check(nr):
# 	if nr % 2 == 0:
# 		return True
# 	return False
#
# print(parity_check(5))
# print(parity_check(6))

# 3.
# def char_count(nume, prenume, nume_mijlociu=''):
# 	return (len(nume) + len(prenume) + len(nume_mijlociu))
#
# print(char_count('Marian', 'Laurentiu-Valentin', 'S'))

# 4.
# def arie_dreptunghi(lungime, latime):
# 	return lungime * latime
#
# print(arie_dreptunghi(4,5))

# 5.
# import math
# def arie_cerc(raza):
# 	return math.pi * (raza ** 2)
#
# print(arie_cerc(4))

# 6.
# def look_for_char(lake, duck):
# 	if duck in lake:
# 		return True
# 	return False
#
# print(look_for_char('Marian Laurentiu-Valentin', 'u'))
# print(look_for_char('Marian Laurentiu-Valentin', 'x'))

# 7.
# def count_upper_lower(phrase):
# 	lowers = 0
# 	uppers = 0
# 	nots = 0
# 	for letter in phrase:
# 		if letter.isupper():
# 			uppers += 1
# 		elif letter.islower():
# 			lowers += 1
# 		else:
# 			nots += 1
#
# 	print(f'Nr. de caractere lower case este {lowers}')
# 	print(f'Nr. de caractere upper case este {uppers}')
# 	print(f'Nr. de caractere nici lower nici upper case este {nots}')
#
# count_upper_lower('AnaaremereVladarepereEumanancciuc')
# count_upper_lower('Ana are mere, Vlad are pere, Eu mananc ciuc-*$%@')

# 8.
# def extract_positive_numbers(in_list):
# 	out_list = []
# 	for number in in_list:
# 		if number >= 0:
# 			out_list.append(number)
# 	return out_list
#
# print(extract_positive_numbers([3, 6, -2, -5, 3, 0, 6, -2, -56]))

# 9.
# def whosdaboss(a,b):
# 	if a > b:
# 		print(f'Primul numar {a} este mai mare decat al doilea nr {b}')
# 	elif a < b:
# 		print(f'Al doilea nr {b} este mai mare decat primul nr {a}')
# 	else:
# 		print('Numerele sunt egale')
#
# whosdaboss(4,8)
# whosdaboss(5,2)
# whosdaboss(1,1)

# 10.
# def insert_number(drawer, shirt):
# 	if shirt not in drawer:
# 		print('am adaugat numarul nou in set')
# 		return True
# 	else:
# 		print('nu am adaugat numarul in set. Acesta exista deja')
# 		return False
#
# print(insert_number([1,2,3,4,5], 6))
# print(insert_number([1,2,3,4,5], 2))


###################################################################################
# Exercitii optionale - grad de dificultate: Mediu spre greu: may need Google
###################################################################################

# 1.
# from calendar import monthrange
#
# def get_month_days(month):
# 	return monthrange(2022, month)[1]
#
# # se introduce luna ca numar: 1 ptr Ianuarie, 2 ptr Februarie......12 pentru Decembrie
# print(get_month_days(11))

# 2.
# def calculator(a, b):
# 	return (a+b, a-b, a*b, a/b)
#
# a, b, c, d = calculator(10, 2)
# print(f"Suma: {a}")
# print(f"Diferenta: {b}")
# print(f"Inmultirea: {c}")
# print(f"Impartirea: {d}")

# 3.
# def counting_numbers(l):
# 	rez = {}
# 	for i in range(10):
# 		rez[i] = l.count(i)
# 	return rez
#
# print(counting_numbers([1, 3, 1, 5, 9, 7, 7, 5, 5]))

# 4.
# def find_max(a, b, c):
# 	return max(a,b,c)
#
# print(find_max(1,3,2))

# 5.
# def calc_of_sum(number):
# 	rez = 0
# 	for i in range(number + 1):
# 		rez += i
# 	return rez
#
# print(calc_of_sum(3))


###################################################################################
# Exercitii optionale - Bonus
###################################################################################

# 1.
# METODA 1 - VERIFICARE DETALIATA
# def find_com(l1,l2):
# 	l3 = []
# 	for nr in l1:
# 		if nr in l2 and nr not in l3: # verificam fiecare elem din lista 1 daca este si in lista 2 si daca nu a fost adaugat deja pentru a nu avea duplicate
# 			l3.append(nr)
# 	for nr2 in l2:
# 		if nr2 in l1 and nr2 not in l3: # verificam fiecare elem din lista 2 daca este si in lista 1 si daca nu a fost adaugat deja pentru a nu avea duplicate
# 			l3.append(nr2)
# 	return l3
#
# # METODA 2 - MAI PUTIN COD
# def find_com2(l1, l2):
# 	return list(set(l1).intersection(l2))
#
# print(find_com([1,1,2,3], [2,2,3,4]))  # test METODA 1
# print(find_com2([1,1,2,3], [2,2,3,4]))  # test METODA 2

# 2.
# def aplicare_reducere(pret, reducere=0):
# 	if reducere > 100:
# 		print(f'Nu se poate aplica o reducere mai mare de 100%, frumoasa incercare si drept rasplata iti dublam pretul!')
# 		return pret*2
# 	elif reducere < 0:
# 		print(f'Nu se poate aplica o reducere mai mica decat 0, asta ar insemna sa iti crestem pretul. Dar daca insisti, poftim un pret dublu!')
# 		return pret*2
# 	else:
# 		return pret*(1 + reducere/100)
#
# print(aplicare_reducere(100,10))
# print(aplicare_reducere(100,50))
# print(aplicare_reducere(100,-5))
# print(aplicare_reducere(100,110))

# 3.
# pentru timezones: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# from datetime import datetime, date
# import pytz
#
# def afisare_data_ora_RO():
# 	ro_timezone = pytz.timezone('Europe/Bucharest')
# 	ro_date = date.today()
# 	ro_time = datetime.now().strftime("%H:%M:%S")
# 	print(f'Romania')
# 	print(f'Timezone: {ro_timezone}')
# 	print(f'Data: {ro_date}')
# 	print(f'Ora: {ro_time}')
#
# def afisare_data_ora_CH():
# 	ch_timezone = pytz.timezone('Asia/Shanghai')
# 	ch_date = pytz.datetime.date.today()
# 	ch_time = datetime.now(ch_timezone).strftime("%H:%M:%S")
# 	print(f'China')
# 	print(f'Timezone: {ch_timezone}')
# 	print(f'Data: {ch_date}')
# 	print(f'Ora: {ch_time}')
#
# afisare_data_ora_RO()
# afisare_data_ora_CH()

# 4.
# from datetime import date
#
# def bday_counting(year, month, day):
# 	bday = date(year,month,day)
# 	current_day = date.today()
# 	left = bday - current_day
# 	print(f'Astazi suntem in data de {current_day}, ziua ta este abia in data de {bday}, deci mai ai de asteptat inca {left.days} zile.')
#
# def x_mas_counting():
# 	x_mas_day = date(date.today().year, 12, 25)
# 	current_day = date.today()
# 	left = x_mas_day - current_day
# 	print(f'Astazi suntem in data de {current_day}, craciunul este abia in data de {x_mas_day}, deci mai ai de asteptat inca {left.days} zile.')
#
# bday_counting(2023,10,4)
# x_mas_counting()
