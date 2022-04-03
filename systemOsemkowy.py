#zamiana liczby z dziesiętnej na system ósemkowy

def osemkowy(liczba):
    lista=[]
    while liczba>0:
        lista.append(liczba%8)
        liczba=liczba//8
    lista.reverse()
    oktalnie=lista

    return(oktalnie)
i=0
while i==0:
    liczba=int(input("wpisz liczbe "))
    print(osemkowy(liczba))
    ask=input("czy chcesz zamienić kolejną liczbę? (tak/nie) ")
    if ask=="nie":
        i=i+1