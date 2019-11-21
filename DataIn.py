from tkinter import filedialog as fd

def get_file():
    filename = fd.askopenfilename()
    file = open(filename,'r')
    return file

def get_line(line):
    return [str(n) for n in line.split(',')]

#Función principal para U
def set_u():
    file = get_file()
    f1=file.readlines()
    array = []
    for line in f1:
        array.append(get_line(line))
    n = len(array)
    #Validación de datos
    for i in range(n):
        if n != len(array[i]):
            print("El vector de la linea",i+1,"no cumple con la dimension adecuada")
            return 0

    #Creacion de la lista de vectores
    vectores = []
    for i in range(n):
        vector=[]
        for j in range(n):
            vector.append(int(array[i][j]))
        vectores.append(vector)
    return vectores

#Función principal para V
def set_v(n):
    file = get_file()
    f1=file.readlines()
    array = []
    for line in f1:
        array.append(get_line(line))

    #Validación de datos
    if n < len(array):
        print("V tiene mas vectores que U")
        return 0
    if n > len(array):
        print("V tiene menos vectores que U")
        return 0
    if(n!=1):
        for i in range(n-1):
            if len(array[i]) != len(array[i+1])  :
                print("El vector de la linea",i+2,"no cumple con la dimension adecuada respecto al de la linea",i+1)
                return 0
 
    #Creacion de la lista de vectores
    vectores = []
    for i in range(len(array)):
        vector=[]
        for j in range(len(array[i])):
            vector.append(int(array[i][j]))
        vectores.append(vector)
    return vectores

def set_val():
    u=set_u()
    if u!=0:
        v=set_v(len(u))
        return u,v
    return u
    
