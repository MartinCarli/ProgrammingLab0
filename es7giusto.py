#les n 7 giusto


#creo la classe CSVfile
class CSVFile():
    #creo il metodo che istanzia l'oggetto
    def __init__(self, name):
        #alzo un'errore se il nome del file non è una stringa
        if not isinstance(name,str):
            raise Exception ('il nome del file non è una stringa. riprovare grazie')
        #gli attribuisco l'attributo nome
        self.name = name

    #creo un metodo che legge il file e stampa il valore numerico
    def get_data(self, start=None, end=None):
        if start > end:
            raise Exception('il valore "start" non puo essere piu grande del valore "end"')
        #inizializzo una lista dove salvare i valori numerici
        converted_values = []
        #provo ad aprire il file
        try:
            my_file = open(self.name, 'r')
        except Exception as e:
            
            # Stampo l'errore
            print('Errore nella lettura del file: "{}"'.format(e))
            return None
        #creo un contatore da utilizzare nel for
        numero_riga = 0
        #per ogni riga del mio file:
        for line in my_file:
            # mi assicuro che il contatore che sta tra start e end in modo da lavorare solo sulle righe 
            if numero_riga >= start and numero_riga <= end:
                #separo la stringa in piu stringhe usando "," come divisore
                element = line.split(',')
                #escludo l'intestazione
                if element[0] != 'Date':
                    #setto la data e il valore
                    date = element[0]
                    value = element[1]
                    #provo a convertire "value" in valori numerici
                    try:
                        value = float(value)
                    #se si verifica un errore di tipo stampo il seguente messaggio 
                    except TypeError as e:
                        print('cè stato un errore di tipo con la stringa: "{}"'.format(e))
                    #se si verifica un errore di altro tipo stampo il seguente messaggio 
                    except Exception as e:
                        print('cè stato un errore sconosciuto con la stringa "{}"'.format(e))
                        #salto questa linea e continuo col ciclo
                        continue
                    #appendo la stringa convertita in valore numerico alla lista converted_values
                    converted_values.append(value)
            #aumento il contatore di 1
            numero_riga=numero_riga+1
        #chiudo il mio file
        my_file.close()
        #ritorno la lista di valori numerici
        return converted_values
#test
try:
    file = CSVFile('shampoo_sales.csv')
    data = file.get_data(start=1,end=5)
    print(data)
except:
    print(e)

