# This is an Healthy programmer program
import datetime
import pygame
import time
start=input("Do you want to start Healthy Programmer\n"
        "1.type yes to start it for 8 hours(9 to 5)")
start=start.lower()
if start=="yes":
  initialh=time.localtime().tm_hour
  initialm=time.localtime().tm_min
  eye_counter=30
  phy_counter=45
  water_counter=59
  water_drank=0.0
  while initialh!=21:
      if initialm==eye_counter:
          pygame.mixer.init()
          pygame.mixer.music.load("eye.mp3")
          pygame.mixer.music.set_volume(1.0)
          pygame.mixer.music.play(-1)
          while True:
              eye_pause=input("Enter EyDone to stop music")
              if eye_pause=="EyDone":
                  pygame.mixer.music.stop()
                  f=open("eyerec.txt","a")
                  f.write(f"{datetime.datetime.now()}::eye excercise completed\n")
                  f.close()
                  eye_counter=abs((30+initialm)-60)
                  print(eye_counter)
                  break


      if initialm == phy_counter:
          pygame.mixer.init()
          pygame.mixer.music.load("physical.mp3")
          pygame.mixer.music.set_volume(1.0)
          pygame.mixer.music.play(-1)
          while True:
              phy_pause = input("Enter ExDone to stop music")
              if phy_pause == "ExDone":
                  pygame.mixer.music.stop()
                  f = open("phyrec.txt", "a")
                  f.write(f"{datetime.datetime.now()}::Physical excercise completed\n")
                  f.close()
                  phy_counter = abs((45+initialm)-60)
                  break
      while water_drank <= 3.5:
          if initialm == water_counter:
              pygame.mixer.init()
              pygame.mixer.music.load("water.mp3")
              pygame.mixer.music.set_volume(1.0)
              pygame.mixer.music.play(-1)
              while True:
                  water_pause = input("Enter Drank to stop music")
                  if water_pause == "Drank":
                      pygame.mixer.music.stop()
                      f = open("Waterrec.txt", "a")
                      f.write(f"{datetime.datetime.now()}::water excercise completed\n")
                      f.close()
                      water_counter = abs((59+initialm)-60)
                      water_drank+=0.5
                      break

      initialh = time.localtime().tm_hour
      initialm = time.localtime().tm_min
      