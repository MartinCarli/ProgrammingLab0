#crea ogetto CSVfile
#l'ogetto deve avere un self.name
#crea un metodo(funzione) che torni i dati del file csv

#######seconda parte######
#modifica csv, se vogliamo aprire un file inesistente arriva un messaggio
#aggiungiamo nel file una stringa e spazio vuoto e gestiamo l'errore

class CSVfile()
    def __init__(self,name):
        self.name= name

    def get_data():
        values= []
    
        try:
            mio_file = open(self.name,'r')
            
            for line in mio_file:
                try:
                    elements= line.split(',')

                    if elements[0]!= 'Date':
                        date= elements[0]
                        value= elements[1]
                    values.append(float(value))
                except: print("Non e` stato possibile convertire la linea '{}' in un numero float".format(line))

            return(values) 
        except:
            print("Non ho trovato alcun file con questo nome")

file=CSVfile(name= 'shampoo_sales_csv')
print(file.name)
print(file.get_data())