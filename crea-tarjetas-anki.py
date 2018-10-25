import pyautogui
import time

lista=[]
lista.append('IconoAnki.PNG')
lista.append('btnCerrar.PNG')
lista.append('btnAnadir.PNG')

for i in range(len(lista)):
	pos=pyautogui.locateCenterOnScreen(lista[i])
	pyautogui.moveTo(pos[0], pos[1])
	if i == 0 :pyautogui.doubleClick() 
	else: pyautogui.click()
	time.sleep(5)

lista=[]
lista.append(['hola', 'adios'])
lista.append(['adios', 'hola'])

for i in range(len(lista)):
	pyautogui.typewrite(lista[i][0] + '\t' + lista[i][1])
	pyautogui.moveTo(pyautogui.locateCenterOnScreen('btnAnadir2.PNG'))
	pyautogui.click()
	time.sleep(1)