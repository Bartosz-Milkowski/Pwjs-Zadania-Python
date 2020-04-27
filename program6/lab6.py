#-*-coding: utf-8 -*-
#Bartosz Miłkowski
#mb41449
#31B
#Zadanie na ocenę 5
import sys
import os
import pwd
import time
from stat import *

maks = len(sys.argv) - 1

j=1
operacje = 0
otw = 0
#sprawdzenie ile i jakie argumenty
if maks == 0:
	dane = os.listdir(".")
elif maks>3:
	print "Podano za dużo parametrów/argumentów\n"
	sys.exit()
else:
	while j != maks+1:
		if sys.argv[j] == '-l':	
			operacje = operacje + 1
		elif sys.argv[j] == '-L':
			operacje = operacje + 2
		#jeżeli w argumentach folder to go otwórz
		elif os.path.isdir(sys.argv[j]) and otw != 1:
			dane = os.listdir(sys.argv[j])
			fold =  sys.argv[j]
			otw = 1
		else:
			print "Podano nieprawidłowy parametr\n"
			sys.exit()
		j = j + 1
		#jeżeli w argumentach brak folderu to otwórz bieżący
	if otw == 0:
		dane = os.listdir(".")

#gdy argument z folderem to dodaj scieżkę do nazw plików
i=0;
dosort = []
if otw == 1:
	while i != len(dane):
		dosort.append(fold)
		dosort[i] = dosort[i] + '/'
		dosort[i] = dosort[i] + dane[i]
		i = i + 1
	dosort.sort()
	sciezka = dosort
#segregacja plików
dane.sort()
posort = dane
i=0
while i != len(posort): 
	blad = 0    
	if posort[i] == "." or posort[i] == "..":	
		i = i + 1
	else:
		#wypisanie odpowiednich informacji, zależnych od parametrów
		#informacje o plikach
		if otw == 1:	
			try:
        			info= os.stat(sciezka[i])
			except OSError:
        			print (posort[i])
				blad = 1
				pass
		else:
			try:
        			info= os.stat(posort[i])
			except OSError:
        			print (posort[i])
				blad = 1
				pass
		if blad == 0:
			#informacje o właścicielu
			nazwa = pwd.getpwuid(info.st_uid)
			#informacje o czasie
			czas=time.localtime(info.st_mtime)
        		sys.stdout.write(posort[i])
			#gdy -l
			if operacje == 1 or operacje == 3:
				sys.stdout.write('  ')
				print(info.st_size),
				sys.stdout.write('  ')
				print(czas.tm_year),
 				print('-'),
				if czas.tm_mon < 10:
					sys.stdout.write(' 0')
 					print(czas.tm_mon),
				else:
					print(czas.tm_mon),
 				print('-'),
				if czas.tm_mday < 10:
					sys.stdout.write(' 0')
 					print(czas.tm_mday),
				else:
					print(czas.tm_mday),
 				print(' '),
				if czas.tm_hour < 10:
					sys.stdout.write(' 0')
 					print(czas.tm_hour),
				else:
					print(czas.tm_hour),
 				print(':'),
				if czas.tm_min < 10:
					sys.stdout.write(' 0')
 					print(czas.tm_min),
				else:
					print(czas.tm_min),
				print(':'),
				if czas.tm_sec < 10:
					sys.stdout.write(' 0')
 					print(czas.tm_sec),
				else:
					print(czas.tm_sec),
				# utworzenie wyglądu praw
				prawa = info.st_mode
				zas = oct (S_IMODE(prawa))
				if S_ISDIR(prawa):
					pr='d'
				else:
					pr='-'
				k=1	
				while k != 4:
					linia = int(zas[k])
					if linia - 4 >= 0:
						pr = pr + 'r'
						linia = linia - 4
					else:
						pr = pr + '-'
					if linia - 2 >= 0:
						linia = linia - 2
						pr = pr + 'w'
					else:
						pr = pr + '-'
					if linia - 1 >= 0:
						pr = pr + 'x'
					else:	
						pr = pr + '-'
					k = k + 1
				print (pr),
			#gdy -L
			if operacje == 2 or operacje == 3:
				sys.stdout.write("  " + nazwa.pw_name)
			sys.stdout.write("\n")
        	info= []
		nazwa= []
		czas=[]
		i = i + 1
