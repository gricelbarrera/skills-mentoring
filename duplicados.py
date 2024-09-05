def ctr_duplicados(cadena):
    caracteres_vistos = list()
    duplicados = list()
    
    for caracter in cadena:
        if caracter in caracteres_vistos:
            duplicados.appned(caracter)
        else:
            caracteres_vistos.append(caracter)
    
    return duplicados

def main():
    print(ctr_duplicados("Holaaaa"))
    return

if __name__ == "__main__":
    main()