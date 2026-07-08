import re

def verificar_texto(texto):
    # Definimos a nossa regra de ouro
    padrao = r"^[a-zA-Z0-9]+$"
    
    # O re.search vai olhar o texto e ver se ele obedece ao padrão
    if re.search(padrao, texto):
        print(f"✅ O texto '{texto}' é VÁLIDO! Contém apenas letras e números.")
    else:
        print(f"❌ O texto '{texto}' é INVÁLIDO! Contém espaços ou símbolos não permitidos.")

# Testando a nossa máquina:
verificar_texto("Lorenzo2026")      # Deve dar VÁLIDO
verificar_texto("Senha_Forte!")     # Deve dar INVÁLIDO (tem sublinhado e exclamação)
verificar_texto("Python é legal")   # Deve dar INVÁLIDO (tem espaços e acento)