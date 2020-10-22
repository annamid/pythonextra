# Hier impoteer je de os module
import os

# de huidige directory opvragen en opslaan in de variable: werkmap
werkmap = os.getcwd()

# de letters cwd staan voor: current working direcory
print("de huidige map is: " + werkmap)

# een nieuwe map maken met os.mkdir()
os.mkdir("een nieuwe map")

# gebruiker om de naam van de map te vragen 
mapnaam = input("welke naam wil je voor je map?: ")

# als de lengte van mapnaam > 0 dan maken we de map 
lengte_mapnaam = len(mapnaam) 
if lengte_mapnaam > 0:
    os.mkdir(mapnaam)
    print("de map " + mapnaam + " is gemaakt")
else:
    print("je gebt geen naam ingevuld")    
