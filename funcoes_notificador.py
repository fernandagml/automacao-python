#Bibliotecas de tempo do Python
import time
import datetime

#Função de notificação da biblioteca plyer
from plyer import notification

def ler_tarefas(tarefas_arquivo="tarefas.txt"):

    tarefas = []
    with open(tarefas_arquivo, 'r', encoding='utf-8') as arquivo:
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

def monitorar_tarefas():
     
     while True:
        tarefas_agendadas = ler_tarefas()
        if tarefas_agendadas:
            agora = datetime.datetime.now().time()
            
            for tarefa in tarefas_agendadas:
                horario_tarefa = tarefa['horario']
                
                if agora.hour == horario_tarefa.hour and agora.minute == horario_tarefa.minute:
                    print(f"Enviando notificação: {tarefa['mensagem']}")
                    enviar_notificacao("Lembrete de Tarefa!", tarefa['mensagem'])

                    time.sleep(60)

        time.sleep(30)