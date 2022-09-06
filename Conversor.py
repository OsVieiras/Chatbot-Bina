# Armazenar um número entre 0 e 255, por exemplo o número 120.
numero = 255

# Subtraia o número por 128, se o resultado da operação for 0 ou superior então o primeiro bit é 1
if (numero - 128) >= 0:
    binário = "1"
    numero = numero - 128
else:
    binário = "0"

# Subtraia o número por 64, se o resultado da operação for 0 ou superior então o segundo bit é 1
if (numero - 64) >= 0:
    binário = binário + "1"
    numero = numero - 64
else:
    binário = binário + "0"

# Subtraia o número por 32, se o resultado da operação for 0 ou superior então o terceiro bit é 1
if (numero - 32) >= 0:
    binário = binário + "1"
    numero = numero - 32
else:
    binário = binário + "0"

# Subtraia o número por 16, se o resultado da operação for 0 ou superior então o quarto bit é 1
if (numero - 16) >= 0:
    binário = binário + "1"
    numero = numero - 16
else:
    binário = binário + "0"

# Subtraia o número por 8, se o resultado da operação for 0 ou superior então o quinto bit é 1
if (numero - 8) >= 0:
    binário = binário + "1"
    numero = numero - 8
else:
    binário = binário + "0"

# Subtraia o número por 4, se o resultado da operação for 0 ou superior então o sexto bit é 1
if (numero - 4) >= 0:
    binário = binário + "1"
    numero = numero - 4
else:
    binário = binário + "0"

# Subtraia o número por 2, se o resultado da operação for 0 ou superior então o sétimo bit é 1
if (numero - 2) >= 0:
    binário = binário + "1"
    numero = numero - 2
else:
    binário = binário + "0"

# Subtraia o número por 1, se o resultado da operação for 0 ou superior então o oitavo bit é 1
if (numero - 1) >= 0:
    binário = binário + "1"
    numero = numero - 1
else:
    binário = binário + "0"


print(numero)
print(binário)
