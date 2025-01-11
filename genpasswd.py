# Paquetes a usar
import secrets
import string

###################################################

def generate_password(length=16, use_special=True):
    lower = string.ascii_lowercase      
    upper = string.ascii_uppercase      
    numbers = string.digits             
    special = string.punctuation        

    if use_special:
        all = lower + upper + numbers + special
        password = [
            secrets.choice(lower),      
            secrets.choice(upper),      
            secrets.choice(numbers),    
            secrets.choice(special)     
        ]
    else:
        all = lower + upper + numbers
        password = [
            secrets.choice(lower),      
            secrets.choice(upper),      
            secrets.choice(numbers)     
        ]

    password += [secrets.choice(all) for _ in range(length - len(password))]
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

###################################################

# Pedir al usuario si desea usar caracteres especiales
use_special = input("¿Deseas incluir caracteres especiales? (s/n): ").lower()
if use_special == 's':
    use_special = True
elif use_special == 'n':
    use_special = False
else:
    print("Entrada no válida. Se generará la contraseña sin caracteres especiales.")
    use_special = False

# Generar y mostrar la contraseña
password = generate_password(16, use_special)
print(f"Contraseña generada: {password}")

