from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date

janela =Tk()
janela.title("Calculadora de idade")
janela.geometry('310x400')

cor1 = '#191C1C' # preta
cor2 = '#474747' # cinza
cor3 = '#D3D8D8' # branco cinzento

frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=cor1)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=260, pady=0, padx=0, relief=FLAT, bg=cor2)
frame_baixo.grid(row=1, column=0)


l_calculadora = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief='flat', anchor='center', font=('Ivi 15 bold'), bg=cor1, fg=cor3)
l_calculadora.place(x=0, y=30)


l_idade = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0, relief='flat', anchor='center', font=('Arial 20 bold'), bg=cor1, fg=cor3)
l_idade.place(x=60, y=65)


def calcular():
    inicio = cal_de_hoje.get()
    termino = cal_nascimento.get()

    mes_1, dia_1, ano_1 = [int(f) for f in inicio.split('/')]
    data_inicio = date(ano_1, mes_1, dia_1)

    mes_2, dia_2, ano_2 = [int(f) for f in termino.split('/')]
    data_final = date(ano_2, mes_2, dia_2)

    ano = relativedelta(data_inicio, data_final).years
    mes = relativedelta(data_inicio, data_final).months
    dia = relativedelta(data_inicio, data_final).days

    l_app_ano['text'] = ano
    l_app_mes['text'] = mes
    l_app_dia['text'] = dia


l_data_de_hoje = Label(frame_baixo, text="Data de hoje", height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivy 15 bold'), bg=cor2, fg=cor3)
l_data_de_hoje.place(x=0, y=30)

cal_de_hoje = DateEntry(frame_baixo, width=15, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='mm/dd/y', y=2023)
cal_de_hoje.place(x=195, y=35)


l_data_nascimento = Label(frame_baixo, text="Data de Nascimento", height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivy 15 bold'), bg=cor2, fg=cor3)
l_data_nascimento.place(x=0, y=65)

cal_nascimento = DateEntry(frame_baixo, width=15, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='mm/dd/y', y=2023)
cal_nascimento.place(x=195, y=70)


l_app_ano = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 25 bold'), bg=cor2, fg=cor3)
l_app_ano.place(x=25, y=135)
l_app_ano_nome = Label(frame_baixo, text="Ano", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=cor2, fg=cor3)
l_app_ano_nome.place(x=25, y=170)

l_app_mes = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 25 bold'), bg=cor2, fg=cor3)
l_app_mes.place(x=115, y=135)
l_app_mes_nome = Label(frame_baixo, text="Meses", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=cor2, fg=cor3)
l_app_mes_nome.place(x=115, y=170)

l_app_dia = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 25 bold'), bg=cor2, fg=cor3)
l_app_dia.place(x=225, y=135)
l_app_dia_nome = Label(frame_baixo, text="Dias", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=cor2, fg=cor3)
l_app_dia_nome.place(x=225, y=170)

b_calcular = Button(frame_baixo, command=calcular, text="Calcular", width=20, height=1, relief='raised', overrelief='ridge', font=('Ivy 10 bold'), bg=cor2, fg=cor3)
b_calcular.place(x=72, y=225)


janela.mainloop()
