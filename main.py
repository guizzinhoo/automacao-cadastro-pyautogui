import time
import pandas
import pyautogui

#Automatizando a abertura do Chrome, acesso e login ao site, e definindo pausas
pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1.5)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=619, y=406)
pyautogui.write('gui.eu@gmail.com')
pyautogui.press('tab')
pyautogui.write('123987')
pyautogui.press('tab')
pyautogui.press('enter')

#importando a tabela a ser utilizada
tabela = pandas.read_csv('registro.cvs')

#Automatizando o registro de informações
for linha in tabela.index:
    time.sleep(0.5)

    pyautogui.click(x=606, y=287)
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    #Formatando valores vazios
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(str(obs))
    pyautogui.press('tab')

    pyautogui.press('enter')

    pyautogui.scroll(10000)

