
######## importing blibrarys ######
import pygame
#import cv2

path = "./sounds/en/"
attention = "attension.wav"
direction_sound = ["left.wav" , "up.wav" , "right.wav" , "middle.wav" , "down.wav"]
order = 0
order1 = 0
pygame.mixer.init()
speaker_volume = 1 ####volime = 100%
pygame.mixer.music.set_volume(speaker_volume) # activate speaker

######## core of the system ########

def direction ():
    if (order ==0): ######pay attention up left
        pygame.mixer.music.load(path + attention)
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
        
        pygame.mixer.music.load(path + direction_sound[0])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue

        pygame.mixer.music.load(path + direction_sound[1])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue    
    
 
 
    elif (order ==1): ######pay attention up middle
        pygame.mixer.music.load(path + attention)
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
        
        pygame.mixer.music.load(path + direction_sound[1])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue

        pygame.mixer.music.load(path + direction_sound[3])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue



    elif (order ==2): ######pay attention right up
        pygame.mixer.music.load(path + attention)
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
                
        pygame.mixer.music.load(path + direction_sound[2])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
            
        pygame.mixer.music.load(path + direction_sound[1])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
        
                 
             
    elif (order ==3):######pay attention left middle 
        pygame.mixer.music.load(path + attention)
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
        
        pygame.mixer.music.load(path + direction_sound[0])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
        
        pygame.mixer.music.load(path + direction_sound[3])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue       
 
 
 
    elif (order ==4):######pay attention middle
        pygame.mixer.music.load(path + attention)
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
        
        pygame.mixer.music.load(path + direction_sound[3])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
    
    
    
    elif (order ==5):######pay attention  rihht middle
        pygame.mixer.music.load(path + attention)
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue

        pygame.mixer.music.load(path + direction_sound[2])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
        
        pygame.mixer.music.load(path + direction_sound[3])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue



    elif (order ==6):######pay attention left down 
        pygame.mixer.music.load(path + attention)
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
 
        pygame.mixer.music.load(path + direction_sound[0])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
        pygame.mixer.music.load(path + direction_sound[4])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
        
        
        
    elif (order ==7):######pay attention down middle
        pygame.mixer.music.load(path + attention)
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
        
        pygame.mixer.music.load(path + direction_sound[4])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue

        pygame.mixer.music.load(path + direction_sound[3])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
     
   
   
    elif (order ==8):######pay attention down right
        pygame.mixer.music.load(path + attention)
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
        
        pygame.mixer.music.load(path + direction_sound[2])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue

        pygame.mixer.music.load(path + direction_sound[4])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue

        
        
    ### 0= left 1=up 2=right 3=middle 4=down #####



#########son des object
object_sound = ["car.wav" , "animal.wav" , "electric_pole.wav" , "impediment.wav" , "crowding.wav","car_lane.wav","footpath.wav"]

def obstacle() :
    if (order1 ==0): ###### car
        pygame.mixer.music.load(path + object_sound[0])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue    
    
    
 
    elif (order1 ==1): ###### animal 
        pygame.mixer.music.load(path + object_sound[1])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
        
        
        
    elif (order1 ==2): ###### electric_pole 
        pygame.mixer.music.load(path + object_sound[2])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
        
        
    elif (order1 ==3): ###### obstacle 
        pygame.mixer.music.load(path + object_sound[3])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
        
        
        
    elif (order1 ==4): ###### traffic_jam 
        pygame.mixer.music.load(path + object_sound[4])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
        
        
    elif (order1 ==5): ###### car_lane
        pygame.mixer.music.load(path + object_sound[5])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
        
        
        
    elif (order1 ==6): ###### pass_buildings 
        pygame.mixer.music.load(path + object_sound[6])
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy() == True):
            continue
  