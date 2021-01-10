#piccolo errore, per avere un programma migliore si consiglia di cambirare nel metodo predict il prev_months con self.name=name. cosi il programma potra predirre il valore non solo per questi dati ma per tutti gli altri

#                           ESERCIZIO 9                           #


#Implementate il metodo fit() nel modello della lezione precedente. Il fit
#deve, come appena descritto, calcolare l’incremento medio su tutto il
#dataset e salvarlo da qualche parte (es: self.global_avg_increment).
#Poi modificate il metodo predict() in modo che usi l’incremento medio
#su tutto il dataset appena calcolato, anche qui come appena descritto.




prev_months=[8,19,31,41,50,52,60]

class Model(object):
    def fit:
        pass
    def predict:
        pass





class FittableIncrementModel(Model):
    def fit #faccio dopo





    def predict(self,prev_months):

        if not isinstance(prev_months, list):
            raise print("ERRORE: il file non e una lista")
        
        if not len(prev_months)>=2:
            raise print("ERRORE: per fare una predizione bisogna avere almeno 3 numeri")

        n_months= len(prev_months)

        incremento=0

        for i in range(prev_months):
            if(i==0):
                continue
            else:
                incremento=+ prev_months[i]-prev_months[i-1]
        
        avg_incre= incremento/(n_months-1)
        return (prev_months[-1]+avg_incre)


MioModello= FittableIncrementModel()
print(predict(MioModello(prev_months)))