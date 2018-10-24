# Automatizando clics y más

Artículo [aqui](https://automatetheboringstuff.com/chapter18/). ¡Atención, usuarios de Linux y Mac! Hará falta instalar algunas librerías extra:
* En OS X, corre sudo pip3 install pyobjc-framework-Quartz, sudo pip3 install pyobjc-core, y then sudo pip3 install pyobjc.
* On Linux, corre sudo pip3 install python3-xlib, sudo apt-get install scrot, sudo apt-get install python3-tk, y sudo apt-get install python3-dev.

Primero instalamos la librería:

```python
pip install pyautogui
```

En la documentación podemos ver las funciones principales:

<iframe src="https://pyautogui.readthedocs.io/en/latest/cheatsheet.html" frameborder="0" width="100%" height="700" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

>**info**
>
>Si en una terminal normal the python, NO de ipython, introducimos el comando pyautogui.displayMousePosition(), nos irá diciendo la posición de nuestro ratón.

Comandos interesantes:

```python
import pyautogui
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(100, 150)
pyautogui.click()
pyautogui.moveRel(None, 10)  # move mouse 10 pixels down
pyautogui.doubleClick()
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
pyautogui.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('esc') # Puedes acceder a la lista de palabras con pyautogui.KEYBOARD_KEYS
pyautogui.keyDown('shift')
pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')
```

## Reconociendo imágenes

```python
pyautogui.screenshot('archiv.png')
pyautogui.locate('archiv.png')
pos = pyautogui.locateCentreOnScreen('archiv.png')
pyautogui.click()
```