from random import *
anser = ["a","b","c","d","e","f","g","h"]
seed(random())
p0 = ""
print("Witam W Grze MasterMind\n Twoim zadaniem jest odgadnięcie kodu, który składa się z liter od \""+anser[0]+"\" do \"" +anser[len(anser)-1]+"\"\nKu Twojemu szczęściu, dam Tobie delikatne podpowiedzi. ")
print("Jeżeli podczas sprawdzenia wystąpi  symbol \"*\" to jakaś z liter znajduje się na swoim miejscu.\nJeżeli natomiast \"-\" to jakaś z tych liter występuje w kodzie i nie znajduje się na swoim miejscu.")
print("Jeżeli potrzebujesz pomocy ze znakami \"*\" lub \"-\" to wpisz \"?\" lub \"help\"")
print("Podaj poziom trudności (easy (E) = 4 litery do zgadnięcia lub hard (H) = 5 liter do zgadnięcia")
while 1!=0:
    dif = input()
    dif = dif.lower()
    if dif == "e" or dif == "easy":
        dificulty = 4
        break
    elif dif =="h" or dif == "hard":
        dificulty = 5
        break
    else:
        print("Kod jest zbyt długi. Spróbuj jeszcze raz!")
print("Powodzenia!")
for i in range(dificulty):
    p0 = p0 + anser[randint(int(chr(48)),ord(chr(94))-ord('W'))]
for runda in range(9):
    check_info = ""
    while 1 != 0:
        print(str(runda + 1) + ")", end="")
        d = input("Twój Kod: \n")
        if d == "?" or d == "help":
            print("Gra polega na odgadnięcu kodu który jest zapisany za pomocą liter od "+anser[0]+" do " +anser[len(anser)-1])
            print("Jeśli w sprawdzeniu występuje symbol \n \"*\" oznacza on, że jakaś z wpisanych liter znajduje się na swoim miejscu w kodzie.  Jeśli pojawi się symbol \n \"-\" to dana litera z podanego kodu znajduje się w szukanym haśle.")
        elif len(d)<=len(p0) and d != "?":
            for i in range(len(d)):
                if d[i] not in anser:
                    print("Podałeś literę nie będącą w zakresie od "+anser[0]+" do " +anser[len(anser)-1])
                    break
            else:
                break
        else:
            print("Kod jest za długi podaj jeszcze raz")
    if len(d) < len(p0):
        for a in range(3):
            if len(d) == len(p0):
                break
            d += "_"
    d = d.lower()
    d = list(d)
    p = p0
    p = list(p)
    # sprawdzamy "czarne szpilki" (*)
    for i in range(len(p)):
        if d[i] == p[i]:
            p[i] = "*"
            d[i] = "*"
            check_info += "*"
    # sprawdzamy "białe szpilki" (-)
    for i in range(len(p)):
        if d[i] in p and d[i] != "-" and d[i] != "*":
            p[p.index(d[i])] = "-"
            d[i] = "-"
            check_info += "-"
    print(check_info, "\t<- Sprawdzenie")
    if check_info == "****":
        print("wygrałeś")
        break
if check_info != "****":
    print("Przegrełeś \n Poprawy kod " + p0)