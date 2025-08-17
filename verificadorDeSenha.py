# --- Verificador de Força de Senha ---
# Este script analisa uma senha para verificar se ela atende a critérios de segurança.
#Estima o tempo que um computador levaria para quebrar a senha por força bruta.

import re
import math

def estimar_tempo_quebra(senha):
    tamanho_conjunto = 0
    if any(c.islower() for c in senha):
        tamanho_conjunto += 26
    if any(c.isupper() for c in senha):
        tamanho_conjunto += 26
    if any(c.isdigit() for c in senha):
        tamanho_conjunto += 10
    if re.search(r'[^a-zA-Z0-9]', senha):
        tamanho_conjunto += 32

    if tamanho_conjunto == 0:
        return "Instantaneamente"

    comprimento_senha = len(senha)
    combinacoes = math.pow(tamanho_conjunto, comprimento_senha)

    tentativas_por_segundo = 10**10
    segundos_para_quebrar = combinacoes / tentativas_por_segundo

    if segundos_para_quebrar < 1:
        return "Instantaneamente"
    elif segundos_para_quebrar < 60:
        return f"{segundos_para_quebrar:.1f} segundos"
    elif segundos_para_quebrar < 3600:
        return f"{segundos_para_quebrar / 60:.1f} minutos"
    elif segundos_para_quebrar < 86400:
        return f"{segundos_para_quebrar / 3600:.1f} horas"
    elif segundos_para_quebrar < 31536000:
        return f"{segundos_para_quebrar / 86400:.1f} dias"
    elif segundos_para_quebrar < 3153600000:
        return f"{segundos_para_quebrar / 31536000:.1f} anos"
    elif segundos_para_quebrar < 31536000000:
        return f"{segundos_para_quebrar / 3153600000:.1f} séculos"
    else:
        return "Milênios (praticamente inquebrável)"

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

    tempo_estimado = estimar_tempo_quebra(senha)
    print(f"Tempo estimado para quebra: {tempo_estimado}")

senha_usuario = input("Digite a senha que deseja analisar: ")
analisar_senha(senha_usuario)
#madeCaiqueBTC
