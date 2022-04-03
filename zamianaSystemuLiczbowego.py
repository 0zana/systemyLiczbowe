#zamiana liczby dzięsiętnej na wybrany system liczbowy (2/8/16)

def innySystemLiczbowy(liczba, system):
    lista=[]
    while liczba>0:
        if liczba%jakiSystem<10:
            lista.append(liczba%jakiSystem)
        else:
            kod=chr((liczba%jakiSystem-10)+65)
            print(kod)
            lista.append(kod)
        liczba=liczba//jakiSystem
    lista.reverse()
    poZmianie=lista

    return(poZmianie)

i=0
while i==0:
    liczba=int(input("wpisz liczbe "))
    jakiSystem=int(input("na jaki system chcesz zamienić? (2/8/16) "))
    print(innySystemLiczbowy(liczba, jakiSystem))
    ask=input("czy chcesz zamienić kolejną liczbę? (tak/nie) ")
    if ask=="nie":
        i=i+1