#Bibliotecas TKinter
import tkinter as tk

#Biblioteca para rodar a notificação em segundo plano
import threading as thr

#Biblioteca de tempo do Python
import datetime

from funcoes_notificador import Notificador as Nf
        
def salvar_tarefa():

    # Declara que as variáveis a seguir são as globais, ou seja, as mesmas criadas na janela do Tkinter.
    global entrada_horario, entrada_mensagem

    horario = entrada_horario.get()
    mensagem = entrada_mensagem.get()
    
    if horario and mensagem:

        #Formato do horário
        datetime.datetime.strptime(horario, '%H:%M')
        
        with open("tarefas.txt", "a", encoding='utf-8') as arquivo:
            arquivo.write(f"\n{horario};{mensagem}")
        
        # Limpa os campos após salvar
        entrada_horario.delete(0, tk.END)
        entrada_mensagem.delete(0, tk.END)
        
        print("Tarefa salva com sucesso!")

    else:
        print("Por favor, preencha todos os campos.")

#Janela Tk
janela = tk.Tk()
janela.config(bg="#E6E9FF")
janela.title("Gerenciador de Tarefas")
janela.geometry("350x200")

titulo_label = tk.Label(janela, text="Adicionar Nova Tarefa", font=("Arial", 14, "bold"))
titulo_label.pack(pady=10)

horario_label = tk.Label(janela, text="Horário (HH:MM):")
horario_label.pack()
entrada_horario = tk.Entry(janela)
entrada_horario.pack()

mensagem_label = tk.Label(janela, text="Notificar:")
mensagem_label.pack()
entrada_mensagem = tk.Entry(janela)
entrada_mensagem.pack()

botao_salvar = tk.Button(janela, text="Salvar Tarefa", command=salvar_tarefa)
botao_salvar.pack(pady=10)

#Lógica de monitoramento em uma thread separada -- permite que a interface(GUI) e o monitoramento funcionem ao mesmo tempo
monitor_thread = thr.Thread(target=Nf.monitorar_tarefas, daemon=True)
monitor_thread.start()

janela.mainloop()