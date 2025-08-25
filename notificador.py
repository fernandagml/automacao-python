#Função de notificação da biblioteca plyer
from plyer import notification

#Bibliotecas de tempo do Python
import time
import datetime

TITULO = "Lembrete de Tarefa!"
MENSAGEM = "Sua tarefa está agendada para agora. Não se esqueça!"

def ler_tarefas(tarefas_arquivo="tarefas.txt"):
    tarefas = []
    with open(tarefas_arquivo, 'r') as arquivo:
            for linha in arquivo:
                #Remove espaços em branco do início e fim da linha
                linha_limpa = linha.strip()
                if not linha_limpa:
                    continue
                
                partes = linha.split(';', 1)
                if len(partes) == 2:
                    horario_str, mensagem = partes
                    tarefas.append({
                        'horario': datetime.datetime.strptime(horario_str, '%H:%M').time(),
                        'mensagem': mensagem.strip()
                    })
    return tarefas

def enviar_notificacao(titulo, mensagem):
        title=titulo,
        message=mensagem,
        app_name="Notificador de Tarefas",
        timeout=10

print("Notificador de tarefas iniciado. Aguardando o horário...")

tarefas_agendadas = ler_tarefas()

if not tarefas_agendadas:
     print("Nenhuma tarefa agendada. Atualize seu arquivo.")
else:
    while True:
        #Horário atual
        agora = datetime.datetime.now()

        for tarefa in tarefas_agendadas:
            horario_tarefa = tarefa['horario']

        #Horário para a notificação ser enviada
        horario_notificacao = agora.replace(hour=8, minute=55, second=0, microsecond=0)

        if agora.hour == horario_tarefa.hour and agora.minute == horario_tarefa.minute:
                print(f"Notificação: {tarefa['mensagem']}")
                enviar_notificacao("Lembrete de Tarefa!", tarefa['mensagem'])
                
                tarefas_agendadas.remove(tarefa)
                
        time.sleep(30)
        
        if not tarefas_agendadas:
            print("Todas as tarefas agendadas foram enviadas. Encerrando o programa.")
            break