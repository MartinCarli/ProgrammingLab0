#adesso cambiero e faro l esercizio della lezione 6


#====================================================
#problema

#il programma non e finito, bisogna ancora fare in modo che il 
#programma legga un intervallo di righe

#quando avrai capito come fare aggiungi pure qualche test

#=====================================================





#=================== INIZIO DEL PROGRAMMA ==========================





#======================
# Classe per file CSV
#======================

class CSVFile:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name
       

    def get_data(self, start= None, end= None):

        # Inizializzo una lista vuota per salvare i valori
        values = []

        # Provo ad aprire il file per estrarci i dati. Se non ci riesco, prima avverto del'errore, 
        # poi devo abortire. Questo e' un errore "un-recoverable", ovvero non posso proseguire con
        # la lettura dei dati se non riesco ad aprire il file!
        try:
            my_file = open(self.name, 'r')

        except:
            if isinstance is not(name,str):
                raise Exception('Errore: il file non e di tipo stringa')

        # Ora inizio a leggere il file linea per linea
        for line in my_file:
           # Faccio lo split di ogni linea sulla virgola
            elements = line.split(',')

            # Se NON sto processando l'intestazione...
            if elements[0] != 'Date':
                    
                # Setto la data ed il valore
                date  = elements[0]
                value = elements[1]
                
            # La variabile "value" al momento e' ancora una stringa, poiche' ho letto da file di testo,
            # quindi converto a valore floating point, e se nel farlo ho un errore avverto. Questo e'
            # un errore "recoverable", posso proseguire (semplicemente salto la linea).
                try:
                    value = float(value)
                except Exception as e:
                    
                # Stampo l'errore
                    print('Errore nela conversione a float: "{}"'.format(e))
                    
                # Vado al prossimo "giro" del ciclo, quindi NON eseguo quantoviene dopo (ovvero l'append)
                    continue
                
            # Infine aggiungo alla lista dei valori questo valore
                values.append(value)
        
        # Chiudo il file
        my_file.close()
        
        # Quando ho processato tutte le righe, ritorno i valori
        return values
    
        
#======================
# Corpo del programma
#======================

mio_file = CSVFile(name='shampoo_sales.csv')


print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: "{}"'.format(mio_file.get_data()))