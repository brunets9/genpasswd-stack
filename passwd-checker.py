import re
from colorama import Fore, Style, init

###################################################

init(autoreset=True)

def password_quality_checker(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 2
    else:
        feedback.append("La contraseña es demasiado corta (menos de 8 caracteres).")

    if re.search(r'[A-Z]', password):
        score += 2
    else:
        feedback.append("La contraseña no contiene letras mayúsculas.")

    if re.search(r'[a-z]', password):
        score += 2
    else:
        feedback.append("La contraseña no contiene letras minúsculas.")

    if re.search(r'[0-9]', password):
        score += 2
    else:
        feedback.append("La contraseña no contiene dígitos.")

    if re.search(r'[\W_]', password):
        score += 2
    else:
        feedback.append("La contraseña no contiene caracteres especiales (e.g., @, #, $, etc.).")

    return score, feedback

def show_password_quality(score):
    if score <= 2:
        quality = "Muy floja"
        color = Fore.RED
        bar = "[■□□□□]"  
    elif score == 4:
        quality = "Floja"
        color = Fore.YELLOW
        bar = "[■■□□□]"
    elif score == 6:
        quality = "Normal"
        color = Fore.CYAN
        bar = "[■■■□□]"
    elif score == 8:
        quality = "Buena"
        color = Fore.GREEN
        bar = "[■■■■□]"
    else:
        quality = "Muy buena"
        color = Fore.GREEN
        bar = "[■■■■■]"

    print(f"\nCalidad de la contraseña: {color}{quality} {bar}{Style.RESET_ALL}")

def main():
    password = input("Introduce tu contraseña a analizar: ")
    score, feedback = password_quality_checker(password)
    show_password_quality(score)

    if feedback:
        print("\nSugerencias para mejorar la contraseña:")
        for comment in feedback:
            print(f"- {comment}")
    else:
        print("¡Tu contraseña es muy segura!")

if __name__ == "__main__":
    main()
