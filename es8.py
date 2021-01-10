
#piccolo errore, per avere un programma migliore si consiglia di cambirare nel metodo predict il prev_months con self.name=name. cosi il programma potra predirre il valore non solo per questi dati ma per tutti gli altri


#scrivere una funzione senza fit che calcoli la predizione del valore del mese sucessivo

##########INIZIO PRE-PROGRAMMA #########################



prev_months = [50, 52, 60]
#inserisco i dati manualmente come ha fatto il prof (dati di lezione)

class Model(object):
    def fit(self,data):    #ora come ora questo non serve
        pass
    
    def predict(self):
        pass               #ora come ora questo non serve


class IncrementModel(Model):

    def fit(self,data):
        raise NotImplementedError('questo modello non prevede un fit')
    def predict(self,prev_months):
        #inizio con i test base
        if not isinstance(prev_months,list):
            raise print("Errore: 'prev_months' non e` di tipo lista")
        if len(prev_months)<=2:
            raise print("Errore: per calcolare l'incemento, prev_months deve avere almeno 3 'mesi'")

        n_months= len(prev_months)
        incremento=0

        for i in range(n_months):
            if i== 0:
                continue
            else:
                incremento+= prev_months[i]-prev_months[i-1]
        
        avg_incremento= incremento/(n_months-1)
        return (avg_incremento+prev_months[-1])


###########################
#   CORPO DEL PROGRAMMA   #
###########################

mioModello=IncrementModel()
print(mioModello.predict(prev_months))