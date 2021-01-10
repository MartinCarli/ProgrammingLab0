#piccolo errore, per avere un programma migliore si consiglia di cambirare nel metodo predict il prev_months con self.name=name. cosi il programma potra predirre il valore non solo per questi dati ma per tutti gli altri

                 
#                           ESERCIZIO 9                           #



#Implementate il metodo fit() nel modello della lezione precedente. Il fit
#deve, come appena descritto, calcolare l’incremento medio su tutto il
#dataset e salvarlo da qualche parte (es: self.global_avg_increment).
#Poi modificate il metodo predict() in modo che usi l’incremento medio
#su tutto il dataset appena calcolato, anche qui come appena descritto.
############### ESERCIZIO N 9 CON FIT   #######################



data=[8,19,31,41]    #definisco le liste
prev_months=[50,52,60]

class Model(object):        #definisco la prima classe Model
    def fit(self,data):
        pass
    def predict(self,prev_months):
        pass


class FittableIncrementModel(Model):   #definisco l a classe fattab...
    
    def fit(self,data):
        
        if not isinstance(data, list): #faccio dei controlli 
            raise print("ERRORE: il file non e una lista")
        
        if not len(data)>=2:
            raise print("ERRORE: per fare una predizione bisogna avere almeno 3 numeri")

        n_data= len(data)  #setto la lungezza della lista

        incremento1=0      #definisco la variabile dell'incremento (0)

        for i in range(n_data): #dalla riga i fino la fine (n_data)
            if(i==0):           #se i vale 0 vai avanti
                continue
            else:
                incremento1+= data[i]-data[i-1] #senno fai l incremento
        
        self.avg_incre1= incremento1/(n_data-1) #calcolo cosa devo sommare a data "attuale"
        return (data[-1]+self.avg_incre1)   #calcolo l intero incremento della "prima parte" 




    def predict(self,prev_months):    #definisco la classe predict

        if not isinstance(prev_months, list):   #faccio dei controlli
            raise print("ERRORE: il file non e una lista")
        
        if not len(prev_months)>=2:
            raise print("ERRORE: per fare una predizione bisogna avere almeno 3 numeri")

        n_months= len(prev_months)

        incremento=0  #uguale a prima

        for i in range(n_months):
            if(i==0):
                continue
            else:
                incremento+= prev_months[i]-prev_months[i-1]
        
        avg_incre= incremento/(n_months-1)
        return (prev_months[-1]+(self.avg_incre1/2)+(avg_incre/2))#qua utilizzo il valore di prima pre calcolare la predizione finale 

    #######################
    ### CORPO PROGRAMMA ###
    #######################


#QUA STAMPO TUTTI I RESULTATI

mioModello= FittableIncrementModel()
print(mioModello.fit(data))
print(mioModello.predict(prev_months))

#fine programma