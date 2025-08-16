# --- Verificador de Força de Senha ---
# Este script analisa uma senha para verificar se ela atende a critérios de segurança.
import re

def analisar_senha(senha):
    print("\n--- Analisando sua senha ---")
    
    comprimento_minimo = 8
    
    if len(senha) >= comprimento_minimo:
        print("[✓] Comprimento de no mínimo 8 caracteres.")
        comprimento_ok = True
    else:
        print("[✗] Comprimento de no mínimo 8 caracteres.")
        comprimento_ok = False

    if any(c.islower() for c in senha):
        print("[✓] Contém pelo menos uma letra minúscula.")
        tem_minuscula = True
    else:
        print("[✗] Não contém letras minúsculas.")
        tem_minuscula = False

    if any(c.isupper() for c in senha):
        print("[✓] Contém pelo menos uma letra maiúscula.")
        tem_maiuscula = True
    else:
        print("[✗] Não contém letras maiúsculas.")
        tem_maiuscula = False
        
    if any(c.isdigit() for c in senha):
        print("[✓] Contém pelo menos um número.")
        tem_numero = True
    else:
        print("[✗] Não contém números.")
        tem_numero = False

    if re.search(r'[^a-zA-Z0-9]', senha):
        print("[✓] Contém pelo menos um caractere especial.")
        tem_especial = True
    else:
        print("[✗] Não contém caracteres especiais.")
        tem_especial = False

    print("\n--- Resultado ---")
    
    criterios_atendidos = sum([comprimento_ok, tem_minuscula, tem_maiuscula, tem_numero, tem_especial])
    
    if criterios_atendidos == 5:
        print("Resultado: Senha Forte")
    elif criterios_atendidos >= 3:
        print("Resultado: Senha Média")
    else:
        print("Resultado: Senha Fraca")

senha_usuario = input("Digite a senha que deseja analisar: ")
analisar_senha(senha_usuario)
