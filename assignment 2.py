carsPresent = {'Mitsubishi Outlander':250000,'Mitsubishi Outlander PHEV':370000,
'Mitsubishi Eclipse Cross': 1400000,'Mitsubishi Mirage': 170000,
'Mitsubishi MirageG4':200000,'Mitsubishi ASX': 320000,'Mitsubishi Pajero':280000,
'Mitsubishi Montero Sport':333000,'Mitsubishi Lancer':139000,
'Mitsubishi Attrage':600000,'Mitsubishi i-MiEV':450000,'Mitsubishi Colt': 770000,
'Mitsubishi Galant':800000,'Mitsubishi Diamante':1390599,'Mitsubishi Carisma':266000,
'Mitsubishi FTO':366000,'Mitsubishi RVR':670000,'Mitsubishi Chariot':750000,
'Mitsubishi Legnum':435000,'Mitsubishi Space Star':755000,'Mitsubishi Tredia':670000,
'Mitsubishi Sapporo':720000,'Mitsubishi Celeste':3400000,'Mitsubishi Sigma':590000,
'Mitsubishi Cordia':822000,'Mitsubishi Starion':377700,'Mitsubishi L200':999000,
'Mitsubishi Triton':653000,'Mitsubishi Delica':754000,'Mitsubishi Grandis':3490000 }

car_name = input("Enter the car you wish to purchase: ")
print()
if car_name in carsPresent: 
    carPrice = carsPresent[car_name]
    print(car_name + "" + " is in stock and available for purchase")
    print("The Price of {} is ${}".format(car_name,carPrice))
    
else:
    print("sorry", car_name, "is not in stock at the moment.")
    

    
    

