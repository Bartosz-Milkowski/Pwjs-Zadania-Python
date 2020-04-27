#-*-coding: utf-8 -*-
#Bartosz Miłkowski
#mb41449
#31B
#Zadanie na ocenę 4
import os
import sys
print ("Podaj nazwe katalogu")
kat = str(raw_input())
#otwarcie pliku, jeżeli nie ma pliku o danej nazwie to bład
try:
	pliki = os.listdir(kat)
except IOError:
        print ("Nie można otworzyć katalogu")
	sys.exit()
except OSError:
        print ("Nie można otworzyć katalogu")
	sys.exit()
lista = []
sciezka = []
for plik in pliki:
	lista.append(plik)
lista2=lista
znajdz = 0
i=0
while i < len(lista):
	j = i + 1
	sciezka1 = "%s/%s" % (kat,lista[i])
	i = i + 1	
	if os.path.isfile(sciezka1):
	 	f = open(sciezka1,"rb")
		zawartosc1 = f.read()
		nazwa1 = f.name
		roz1 = os.stat(sciezka1).st_size
		f.close
		while j < len(lista2):
			sciezka2 = "%s/%s" % (kat,lista2[j])
			j = j + 1 
			if os.path.isfile(sciezka2):
				f2 = open(sciezka2,"rb")
				nazwa2 = f2.name
				zawartosc2 = f2.read()
				roz2 = os.stat(sciezka2).st_size
				if ((zawartosc1 == zawartosc2) and (roz1 == roz2)):
					print ("Zanaleziono duplikat:"),
					print ("(rozmiar:" + str(roz1) + "b)")
					print (sciezka1)
					print (sciezka2)
					znajdz = 1
				f2.close
if znajdz == 0:
	print ("Nie znaleziono duplikatów")

