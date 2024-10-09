#Abrir o navegador
#Acessar site com login e senha 
#Preencher todas as informações do produto 
#Enviar as informações para o sistema
#Repetir o cadastro até acabar todos os produtos

import pyautogui
import pandas as pd
import pygetwindow as gw
import time

#importar base de dados
tabela = pd.read_csv("produtos.csv")
print(tabela)

#pyautogui.press: serve para pressionar uma tecla do seu teclado
#pyautogui.write: serve para escrever com o teclado (como se estivesse
#pyautogui.click: serve para clicar com o mouse

#definir tempo de espera entre os comandos
pyautogui.PAUSE = 0.8

#Abrir navegador 
pyautogui.press("win")
pyautogui.write("chrome")    
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#esperar carregar 
time.sleep(5)

#Maximizar janela caso esteja minimizada
navegador = gw.getWindowsWithTitle("chrome")
if navegador:
    navegador_chrome = navegador[0]
    if not navegador_chrome.isMaximized:
        navegador_chrome.maximize()

#fazer login 
pyautogui.click(x=712, y=378)
pyautogui.write("julia.testeauto@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234")  
pyautogui.click(x=942, y=533)

#cadastrar produtos
#cada linha da tabela = um produto que deve ser cadastrado 


for linha in tabela.index:
    pyautogui.click(x=760, y=257)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    #repetir em todas as linhas da tabela
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")  

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.click(x=892, y=902)
