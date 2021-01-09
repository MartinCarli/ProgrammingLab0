class CSVFile:
    def __init__(self, filename):
        self.name=filename
        if not isinstance (self.name, str):
            raise Exception('Non è una stringa')
      

    def get_data(self, start=None, end=None):
        #inizializzo una lista vuota per salvare i valori
        values=[]
        i=start
        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            
            # Stampo l'errore
            print('Errore nella lettura del file: "{}"'.format(e))

        for line in my_file:
            if i<=end+1: #qua aggiungo 1 perche parte da 0

                #splitto goni riga sulla virgola
                elements = line.split(',')
                #se non sto processando l'intestazione
                if elements[0] != 'Date':
                    #setto la data e il valore
                    date = elements[0]
                    value = elements[1]
                    try:
                        value = float(value)
                    except Exception as e:
                    
                    # Stampo l'errore
                        print('Errore nela conversione a float: "{}"'.format(e))
                    
                    # Vado al prossimo "giro" del ciclo, quindi NON eseguo quanto viene dopo (ovvero l'append)
                        continue
                
                # Infine aggiungo alla lista dei valori questo valore
                    values.append(value)
            i=i+1    #aggiungo un 1 al start 
        my_file.close()

        return values



#======================
# Corpo del programma
#======================

mio_file = CSVFile('shampoo_sales.csv')

print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: "{}"'.format(mio_file.get_data(start=1,end=5)))
