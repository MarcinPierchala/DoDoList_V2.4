import time
import pickle
from datetime import datetime, timedelta


class DoDo:

    def __init__(self,unical_numers,prior,opis):
        self.data=datetime.now()
        self.prior=prior
        self.opis=opis
        self.unical_numers=unical_numers
        

    def __str__(self):
        dodano=datetime.strftime(self.data, '%Y-%m-%d')
        count=datetime.now()-self.data
        return f" Numer wpisu : {self.unical_numers}. Data dodania : {dodano} i było to {count.days} temu. Priorytet zadania: {self.prior}, a jego opis to : {self.opis}."


class ListDoDo:

    zadanka=[]
    unical_numers=0

    def __init__(self, plik):

        self.plik=plik
        try:
            with open(self.plik,'rb') as f:
                self.zadanka=pickle.load(f)
                self.unical_numers=max(z.unical_numers for z in self.zadanka)
                print('PLIK WCZYTANY')
        except:
            print('NIE MOŻNA ZNALEŹĆ PLIKSA')


    def wyswietl(self):
        print('LISTA ZAPISANYCH ZADAŃ')
        for z in self.zadanka:
            print(z)

        

    def dodaj(self,prior,opis):
        
        self.unical_numers+=1
        print('.......TRWA ZAPIS DO PROGRAMU.......')
        new_task=DoDo(self.unical_numers,prior,opis)
        self.zadanka.append(new_task)
        time.sleep(1)
        print('ZAPISANO ZADANIE NR : ',self.unical_numers)

    def skasuj(self, numer):
        for i,j in enumerate(self.zadanka):
            if j.unical_numers==int(kasuj):
                del self.zadanka[i]
                return

    def save(self):
        with open(self.plik,'wb') as f:
            pickle.dump(self.zadanka, f)



if __name__=='__main__':

    
    finisher=0
    
    zadanka=ListDoDo('c:/Python/zadania.pickle')

    
  

    print('''WITAJ W PROGRAMIE __LISTA_2_DO__ 
    WYBIERZ MENU : 
    1 : DODAJ NOWE ZADANIE
    2 : SKASUJ NIEPOTRZEBNE ZADANIE
    3 : PRZEGLĄD ZADAŃ
    4 : ZAKOŃCZ PROGRAM
    ''')

    while finisher!=4:

        param=input(' PODAJ NUMER MENU : ')

        if param=='1':
            prior=input('''PODAJ PRIORYTET ZADANIA W SKALI : 
            1 : NAJWAŻNIEJSZE
            2 : WAŻNE
            3 : MAŁO WAŻNE 
            PODAJ TUTAJ : ''')
            opis=input('PODAJ KRÓTKI OPIS ZADANIA : ')
            zadanka.dodaj(prior, opis)

        if param=='2':
            kasuj=input('PODAJ NUMER ZADANIA DO SKASOWANIA : ')
            zadanka.skasuj(kasuj)
            
        if param=='3':
            zadanka.wyswietl()
        
        if param=='4':
            print('\nDZIĘKUJĘ ZA SKORZYSTANIE Z PROGRAMU\n\n           DO WIDZENIA')
            zadanka.save()
            
                
            finisher=4
