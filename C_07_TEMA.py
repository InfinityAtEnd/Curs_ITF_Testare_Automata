# TEMA 7 - OOP - Cei 4 Piloni
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):  # clasa abstracta
	PI = 3.14

	@abstractmethod
	def aria(self):
		pass

	def descrie(self):
		print('Cel mai probabil am colturi')


class Patrat(FormaGeometrica):  # clasa copil al clasei FormaGeometrica
	def __init__(self, latura):
		self._latura = latura

	# setter
	def set_latura(self, lat):
		self._latura = lat

	# getter
	def get_latura(self):
		return self._latura

	# deleter
	def delete_latura(self):
		del self._latura
		print('Latura patratului a fost stearsa!') # afisaj pentru a confirma stergerea laturei

	def aria(self):
		return self._latura ** 2


class Cerc(FormaGeometrica):
	def __init__(self, raza):
		self._raza = raza

	# setter
	def set_raza(self, raza):
		self._raza = raza

	# getter
	def get_raza(self):
		return self._raza

	# deleter
	def delete_raza(self):
		del self._raza
		print('Raza cercului a fost stersa!') # afisaj pentru a confirma stergerea razei

	def aria(self):
		return self.PI * (self._raza ** 2)

	def descrie(self):
		print('Eu nu am colturi')


cap = Patrat(3)
fug_in = Cerc(2)
cap.descrie()
fug_in.descrie()
print(f"Latura Patratului este: {cap.get_latura()}")
print(f"Aria patratului este: {cap.aria()}")
print(f'Raza Cercului este: {fug_in.get_raza()}')
print(f"Aria Cercului este: {fug_in.aria()}")
print()
lat = int(input('Introdu valoare pentru latura Patratului: '))
raz = int(input('Introdu valoarea pentru raza cercului: '))
cap.set_latura(lat)
fug_in.set_raza(raz)
print(f"Latura Patratului este: {cap.get_latura()}")
print(f"Aria patratului este: {cap.aria()}")
print(f'Raza Cercului este: {fug_in.get_raza()}')
print(f"Aria Cercului este: {fug_in.aria()}")
print()
print('		Acum sa le stergem si obtinem: ')
print()
cap.delete_latura()
fug_in.delete_raza()
