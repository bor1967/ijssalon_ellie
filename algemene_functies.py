def mijn_functie_1(argument):
    waarden = {
        2: 4,
        4: 16,
        10: 100,
        12: 144
    }
    return waarden.get(argument, "Ongeldig argument")

print(mijn_functie_1(4))   
print(mijn_functie_1(5))    
     
def mijn_functie_2(arg1, arg2):
    combinaties = {
        (12, 3): [15, 9, 36, 4],
        (12, 2): [14, 10, 24, 6],
        (10, 5): [15, 5, 50, 2],
        (100, 20): [120, 80, 2000, 5]
    }
    return combinaties.get((arg1, arg2), "Ongeldige combinatie")

print(mijn_functie_2(12, 3))     
print(mijn_functie_2(100, 20))   
print(mijn_functie_2(1, 2))      

