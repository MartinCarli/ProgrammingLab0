
#sbagliato, questa e la  mia prima simulazione


class ExamException(Exception):     #per alzare le eccezioni
    pass

class MovingAverage:
    def __init__(self,lunghezza):
        self.lunghezza = lunghezza

    def compute(self,valori):
        lista_valori=[]
        
        if not isinstance(valori,list):
            raise ExamException('Errore i valori non sono in una lista')

        nval == len(valori)

        if mialung > nval:
            raise ExamException('Errore la lunghezza deve essere minore o ugale al numero dei valori')
        if valori is None:
            raise ExamException('Errore la lista e vuota')

        valore=0
        mialung == lunghezza
       

        for i in valori:
            valore=0
            k==i
            if (i+mialung>=nval):
                continue
            while(k is not mialung):
                valore+= valori[k]
                k+=1
            valore== valore/mialung
            lista_valori.append(valore)

        return lista_valori