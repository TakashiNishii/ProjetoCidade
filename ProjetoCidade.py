#Trabalho desenvolvido por Thainara Orneles Matos e Ygor Takashi Nishi para a matéria de Tópicos em linguagem de programação

import turtle
import random

s = turtle.getscreen()
t = turtle.Turtle()

#Usamos varios stamp para deixar o ceu estrelado com as estrelas de tamanhos diferentes
#e aleatórias
def CeuEstrelado():
    y = 400
    for x in range(1,6):
        t.goto(-700,y)
        for i in range(2):
            t.hideturtle()
            for image in ['S6.gif', 'S5.gif', 'S6.gif', 'S5.gif', 'S6.gif', 'S6.gif', 'S5.gif']:
                rand = random.randrange(85,230)
                t.shape(image)
                t.showturtle
                t.stamp()
                t.forward(rand)
        y = y - 80
#Para diminuir o código utilizamos de uma função para desenhar estruturas quadradas e retangulares
def estrutura(largura,altura):
    for i in range(2):
        t.forward(largura)
        t.left(90)
        t.forward(altura)
        t.left(90)
#Mudando a forma da nossa "seta"
t.penup()
t.home()
#imagem
s.register_shape('Star2.gif')
s.register_shape('S6.gif')
s.register_shape('S5.gif')
t.shape('Star2.gif')
t.hideturtle()

# cor de fundo
s.bgcolor("#060061")
s.setup(1530, 800)
s.screensize(1530, 800)

CeuEstrelado()
#Para desenhar a lua foram feitos dois circulos sobrepostos
t.penup()
t.goto(550,250)
t.pendown()
t.begin_fill()
t.pen(pencolor = "#bac3ca", fillcolor = "white", pensize = 3, speed = 100)
t.circle(80)
t.end_fill()

t.penup()
t.goto(535,270)
t.pendown()
t.begin_fill()
t.pen(pencolor = "#060061", fillcolor = "#060061", pensize = 3, speed = 100)
t.circle(80)
t.end_fill()

#coordenadas do primeiro predio da esq para dir
t.penup()
t.goto(-765,-415)
t.pendown()

#começo das estruturas de prédio
#Prédio 1:
t.begin_fill()
t.pen(pencolor = "black", fillcolor = "#4F4F4F", pensize = 1, speed = 0)
estrutura(200,800)
t.end_fill()
#Janelas:
t.penup()
t.goto(-745,-375)
t.pendown()
t.pen(pencolor = "#4F4F4F", fillcolor = "yellow", pensize = 1, speed = 0)
for i in range(19):
    for j in range(10):
        t.begin_fill()
        estrutura(10,10)
        t.end_fill()
        t.penup()
        t.forward(15)
        t.pendown()
    t.penup()
    t.goto(-745,-375 + (40*(i + 1)))
    t.pendown()
    
#fim retangulo


t.penup()
t.goto(-480,-415)
t.pendown()
#Prédio 2
t.begin_fill()
t.pen(pencolor = "black", fillcolor = "#4F4F4F", pensize = 1, speed = 0)
estrutura(225,820)
t.end_fill()
#Janelas:
t.penup()
t.goto(-460,-375)
t.pendown()
t.pen(pencolor = "#4F4F4F", fillcolor = "#ac58aa", pensize = 1, speed = 0)
for i in range(20):
    for j in range(14):
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()
        t.forward(15)
        t.pendown()
    t.penup()
    t.goto(-460,-375 + (40*(i + 1)))
    t.pendown()
#fim prédio 2   

t.penup()
t.goto(-680,-415)
t.pendown()
#Prédio 3:
t.begin_fill()
t.pen(pencolor = "black", fillcolor = "#4F4F4F", pensize = 1, speed = 0)
estrutura(225,500)
t.end_fill()
#Janelas:
t.penup()
t.goto(-660,-375)
t.pendown()
t.pen(pencolor = "#4F4F4F", fillcolor = "#ffa500", pensize = 1, speed = 0)
for i in range(22):
    for j in range(13):
        t.begin_fill()
        estrutura(10,15)
        t.end_fill()
        t.penup()
        t.forward(15)
        t.pendown()
    t.penup()
    t.goto(-660,-375 + (20*(i + 1)))
    t.pendown()
#fim prédio 3


t.penup()
t.goto(-180,-415)
t.pendown()
#Prédio 4
t.begin_fill()
t.pen(pencolor = "black", fillcolor = "#4F4F4F", pensize = 1, speed = 0)
estrutura(225,920)
t.end_fill()
#Janelas:
t.penup()
t.goto(-160,-375)
t.pendown()
t.pen(pencolor = "#4F4F4F", fillcolor = "#6eaa5e", pensize = 1, speed = 0)
for i in range(14):
    for j in range(14):
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.penup()
        t.forward(15)
        t.pendown()
    t.penup()
    t.goto(-160,-375 + (60*(i + 1)))
    t.pendown()
#fim prédio 4

t.penup()
t.goto(-300,-415)
t.pendown()
#Prédio 5
t.begin_fill()
t.pen(pencolor = "black", fillcolor = "#4F4F4F", pensize = 1, speed = 0)
estrutura(225,620)
t.end_fill()
#Janelas:
t.penup()
t.goto(-280,-375)
t.pendown()
t.pen(pencolor = "#4F4F4F", fillcolor = "#ff0048", pensize = 1, speed = 0)
for i in range(29):
    for j in range(9):
        t.begin_fill()
        estrutura(15,10)       
        t.end_fill()
        t.penup()
        t.forward(20)
        t.pendown()
    t.penup()
    t.goto(-280,-375 + (20*(i + 1)))
    t.pendown()
