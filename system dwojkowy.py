k=int(input('wpisz liczbe= '))
Dwojkowy=[]
liczba=k
while liczba>0:
    if liczba%2==1:
        Dwojkowy.append(1)
        liczba=liczba//2
    else:
        Dwojkowy.append(0)
        liczba=liczba//2
Dwojkowy.reverse()

print(k, " w systemie dwójkowym to ", Dwojkowy)
        
    
