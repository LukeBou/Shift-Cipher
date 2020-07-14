# =============================================================================
# TRABAJO FINAL PYTHON 3
# Nombre: Lucas Jimenez Bou
# Modalidad: Propuesta 2
# =============================================================================

with open("fichero_cifrado.txt", "r") as f: #leemos el archivo .txt que contiene el cifrado
    texto_cifrado = f.read()
    
def cifrando(texto, i):
    texto = texto.replace(" ", "")   #elimina los espacios entre las palabras
    texto_novo = ""
    for c in texto:     
        
#        ord(c)                                         #descubrimos el codigo unicode del caracter 
#        ord(c) - 65                                    #restamos 65 para que trabajemos con un codigo alternativo en que la letra A y Z tengan index 0 y 25 respectivamente
#        ord(c) - 65 + i                                #añadimos la clave i que "mueve" el alfabeto
#        (ord(c) - 65 + i) %26                          #el restante de la division entre 26 determina la posicion de la clave en caso del codigo original + clave superen el index 25 del codigo alternativo 
#        (ord(c) - 65 + i) %26)+65                      #añadimos 65 al codigo alternativo para obtener el index dentro del codigo ASCII
#        letra_nova = chr((ord(c) - 65 + i) %26)+65)    #descubrimos a que caracter se refiere el nuevo codigo ASCII

        letra_nova = chr(((ord(c)-65+i)%26)+65)
        texto_novo += letra_nova             #creamos una nueva cadena con todos los caracteres en la respectiva clave
        texto_novo = texto_novo.replace("NN", "Ñ")  #cambiando los caracteres NN por Ñ
    return texto_novo



def claves_y_descifrados(codigo_cifrado):
    cyc = {}
    for i in range(0,27):
        cyc[i] = cifrando(codigo_cifrado, i)  #percorre la funcion cifrando() de 0 a 26, referente a la longitud del alfabeto 
    return cyc


fichero_plano = claves_y_descifrados(texto_cifrado)        

        

# =============================================================================
# ELEGIR TEXTO Y CLAVE CORRECTOS
# =============================================================================


with open ("Diccionario.txt", "r") as h:  #leyendo el Diccionario de lengua castellana
    dic_castellano = h.read()



def palabra_hits(cifrado, dic=dic_castellano):
    """" 
    BUSCA POR LAS PALABRAS DENTRO DE DICCIONARIO.TXT Y REGISTRA EL NUMERO DE EXITOS DENTRO DE CADENA DE CÖDIGO CIFRADO
    """
    dic = dic.split() # separar palabras con funcion  .split()
    hits = 0
    palabras_detectadas = []
    for palabra in dic: #vamos recorrer cada palabra del Diccionario.txt haciendo modificaciones para que sean compatibles y comparables a las palabras del codigo_plano
        if len(palabra) <= 3:        #reducimos la posibilidad de falsos positivos
            continue
        else:
            palabra = (palabra.upper())  #convertimos a letras mayúsculas
            palabra = palabra.replace("Á", "A") #se eliminan posibles tildes
            palabra = palabra.replace("É", "E")
            palabra = palabra.replace("Í", "I")
            palabra = palabra.replace("Ó", "O")
            palabra = palabra.replace("Ú", "U")
            palabra = palabra.replace("Ü", "U")
            palabra = palabra.replace("Ö", "O")
            hits +=  cifrado.count(palabra)  # la funcion count() cuenta cuantas veces aparece la palabra en una cadena y sumamos este valor al variable "hits" 
                                             #cuanto más "hits", más grande la probalidad que esta se la clave "crackeada"
            if palabra in cifrado:
                palabras_detectadas.append(palabra) #quiero que el programa me diga cuales palabras fueron identificada en el codigo
    
    print(cifrado)            
    print("Palabras detectadas: ", str(palabras_detectadas),"\n\n")        
    return hits
         

def clave_detect(fichero_plano):
    clave_hit = []
    for clave, cifrado in fichero_plano.items():
        print("Clave: ", clave)
        clave_hit.append((clave,palabra_hits(cifrado)))
    clave_detect = max(clave_hit, key=lambda x:x[1])
    #la funcion max() retorna el objecto más alto, el criterio de comparación "key" se realiza mediante la función lambda, 
    #en este caso, comparamos a los index = 1 de cada tupla en clave_hit
    return clave_detect #retorna una tupla con la clave con más hits y su respectivo numero de hits
  
final = clave_detect(fichero_plano)
print("\u2605"*5)  
resultado = str("CLAVE CORRECTA: " + str(final[0])+ "\nTexto: "+ str(fichero_plano[final[0]]) +"\nNumero de hits: "+ str(final[1]))
print(resultado)
print("\u2605"*5)


with open ("fichero_plano.txt", "w") as g:
    g.write("BUCLE DE CRACKEO:\n\n")
    for k, v in fichero_plano.items():
        g.write("Clave: "+ str(k)+ "\n" + str(v) + "\n\n")
        
    g.write ("___________________________________________________ \n\n"+
             "RESULTADO FINAL \n\n"+
             "___________________________________________________ \n\n"
             )
    g.write(resultado)