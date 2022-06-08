from pynput import keyboard
import pyautogui as cursor
from time import sleep

# sleep(3)
# getLocation = cursor.position()
# print(getLocation)
# sleep(100)


def apertou(botao):
#atualizar clickando nos 4 quadradinhos
    if(botao == keyboard.KeyCode(char="0")):
        cursor.moveTo(x=515, y=270, duration=0.01)
        cursor.click()
#Selecionar item e enviar transação pra (metamask)
    elif(botao == keyboard.KeyCode(char="1")):
        cursor.moveTo(x=297, y=661, duration=0.01)
        cursor.click()
#Ir para atividade na (metamask)
    elif (botao == keyboard.KeyCode(char="2")):
        cursor.moveTo(x=1549, y=483, duration=0.01)
        cursor.click()
#Selecionar transação (metamask)
    elif (botao == keyboard.KeyCode(char="3")):
        cursor.moveTo(x=1020, y=547, duration=0.01)
        cursor.click()
#Aceitar transação (metamask)
    elif (botao == keyboard.KeyCode(char="4")):
        cursor.moveTo(x=1422, y=944, duration=0.01)
        cursor.click()
#Voltar depois que selecionar item
    elif (botao == keyboard.KeyCode(char="6")):
        cursor.moveTo(x=105, y=262, duration=0.01)
        cursor.click()
#Abrir autorefresh (extensão)
    elif (botao == keyboard.KeyCode(char="7")):
        cursor.moveTo(x=590, y=92, duration=0.01)
        cursor.click()
#Iniciar autorefresh (extensão)
    elif (botao == keyboard.KeyCode(char="8")):
        cursor.moveTo(x=467, y=138, duration=0.01)
        cursor.click()
#Sai do autorefresh (extensão)
    elif (botao == keyboard.KeyCode(char="9")):
        cursor.moveTo(x=673, y=226, duration=0.01)
        cursor.click()
    elif (botao == keyboard.KeyCode(char="5")):
        break
#Loop
with keyboard.Listener(on_press=apertou) as listener:
    listener.join()
