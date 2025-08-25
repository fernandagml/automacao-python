# 📣 Notificador de Tarefas

## Descrição do Projeto 📝

Este é um projeto simples, porém funcional, de um aplicativo de desktop para agendar e receber lembretes de tarefas. O objetivo principal do projeto foi aprimorar e praticar conceitos da programação, como interface gráfica, manipulação de arquivos e automação.

## Funcionalidades 🖱

- **Interface Gráfica (GUI):** Permite adicionar novas tarefas de forma intuitiva, informando o horário e a mensagem.
- **Notificação de Sistema:** Envia lembretes diretamente para a área de trabalho do usuário no horário agendado.
- **Armazenamento de Dados:** Salva e carrega as tarefas de um arquivo de texto (`.txt`), mantendo os dados persistentes.
- **Execução em Segundo Plano:** Utiliza _threading_ para monitorar os horários das tarefas sem travar a interface gráfica.

## Tecnologias Utilizadas 💻

Este projeto foi uma excelente oportunidade para aplicar e aprofundar o conhecimento nas seguintes bibliotecas:

- **Python:** A linguagem de programação principal.
- **Tkinter:** Utilizada para a criação da interface gráfica do aplicativo.
- **Threading:** Uma biblioteca que eu nunca tinha utilizado e foi essencial para o funcionamento em segundo plano do projeto.
- **Winotify:** Biblioteca de notificação específica para Windows. A escolha por esta biblioteca foi uma decisão de aprendizado após testar e enfrentar problemas de compatibilidade com a biblioteca **Plyer**.

## Estrutura do Projeto 📍

A organização do código em módulos é importante para manter o projeto limpo e escalável.

    automacao-python
      
    |-- notificador.py           # Arquivo principal da interface gráfica
    |-- funcoes_notificador.py   # Funções de lógica (notificação, leitura de arquivo, etc.)
    |-- tarefas.txt              # Arquivo de dados para armazenar as tarefas


## Melhorias Futuras 📎✔

O projeto ainda pode ser aprimorado com as seguintes funcionalidades:

- **Distribuição como Executável:** O principal objetivo é transformar o projeto em um único arquivo `.exe`, eliminando a necessidade de o usuário ter o Python instalado. (Observação: Houve desafios com a compilação, o que se tornou uma meta de aprendizado futura).
- **Gerenciamento de Tarefas:** Adicionar a opção de deletar ou editar tarefas diretamente pela interface gráfica.
- **Notificações Recorrentes:** Implementar a opção de agendar tarefas diárias ou semanais.
