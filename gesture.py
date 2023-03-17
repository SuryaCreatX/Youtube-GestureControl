import cv2
import mediapipe as mp
from func import recognizeHandGesture,getStructuredLandmarks
import webbrowser
import pyautogui as py
import time
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

webbrowser.open("https://www.youtube.com/")
time.sleep(3)
py.moveTo(577,124)
py.click()

py.write("Python in explained")
time.sleep(3)
py.click(x=1258, y=135)

time.sleep(1)
'''from selenium import webdriver
chromedriver="chromedriver"
driver=webdriver.Chrome(chromedriver)'''
py.moveTo(703,656)
py.click()

time.sleep(1)

py.click()

def gest():
    '''driver.get('https://www.youtube.com/watch?v=09R8_2nJtjg')
    driver.execute_script('document.getElementsByTagName("video")[0].play()')'''
    hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
    cap = cv2.VideoCapture(0)
    i=0
    c=0
    while cap.isOpened():
      l=[]
      i+=1
      success, image = cap.read()
      if not success:
        break
      image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
      image.flags.writeable = False
      results = hands.process(image)
      image.flags.writeable = True
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
      o=results
      if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
          mp_drawing.draw_landmarks(
              image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
          c+=1
          for lp in hand_landmarks.landmark:
              l.append(lp.x)
              l.append(lp.y)
      cv2.imshow('MediaPipe Hands', image)
      try:
          recognizedHandGesture = recognizeHandGesture(getStructuredLandmarks(l))
          print(recognizedHandGesture)
          if(recognizedHandGesture==5):
              py.keyDown('k')
              py.keyUp('k')
              time.sleep(1)
          elif(recognizedHandGesture==4):
              py.keyDown('shift')
              py.press('n')
              py.keyUp('shift')
              time.sleep(1)
          elif(recognizedHandGesture==3):
              py.keyDown('m')
              py.keyUp('m')
              time.sleep(1)
              #driver.execute_script('document.getElementsByTagName("video")[0].playbackRate = 2')
          elif(recognizedHandGesture==2):
              
              py.keyDown("right")
              py.press('right')
              py.keyUp("right")
              time.sleep(1)
              
              '''a = input("Enter the topic :")
              webbrowser.open("https://www.youtube.com/")
              time.sleep(3)
              py.keyDown('/')
              py.keyUp('/')
              time.sleep(3)
              py.write(a)
              time.sleep(3)
              py.keyDown('enter')
              py.keyUp('enter')
              time.sleep(2)
              py.moveTo(703,656)
              py.click()

              time.sleep(1)

              py.click()'''

              #driver.execute_script('document.getElementsByTagName("video")[0].playbackRate = 1')
          elif(recognizedHandGesture==6):
              py.keyDown('shift')
              py.press('p')
              py.keyUp('shift')
              time.sleep(1)
              #driver.execute_script('document.getElementsByTagName("video")[0].volume = 0')
          elif(recognizedHandGesture==7):
              py.keyDown("left")
              py.press('left')
              py.keyUp("left")
              time.sleep(1)
              #driver.execute_script('document.getElementsByTagName("video")[0].volume = 1')

      except:
          print('none')
      if cv2.waitKey(5) & 0xFF == 27:
        break
    hands.close()
    cap.release()
gest()
