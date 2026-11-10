@echo off
rem Chamado pelo Agendador de Tarefas do Windows todo dia (via rodar-escondido.vbs, sem janela).
rem "start /low" = prioridade baixa: o robô só usa o PC quando sobra, não trava nada.
set PYTHONIOENCODING=utf-8
cd /d "%~dp0..\.."
set PY="C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\python.exe"
start "" /low /b /wait %PY% sistema\acompanhamento\acompanhar.py rodar > sistema\acompanhamento\saida-ultima-rodada.txt 2>&1
start "" /low /b /wait %PY% sistema\acompanhamento\acompanhar.py relatorio >> sistema\acompanhamento\saida-ultima-rodada.txt 2>&1
