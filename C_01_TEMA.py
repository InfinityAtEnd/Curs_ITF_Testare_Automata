# Tema 1 Setup, Variabile, Tipuri de date

# ATENTIE - pentru exercitiile care necesita imput de la user, anulati comenturile(caracterul "#") de la toate liniile de cod
# 			doar pentru exercitiul pe care doriti sa-l verificati.

###################################################################################
# Exercitii Recomandate - grad de dificultate: Usor
# 1. Done
# 2. Done

# Exercitii obligatorii - grad de dificultate: Usor spre Mediu:

# 1
# variabila - este formata dintr-un nume unic caruia programul ii aloca o memorie si caruia i se atribuie o valoare

# 2
V1 = "aceasta este o variabila de tip string, v2 de tip int, v3 de tip float iar ultima(v4) de tip bool"
V2 = 22
V3 = 22.21
V4 = False

# 3
print(type(V1))
print(type(V2))
print(type(V3))
print(type(V4))

# 4
print("Rotunjire variabilei de tip float!")
v3 = round(v3)
print(type(v3))

# 5
print(f"Variabila de tip string contine urmatoarea valoare: {v1}")
print(f"Azi am fost la magazin sa-mi cumpar mere de {v2} lei.")
print(f"Cand am ajung la casa de marca a trebuit sa platesc exact {v3} lei.")
print(f"Caserita m-a intrebat daca vreau si sacosa. I-am raspuns ca {v4}! :)")

# 6
# numele = input("numele: ")
# prenumele = input("prenumele: ")
# print(f"{numele.capitalize()} {prenumele.capitalize()} are {len(numele) + len(prenumele)} caractere.")

# 7
# lungimea = int(input("lungimea: "))
# latimea = int(input("latimea: "))
# print(f"Aria dreptunghiului este {lungimea * latimea}.")

# 8 + 9
the_string = "Coral is either the stupidest animal or the smartest rock"
print(f"Cuvantul 'the' apare de {the_string.count('the')} ori.")

# 10
# assert the_string.isnumeric(), "String-ul oferit NU contine doar numere!"


###################################################################################
# Exercitii Optionale - grad de dificultate: Mediu spre greu(s-ar putea sa ai nevoie de Google).

# 1
# st = input("Introduceti un string de dimensiune impara: ")
# print(f"Caracterul din miljoc este: {st[int((len(st) - 1) / 2) ]}")

# 2
# assert un_string == un_string[-1], "Acest string NU este palindrom."

# 3
# vv = input("introduceti un string format din cel putin 2 cuvinte: ").split()
# for word in vv:
# 	print(word)

# 4
# vvv = input("introduceti un string pentru a capitaliza primul caracter: ")
# first_char = vvv[0]
# for i in range(1 , len(vvv) - 1):
# 	if vvv[i] == first_char:
# 		vvv = vvv[:i] + first_char.capitalize() + vvv[i+1:]
# print(f"Primul character este: {first_char} iar string-ul rezultat este: {vvv}")

# 5
# user = input("introduceti username-ul: ")
# password = input("introduceti password-ul: ")
# print(f"Parola pentru {user} este {'*' * len(password)} si are {len(password)} caractere.")






