def list_sum(the_list):
    total=0
    for item in the_list:
        total = total + item
    return total


# Inizializzo una lista vuota per salvare i valori
values = []
# Apro e leggo il file, linea per linea
my_file = open("shampoo_sales.txt", "r")
for line in my_file:
 # Faccio lo split di ogni riga sulla virgola
    elements = line.split(',')
 # Se NON sto processando l’intestazione...
    if elements[0] != 'Date':

        date = elements[0]
        value = elements[1]
    values.append(float(value))


x= list_sum(values)
print(x)
#fineprogramma