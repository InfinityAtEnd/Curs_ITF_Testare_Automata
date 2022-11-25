# TEMA 3 - Structuri de date

# ATENTIE - pentru exercitiile care necesita imput de la user, anulati comenturile(caracterul "#") de la toate liniile de cod
# 			doar pentru exercitiul pe care doriti sa-l verificati.

###################################################################################

# Exercitii Recomandate - done

###################################################################################
# Exercitii obligatorii - grad de dificultate: Usor spre Mediu
###################################################################################

# 1.
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(f'Notele muzicale sunt: {note_muzicale}')
note_muzicale = note_muzicale[::-1]
print(f'Notele muzicale inversate prin slicing sunt: {note_muzicale}')
note_muzicale.reverse()
print(f'Notele muzicale inversate prin motoda reverse() sunt: {note_muzicale}')

# 2.
do_appearences = note_muzicale.count('do')
print(f'Nota "do" apare in lista de note muzicale de {do_appearences} ori.')

# 3.
list01 = [3, 1, 0, 2]
list02 = [6, 5, 4]
# list01.extend(list02)  # VARIANTA 1 : folosind metoda extend()
lista_unita = list01 + list02 # VARIANTA 2 : folosim concatenarea listelor
print(f'Lista rezultata din unirea celor doua liste este: {lista_unita}')

# 4.
lista_unita.sort()
print(f'Lista unita sortata este: {lista_unita}')
lista_unita.remove(0)
print(f'Lista unita dupa eliminarea lui 0 este: {lista_unita}')

# 5.
if len(lista_unita) > 0:
	print('Lista nu este goala.')
else:
	print('Lista este goala.')

# 6.
lista_unita.clear()

# 7.
if len(lista_unita) > 0:
	print('Lista nu este goala.')
else:
	print('Lista este goala.')

# 8.
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(f'Elevi din dict1 sunt: {list(dict1.keys())}') # transformand in list se elimina notatia dict_keys(

# 9.
for key in dict1.keys():
	print(f'{key} a luat nota {dict1[key]}')

# 10.
dict1['Dorel'] = 6
print(f'Nota lui Dorel dupa contestatie este: {dict1["Dorel"]} ')

# 11.
# eliminare Gigel
dict1.pop('Gigel')
print(f'Elevul Gigel a parasit clasa!')
# adaugarea lui Ionica cu nota 9
dict1['Ionica'] = 9
print(f'Elevul Ionica s-a alaturat clasei!')
print(f'Structura clasei dupa cele doua transferuri este: {list(dict1.keys())}')

# 12.
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(f'Zilele saptamani sunt: {zile_sapt}')

# 13.
if weekend.issubset(zile_sapt):
	print(f'Weekend este un subset al zilelor din saptamanii.')
else:
	print(f'Weekend NU este un subset al zilelor din saptamanii.')

# 14.
diff_zile = zile_sapt.difference(weekend)
print(f'Diferenta dintre Weekend si zilele saptamani sunt zilele: {diff_zile}')

# 15.
inter_zile = zile_sapt.intersection(weekend)
print(f'Intersecta intre weekend si zilele saptamani sunt zilele: {inter_zile}')

###################################################################################
# Exercitii Optionale - grad de dificultate: Mediu spre greu _ may need google
###################################################################################
lista_jucatori = ['Gica', 'Popescu', 'Pepe', 'Bula', 'Mario']
swaps_max = 3  # selecteaza numarul maxim de schimbari
swaps_done = 0 # selecteaza numarul de schimbari DEJA efectuate
if swaps_done >= swaps_max:
	print(f'Imi pare rau dar aparent nu ai dreptul la schimbari') # in caz ca se selecteaza la swaps_done un numar mai mare sau egal cu  swaps_max
else:
	while swaps_done != swaps_max:
		print('#' * 100) # pentru a delimita o noua runda de schimbari !!!
		print(f'Jucatori actuali pe teren sunt: {lista_jucatori}')
		print(f'Mai ai dreptul la {swaps_max - swaps_done} schimbari!')
		player_to_pop = input('Introdu jucatorul care sa iasa( sau "q" pentru iesire): ')
		if player_to_pop == 'q':
			print('Iti multumim pentru participare!')
			break
		if player_to_pop not in lista_jucatori:
			print(f'Nu se poate efectua schimbarea deoarece jucatorul {player_to_pop} nu e in teren')
			print(f'Mai ai {swaps_max - swaps_done} schimbari.')
			continue
		else:
			swaps_done += 1
			lista_jucatori.remove(player_to_pop)
			player_to_add = input('Introdu jucatorul care sa intre pe teren( sau "q" pentru iesire): ')
			if player_to_add == 'q':
				print('Iti multumim pentru participare!')
				break
			lista_jucatori.append(player_to_add)
			print(f'Jucatorul {player_to_add} a intrat pe teren, jucatorul {player_to_pop} a iesit de pe teren, mai ai {swaps_max - swaps_done} schimbari. ')

		if swaps_done == swaps_max:
			print(f'Ti-ai folosit toate cele {swaps_max} schimbari!')
			print('Iti multumim pentru participare!')