#fim prédio 5

t.penup()
t.goto(20,-415)
t.pendown()
#Prédio 6
t.begin_fill()
t.pen(pencolor = "black", fillcolor = "#4F4F4F", pensize = 1, speed = 0)
estrutura(200,640)
t.end_fill()
#Janelas:
t.penup()
t.goto(40,-375)
t.pendown()
t.pen(pencolor = "#4F4F4F", fillcolor = "#00c3ff", pensize = 1, speed = 0)
for i in range(15):
    for j in range(10):
        t.begin_fill()
        estrutura(10,10)
        t.end_fill()
        t.penup()
        t.forward(15)
        t.pendown()
    t.penup()
    t.goto(40,-375 + (40*(i + 1)))
    t.pendown()
    
#fim prédio 6

t.penup()
t.goto(80,-415)
t.pendown()
#Prédio 7
t.begin_fill()
t.pen(pencolor = "black", fillcolor = "#4F4F4F", pensize = 1, speed = 0)
estrutura(200,520)
t.end_fill()
#Janelas:
t.penup()
t.goto(100,-375)
t.pendown()
t.pen(pencolor = "#4F4F4F", fillcolor = "yellow", pensize = 1, speed = 0)
for i in range(12):
    for j in range(5):
        t.begin_fill()
        t.circle(15)  
        t.end_fill()
        t.penup()
        t.forward(40)
        t.pendown()
    t.penup()
    t.goto(100,-375 + (40*(i + 1)))
    t.pendown()
#fim prédio 7

t.penup()
t.goto(-100,-415)
t.pendown()
#Prédio 8
t.begin_fill()
t.pen(pencolor = "black", fillcolor = "#4F4F4F", pensize = 1, speed = 0)
estrutura(200,420)
t.end_fill()
#Janelas:
t.penup()
t.goto(-80,-375)
t.pendown()
t.pen(pencolor = "#4F4F4F", fillcolor = "#00c3ff", pensize = 1, speed = 0)
for i in range(9):
    for j in range(4):
        t.begin_fill()
        estrutura(20,20)
        t.end_fill()
        t.penup()
        t.forward(40)
        t.pendown()
    t.penup()
    t.goto(-80,-375 + (40*(i + 1)))
    t.pendown()
#fim prédio 8

t.penup()
t.goto(300,-415)
t.pendown()
#Prédio 9
t.begin_fill()
t.pen(pencolor = "black", fillcolor = "#4F4F4F", pensize = 1, speed = 0)
estrutura(200,540)
t.end_fill()
#Janelas:
t.penup()
t.goto(320,-375)
t.pendown()
t.pen(pencolor = "#4F4F4F", fillcolor = "#ffa500", pensize = 1, speed = 0)
for i in range(12):
    for j in range(5):
        t.begin_fill()
        t.circle(15)  
        t.end_fill()
        t.penup()
        t.forward(40)
        t.pendown()
    t.penup()
    t.goto(320,-375 + (40*(i + 1)))
    t.pendown()
#fim prédio 9

t.penup()
t.goto(200,-415)
t.pendown()
#Prédio 10
t.begin_fill()
t.pen(pencolor = "black", fillcolor = "#4F4F4F", pensize = 1, speed = 100)
estrutura(200,380)
t.end_fill()
#Janelas:
t.penup()
t.goto(220,-375)
t.pendown()
t.pen(pencolor = "#4F4F4F", fillcolor = "#6eaa5e", pensize = 1, speed = 0)
for i in range(17):
    for j in range(11):
        t.begin_fill()
        estrutura(10,15)
        t.end_fill()
        t.penup()
        t.forward(15)
        t.pendown()
    t.penup()
    t.goto(220,-375 + (20*(i + 1)))
    t.pendown()
#fim prédio 10

t.penup()
t.goto(450,-415)
t.pendown()
#Prédio 11
t.begin_fill()
t.pen(pencolor = "black", fillcolor = "#4F4F4F", pensize = 1, speed = 100)
estrutura(200,480)
t.end_fill()
#Janelas:
t.penup()
t.goto(470,-375)
t.pendown()
t.pen(pencolor = "#4F4F4F", fillcolor = "#ac58aa", pensize = 1, speed = 0)
for i in range(22):
    for j in range(9):
        t.begin_fill()
        estrutura(15,10)   
        t.end_fill()
        t.penup()
        t.forward(20)
        t.pendown()
    t.penup()
    t.goto(470,-375 + (20*(i + 1)))
    t.pendown()
#fim prédio 12

#imagem
# adiciona um novo shape 
s.register_shape('Star2.gif')
#transforma o turtle (seta) na imagem selecionada
t.shape('Star2.gif')
t.penup()
t.goto(0,500)
t.right(30)
t.showturtle()
#função que define instruções 
def clickleft(x,y):   
    t.pen(speed = 1)
    t.forward(800)
    t.hideturtle()
    t.goto(0,500)
    t.showturtle()
#coleta eventos do teclado       
turtle.listen()
'''chama a funçao quando acionado o botão esquerdo do mouse.
O número 1 representa o botão esq, 2 botão do meio e 3 o botão direito '''
turtle.onscreenclick(clickleft, 1)
#mantem o loop e espera uma resposta do usuário 
turtle.mainloop()
