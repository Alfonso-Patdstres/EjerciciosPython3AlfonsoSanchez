import re

# Correo electronico
correoE = 'juan@padts.mx', 'juan@padts.com.mx', 'juan@python.padts.mx'

# Patron de correo
patronC = '[a-zA-Z0-9._]{4,12}@[a-zA-Z0-9]*(\.[a-zA-Z0-9]*)?(\.[a-zA-Z0-9]{2,3}){1,2}$'

# Verificaion de correos
print('\nVerificacion de correos:')
for i in correoE:
    print(f'{i} \t\t Correo valido' if re.match(patronC, i) else f'{i} \t\t Correo no valido')


# Numero Telefonico
numeroT = '3314567822', '(33)14567822', '(331)4567822', '(33) 1456 7822', '(333)-456-7822', '(331) 456-7822'

# Patron Numeros
patronN = '[0-9]{10}|\([0-9]{2,3}\)[0-9]{7,8}|\([0-9]{2,3}\)[ ][0-9]{3,4}[ ]?[0-9]{4}|\([0-9]{2,3}\)[-][0-9]{3,4}[-]?[0-9]{4}$'

# Verificaion de correos
print('\nVerificación de numeros de telefono:')
for i in numeroT:
    print(f'{i} \t\t Numero Valido' if re.match(patronN, i) else f'{i} \t\t Numero no valido')


# RFC
rfc = 'JUPG500515GD4', 'JuPG500515GD4' , 'JUPG500515HGD4'

# Patron RFC
patronR = '[A-Z]{4}[0-9]{6}[A-Z0-9]{3}$'

#Verificación RFC
print('\nVerificacion RFC')
for r in rfc:
    print(f'{r}\t\t RFC Valido' if re.match(patronR, r) else f'{r}\t\t RFC no Valido')


# Curp
curp = 'PEGJ500515HZSRRN00', 'PEGJ500515JZSRRN00', 'PEGJ500515MZSRR1A0'

# Patron Curp
patronCu = '[A-Z]{4}[0-9]{6}[HM][A-Z]{2}[A-Z]{3}[A-Z0-9]{2}'

#Verificar Curp
print('\nVerificar Curp')
for c in curp:
    print(f'{c}\t\t Curp valida' if re.match(patronCu, c) else f'{c}\t\t Curp no valida')
