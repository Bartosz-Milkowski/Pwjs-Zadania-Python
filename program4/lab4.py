#-*-coding: utf-8 -*-
#Bartosz Miłkowski
#mb41449
#31B
#Zadanie na ocenę 5
import collections as col
import operator
import sys
print ("Podaj numer zadania: 1 lub 2")
zad = str(raw_input())
if zad == "1":
	print ("Podaj nazwę pliku dla histogramu")
	plik = str(raw_input())
	#otwarcie pliku, jeżeli nie ma pliku o danej nazwie to błąd
	try:
       		f = open(plik,"r")
	except IOError:
        	print ("Nie mozna otworzyc pliku")
		sys.exit()
	# jeżeli plik otwarty
	if f.mode == "r":
		zawart = f.read() #czytaj zawartość
		zawartosc = zawart.upper()
		dl = 0
		czestosc = {}
		for i in zawartosc: #zlicz występowanie liter alfabetu
			if i.isalpha() == True:
				dl += 1
			if i in czestosc:
				czestosc[i] += 1
			else:
				czestosc[i] = 1
		# posortuj elementy po ilości występowań
		posortowane = sorted(czestosc.items(), key=operator.itemgetter(1), reverse = True)
		histogram = col.OrderedDict(posortowane)
		for k in histogram: # wypisz dane histogramu
			if k.isalpha():
				print(k + "  "),
				print(histogram[k]),
				print(" "),
				print("%.3f" % float(float(histogram[k])/float(dl)) + "%")
	f.close()
elif zad == "2":
	#otwarcie pliku, jeżeli nie ma pliku o danej nazwie to błąd
	try:
       		f = open("plik.txt","r")
	except IOError:
        	print ("Nie mozna otworzyc pliku")
		sys.exit()
	# jeżeli plik otwarty
	if f.mode == "r":
		dl = 0
		zawartosc1 = f.read() #czytaj zawartość
		nag = zawartosc1[:26] # podziel zawartość na pierwszą linie z literami i resztę tekstu
		tresc = zawartosc1[26:]
		wzor = list()
		czestosc = {}
		for i in tresc:
			if i.isalpha() == True:
				dl += 1
			if i in czestosc: #zlicz występowanie liter alfabetu
				czestosc[i] += 1
			else:
				czestosc[i] = 1
		# posortuj elementy po ilości występowań
		posortowane = sorted(czestosc.items(), key=operator.itemgetter(1), reverse = True)
		histogram = col.OrderedDict(posortowane)
		j=0
		# uzupenij listę histogramem występowania zaszyfrowanych liter
		for k in histogram:
			if k.isalpha():
				wzor.append(k)
				j +=1
		# dla treści pliku wypisz alfabet lub inny znak
		for i in tresc:
			if i.isalpha():
				poz = 0
				for k in wzor:
					if i == k : # jeżeli litera z tekstu równa literze w wzorze to pisz odpowiadającą jej literę z nag
						ind = wzor.index(k)
						sys.stdout.write(nag[ind])
			else:
				sys.stdout.write(i)

	f.close()
else:
	print ("Podano zły numer")

