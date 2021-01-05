#crea ogetto CSVfile
#l'ogetto deve avere un self.name
#crea un metodo(funzione) che torni i dati del file csv

class CSVfile()
    def __init__(self,name):
        self.name= name

    def get_data():
        values= []
    
        mio_file = open(self.name,'r')

        for line in mio_file:
            elements= line.split(',')

            if elements[0]!= 'Date':
                date= elements[0]
                value= elements[1]
            values.append(float(value))

        return(values)

# file=CSVfile(name= 'shampoo_sales_csv')
# print(file.name)
# print(file.get_data())