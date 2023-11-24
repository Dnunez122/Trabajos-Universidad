# "secrets" se usa para generar tokens aleatorios de seguridad y string para trabajar con cadenas de texto
import secrets
import string

#Se declara la variable letras para crear cadenas de texto con concatenaciones de mayusculas y minusculas.
letras = string.ascii_letters

#Se usa este comando para obtener numeros del 0 al 9
digitos = string.digits

#Se usa este comando para obtener los caracteres especiales.
Caracteres = string.punctuation

#Los unimos en una variable
contraseña = letras + digitos + Caracteres

#Delimitamos la contraseña a 8 digitos.
contra_leng = 8

#aqui se guardara la contraseña generada por python con una longitud de 8
psw = ''

#Se usa un ciclo "para" con numero maximo de 8 digitos, se agrega el char random que genere python y se agrega a secrets, y a contraseña.
for i in range(contra_leng):
    psw += ''.join(secrets.choice(contraseña))
    print(psw) # Para finalmente imprimir la contraseña ya generada por python despues de que el "for" se haya completado.