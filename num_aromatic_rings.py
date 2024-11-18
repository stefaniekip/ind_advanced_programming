import pandas as pd
import csv
from collections import Counter
#df = pd.read_csv("/Users/stefaniekip/Documents/BMT jaar 4/Q2 - Advanced programming/Individual Feature Engineering/data_processed.csv",'r')
def file_preparation(data):
    with open(data, 'r') as file:
        reader = csv.reader(file)
        smiles_kolom = [row[0] for row in reader]
    return smiles_kolom
file = file_preparation("/Users/stefaniekip/Documents/BMT jaar 4/Q2 - Advanced programming/Individual Feature Engineering/data_processed.csv")

def number_aromatic_rings(data):
    with open(data, 'r') as file:
        reader = csv.reader(file)
        smiles_kolom = [row[0] for row in reader]
    number_of_aromatic_rings = []
    previous = None
    for row in smiles_kolom:
        number_aro_rings = 0
        for letter in row:
            #if letter.isdigit() and previous is not None:
            if letter.isdigit():
                if previous.islower():
                    number_aro_rings += 1 
            previous = letter
                #if row[letter-1].islower():
                #if previous 
                    #number_aro_rings += 1 
        number_aro_rings = number_aro_rings//2
        number_of_aromatic_rings.append(number_aro_rings)
    return number_of_aromatic_rings

def controle(data, lijst):
    with open(data, 'r') as file:
        values_aro_rings = []
        reader = csv.reader(file)
        #smiles_kolom = [row[0] for row in reader]
        #smiles_kolom = row[9]
        column_number = -2
        for row in reader:
            values_aro_rings.append(row[column_number])
    plek = 0
    goede_lijst = {}
    foute_lijst = {}
    for waarde in lijst:
        if waarde == values_aro_rings[plek]:
            goede_lijst[plek] = waarde
        else:
            foute_lijst[plek] = waarde
        plek += 1
    return foute_lijst

#print(controle("/Users/stefaniekip/Documents/BMT jaar 4/Q2 - Advanced programming/Individual Feature Engineering/data_processed.csv", number_aromatic_rings("/Users/stefaniekip/Documents/BMT jaar 4/Q2 - Advanced programming/Individual Feature Engineering/data_processed.csv")))

# Functie om te controleren of de lijst overeenkomt met de een-na-laatste kolom
def check_values_against_csv_column(csv_file, values):
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Sla de header over als die aanwezig is
        
        # Extraheer de een-na-laatste kolom
        column = []
        for row in reader:
            if len(row) < 2:  # Controleer of er genoeg kolommen zijn
                raise ValueError("Een of meer rijen hebben minder dan twee kolommen.")
            try:
                # Converteer naar integers voor vergelijking
                column.append(int(row[-2]))
            except ValueError:
                raise ValueError(f"Kan waarde '{row[-2]}' niet converteren naar een integer.")

        # Vergelijk de waarden
        match = column == values
        return match, column  # Geeft de overeenkomst en de kolom terug

# Voorbeeldgebruik
csv_bestand = "/Users/stefaniekip/Documents/BMT jaar 4/Q2 - Advanced programming/Individual Feature Engineering/data_processed.csv"  # Vervang door jouw CSV-bestand
lijst = number_aromatic_rings("/Users/stefaniekip/Documents/BMT jaar 4/Q2 - Advanced programming/Individual Feature Engineering/data_processed.csv")  # Vervang door jouw waarden

komt_overeen, kolom_waarden = check_values_against_csv_column(csv_bestand, lijst)

#if komt_overeen:
    #print("De waarden van de lijst komen overeen met de een-na-laatste kolom in de CSV.")
#else:
   # print("De waarden van de lijst komen NIET overeen met de een-na-laatste kolom in de CSV.")
   # print("Kolom uit CSV:", kolom_waarden)


print(number_aromatic_rings("/Users/stefaniekip/Documents/BMT jaar 4/Q2 - Advanced programming/Individual Feature Engineering/data_processed.csv"))