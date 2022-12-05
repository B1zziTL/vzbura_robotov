#vlozenie modulu
import tkinter

#nastavenie platna
canvas = tkinter.Canvas(width=500,height=500,background="white")
canvas.pack()

#nastavenie vstupneho pola
entry1 = tkinter.Entry()
entry1.pack()

#zadeklarovanie premennych
povodna_x = 250
povodna_y = 250
momentalna_x = povodna_x
momentalna_y = povodna_y
uhol = 1

#vykreslenie zakladneho bodu (robota)
canvas.create_line(povodna_x,povodna_y,povodna_x+1,povodna_y+1)

def co_teraz(): #funkcia na zistenie parametrov prikazov
    #zadeklarovanie globalnych premennych
    global prikaz, smer, nieco, dlzka

    #ulozenie vstupu do premennej
    prikaz = entry1.get()

    #podmienky na zapisanie prikazov do spravnych premennych
    if prikaz == "vpravo":
        smer = "vpravo"
    elif prikaz == "vlavo":
        smer = "vlavo" 
    else:
        #rozdelenie dvojslovneho prikazu a vyuzitie druhej casti
        prikazik = prikaz.split()
        if len(prikazik) == 2:
            dlzka = int(prikazik[1])

    #zistovanie novozadanych udajov po 500 sekundach   
    canvas.after(500,co_teraz)

def bobek_maliar(): #funkcia na vykreslenie prikazov
    #zadeklarovanie globalnych premennych
    global momentalna_x, momentalna_y
    global uhol

    #pomocne podmienky na spravne urcenie uhlu
    if uhol == 1 and smer == "vlavo":
        uhol = 5
    if uhol == 4 and smer == "vpravo":
        uhol = 0

    #podmienky na zapisanie zmeny uhla
    if smer == "vpravo":
        uhol += 1
    if smer == "vlavo":
        uhol -= 1

    #podmienky na vykreslenie novej ciary podla momentalneho uhla a nasledna zmena zaciatocnych suradnic buducej ciary
    if uhol == 1: #0°/360°
        canvas.create_line(momentalna_x,momentalna_y,momentalna_x,momentalna_y-dlzka)
        momentalna_y -= dlzka
    if uhol == 2: #90°
        canvas.create_line(momentalna_x,momentalna_y,momentalna_x+dlzka,momentalna_y)
        momentalna_x += dlzka
    if uhol == 3: #180°
        canvas.create_line(momentalna_x,momentalna_y,momentalna_x,momentalna_y+dlzka)
        momentalna_y += dlzka
    if uhol == 4: #270°
        canvas.create_line(momentalna_x,momentalna_y,momentalna_x-dlzka,momentalna_y)
        momentalna_x -= dlzka

#privolanie funkcie
co_teraz()

#nastavenie tlacidla
magicke_tlacitko = tkinter.Button(text="Vykonaj",command=bobek_maliar)
magicke_tlacitko.pack()
