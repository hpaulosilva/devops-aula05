def incializar():
    tab=[]
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append(".")
        tab.append(linha)
    return tab

def main():
    jogo = incializar()
    print (jogo)
if __name__ == "__main__":
    main()