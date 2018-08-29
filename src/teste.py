import jogodavelha
import sys

erroIncializar = False
jogo = jogodavelha.incializar()

if len(jogo) !=3:
    erroIncializar = True
else:
    for linha in jogo:
        if len (linha) !=3:
            erroIncializar = True
        else:
            for elemento in linha:
                if elemento != ".":
                    erroIncializar = True
if erroIncializar:
    sys.exit(1)
else:
    sys.exit(0)