import pandas as pd


df = pd.DataFrame({
    'Autor':[],
    'Tytuł':[],
    'Literatura':[],
    'Cena':[],
    'Ilość kartek':[],    
})

file = pd.read_csv("Books.csv")

while True:
    print("\n\nMenu:  \n")
    print("1.Dodaj książkę \n")
    print("2.Wyrzuć książkę \n")
    print("3.Wyświetl bibliotekę \n")


    x = input("Wpisz numer: ")

    if x == '1':
        autor = input("Podaj autora: ")
        tytuł = input("Podaj tytuł: ")
        literatura = input("Podaj literature: ")
        cena = input("Podaj cene: ")
        ilośćKartek = input ("Podaj ilosc kartek: ")

        data =  [{'Autor':autor,'Tytuł':tytuł,'Literatura':literatura,'Cena':cena,'Ilość kartek':ilośćKartek}]
        newBook = df.append(data,sort=False)
        newBook.to_csv("Books.csv",mode='a',header=False)

    if x =='2':
        id = int(input("Podaj numer wiersza, który chcesz usunąć: "))
        file.drop(df.columns[[id]],axis=1)    

    if x =='3':
        print("Twoja Biblioteka:  \n \n")
        print(file)

    if x =='4':
        print('bye')
        break
    