import os

#zo open je een bestand om naar te schrijven
bestand = open("test.txt","w")

#een tekst naar een bestand schrijven
bestand.write("test 123!")

#bestand in read only (r) mode openen
bestand2 = open("test.txt","r")

#een tekst naar een bestand schrijven 
bestand2.write("lekker alles overschrijven")

