#esercizio= scrivi un modello simile a quello visto a lezzione

class Model(object):
    def fit(self,data):    #ora come ora questo non serve
        pass
    
    def predict(self):
        pass              #ora come ora questo non serve


#inserisco i dati manualmente come ha fatto il prof

shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]

#inizio a scrivere le funzioni

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

        for i in range(n_months)
            if i= 0
                continue
            else
                incremento+= prev_months[i]-prev_months[i-1]
                
        avg_incremento= inremento/prev_months[-1]
        return avg_incremento+prev_months[-1]

