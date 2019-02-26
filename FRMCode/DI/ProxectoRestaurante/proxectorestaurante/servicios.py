import locale #Permite obter os datos referentes a o teu pais, neste caso, util para a moeda.
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
import zipfile
import os
import getpass
import datetime


def comprobarDNI(caixa):
    try:
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"  # letras del dni
        extrange = "XYZ"
        taboaextrange = {'X': '0', 'Y': '1', 'Z': '2'}
        numeros = "1234567890"
        dni = caixa.get_text()
        dni = dni.upper()  # pasa letras a mayúsculas
        if len(dni) == 9:
            letra = dni[8]
        dni = dni[:8]  # el número que son los 8 primeros
        if dni[0] in extrange:  # comprueba que es extranjero
            dni = dni.replace(dni[0], taboaextrange[dni[0]])
        return len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == letra
    except:
        return False

def recortarEuro(cadea):
    var = cadea.split("€")[0]
    retoque = float(var)
    return retoque


def colocarEuro(numero):
    retoque = locale.currency(numero)
    return retoque

def xerar_copia_seg():
    nome='Restaurante'
    data =datetime.datetime.now()
    if not os.path.exists('/home/'+getpass.getuser()+'/copias_seguridade'):
        os.makedirs('/home/'+getpass.getuser()+'/copias_seguridade', mode=0o777)
    fichzip = zipfile.ZipFile('/home/'+getpass.getuser()+'/copias_seguridade/'+str(data)+"_copia_"+nome+".zip",'w')
    fichzip.write(nome, './Restaurante' ,zipfile.ZIP_DEFLATED)
    fichzip.close()
