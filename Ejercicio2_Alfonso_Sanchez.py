import re

texto = '1aA'

# No contiene letras
nl = '[a-zA-Z]'
print('No contiene letras:', False if re.search(nl, texto) else True)

# Solo numero
sn = '\d+$'
print('Solo numeros:', True if re.match(sn, texto) else False)

# Solo Mayusculas
sM = '[A-Z]+$'
print('Solo mayusculas:', True if re.match(sM, texto) else False)

# Solo minusculas
sm = '[a-z]+$'
print('Solo minusculas:', True if re.match(sm, texto) else False)

# No contiene numeros
nn = '[0-9]'
print('No contiene numeros:', False if re.search(nn, texto) else True)