import pywhatkit as kt

lista_de_numeros = ["COLOQUE O(S) NÚMERO(S) AQUI"]
msg = "COLOQUE A MENSAGEM AQUI"

for numero in lista_de_numeros:
    kt.sendwhatmsg(numero, msg, 0, 0)
                                #Coloque a hora e minuto que deseja enviar a mensagem