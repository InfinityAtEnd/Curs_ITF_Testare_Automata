# TEMA 2 - Operatori, conditionale

# ATENTIE - pentru exercitiile care necesita imput de la user, anulati comenturile(caracterul "#")
# de la toate liniile de cod
# 			doar pentru exercitiul pe care doriti sa-l verificati.

###################################################################################

# Exercitii Recomandate - done

###################################################################################
# Exercitii obligatorii - grad de dificultate: Usor spre Mediu
###################################################################################

# 1. - if else - se creaza o conditie care, daca aceasta este adevarata(TRUE) se v-a
# executa blocul de cod
# intre if si else
#				iar daca conditia este falsa(FALSE) se v-a executa blocul de cod dupa else.
#				*** - ambele blocuri de cod au indent.

# # 2
# x = input("Introdu un numar pentru verificare: ")
# if x.isnumeric():
# 	print(f"Numarul {x} este un numar natural.")
# else:
# 	print(f"Numarul {x} NU este un numar natural.")

# 3.
# x = int(input("Introdu un numar pentru verificare: "))
# if x > 0:
# 	print(f"Numarul {x} este pozitiv.")
# elif x < 0:
# 	print(f"Numarul {x} este negativ")
# else:
# 	print(f"Numarul {x} este neutru")

# # 4.
# x = int(input("Introdu un numar pentru verificare: "))
# if x > -2 and x < 13:
# 	print(f"Numarul {x} este intre -2 si 13.")
# else:
# 	print(f"Numarul {x} NU este intre -2 si 13.")

# # 5.
# x = int(input("Introdu valoarea lui X: "))
# y = int(input("Introdu valoarea lui Y: "))
# if x-y < 5:
# 	print(f"Diferenta dintre {x} si {y} este mai mica de 5.")

# 6.
# x = int(input("Introdu un numar pentru verificare: "))
# if not (x > 5 and x < 27):
# 	print(f"Numarul {x} NU este intre 5 si 27.")

# 7.
# x = int(input("Introdu valoarea lui X: "))
# y = int(input("Introdu valoarea lui Y: "))
# if x == y:
# 	print(f"Numerele {x} si {y} sunt egale.")
# else:
# 	if x > y:
# 		print(f"Dintre numerele {x} si {y}, numarul {x} este mai mare.")
# 	else:
# 		print(f"Dintre numerele {x} si {y}, numarul {y} este mai mare.")

# 8.
# x = int(input("Introdu valoarea lui X: "))
# y = int(input("Introdu valoarea lui Y: "))
# z = int(input("Introdu valoarea lui Z: "))
# if x == y and y == z:
# 	print(f"Triunghiul cu laturile {x}, {y}, {z} este echilateral.")
# elif x == y or y == z or x == z:
# 	print(f"Triunghiul cu laturile {x}, {y}, {z} este isoscel.")
# else:
# 	print(f"Triunghiul cu laturile {x}, {y}, {z} este un triunghi oarecare.")

# 9.
# litera = input("Introdu o litera: ")
# if litera in 'aeiouAEIOU':
# 	print(f"Litera {litera} este o vocala.")
# else:
# 	print(f"Litera {litera} NU este o vocala.")

# 10.
# nota = int(input("Introdu o nota din sistemul romanesc: "))
# if nota >= 9:
# 	print(f"Nota {nota} este reprezentata prin nota A.")
# elif nota >= 8:
# 	print(f"Nota {nota} este reprezentata prin nota B.")
# elif nota >= 7:
# 	print(f"Nota {nota} este reprezentata prin nota C.")
# elif nota >= 6:
# 	print(f"Nota {nota} este reprezentata prin nota D.")
# elif nota > 4:
# 	print(f"Nota {nota} este reprezentata prin nota E.")
# else:
# 	print(f"Nota {nota} este reprezentata prin nota F.")


###################################################################################
# Exercitii Optionale - grad de dificultate: Mediu spre greu - might need Google.
###################################################################################

# 1.
# x = int(input("Introdu valoarea lui X: "))
# if len(str(x)) >= 4:
# 	print(f"Numarul {x} are {len(str(x))} cifre.")
# else:
# 	print(f"Numarul {x} nu are minim 4 cifre.")

# 2.
# x = int(input("Introdu valoarea lui X: "))
# if len(str(x)) == 6:
# 	print(f"Numarul {x} are exact 6 cifre.")
# else:
# 	print(f"Numarul {x} nu are exact 6 cifre.")

# 3.
# x = int(input("Introdu valoarea lui X: "))
# if x % 2 == 0:
# 	print(f"Numarul {x} este un numar par.")
# else:
# 	print(f"Numarul {x} este un numar impar.")

# 4.
# x = int(input("Introdu valoarea lui X: "))
# y = int(input("Introdu valoarea lui Y: "))
# z = int(input("Introdu valoarea lui Z: "))
# if x >= y:
# 	if x >= z:
# 		print(f"Dintre {x}, {y}, {z}, cel mai mare este: {x}.")
# 	else:
# 		print(f"Dintre {x}, {y}, {z}, cel mai mare este: {z}.")
# else:
# 	if y >= z:
# 		print(f"Dintre {x}, {y}, {z}, cel mai mare este: {y}.")
# 	else:
# 		print(f"Dintre {x}, {y}, {z}, cel mai mare este: {z}.")

# 5.
# x = int(input("Introdu valoarea lui X: "))
# y = int(input("Introdu valoarea lui Y: "))
# z = int(input("Introdu valoarea lui Z: "))
# if (x > 0) and (y > 0) and (z > 0) and (x + y > z) and (x + z > y) and (y + z > x):
# 	print(f"Numerele {x}, {y} si {z} formeaza un triunghi valid.")
# else:
# 	print(f"Numerele {x}, {y} si {z} NU formeaza un triunghi valid.")

# 6 + 7
# st = 'Coral is either the stupidest animal or the smartest rock'
# x = int(input("Introdu valoarea lui X: "))
# print(st[:len(st) - x])
# st_nou = st[:5] + st[-5:]
# print(st_nou)

# 8.
# st = 'Coral is either the stupidest animal or the smartest rock'
# word = 'rock'
# word_index = st.index(word)
# print(st[:word_index])

# 9.
# st = input("Introdu un string oarecare: ")
# assert st[0].capitalize() == st[-1].capitalize(), "Primul si ultimul caracter NU sunt la fel!!!"

# 10.
# string_number = '0123456789'
# print(f"Numerele pare sunt: {string_number[::2]}")
# print(f"Numerele impare sunt: {string_number[1::2]}")


###################################################################################
# Exercitii Bonus - may need google
###################################################################################
# 11. - Joc ghicit zarul
# import random
#
# dice_roll = random.randint(1,6)
# numar_ales = int(input("Ghiceste un numar intre 1 si 6: "))
# if numar_ales == dice_roll:
# 	print(f"Ai ghicit. Felicitari! Ai ales {numar_ales} si zarul a fost {dice_roll}")
# else:
# 	if numar_ales > dice_roll:
# 		print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_ales} dar zarul a fost {dice_roll}")
# 	else:
# 		print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {numar_ales} dar zarul a fost {dice_roll}")
