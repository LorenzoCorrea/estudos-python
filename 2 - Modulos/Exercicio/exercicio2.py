# Agendamento de desligamento
# Crie duas funções em python para agendar o desligamento do computador em uma hora e meia hora.
import os

tempo_60 = 1800
tempo_1 = 3600

comando = f"shutdown /s /t {tempo_60}"
os.system(comando)