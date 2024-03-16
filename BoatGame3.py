import pygame,sys,random,time,math
from pygame.locals import*
pygame.init()

displaysurf=pygame.display.set_mode((1600,900))
pygame.display.set_caption("The Boat Game")
clock=pygame.time.Clock()

imageLIST=[]
explosionIMGLIST=[]
bulletLIST=[]
enemyLIST=[[100,100,0,10,1,1]]#x,y,counter to shoot,health , level

shoot=pygame.mixer.Sound("shotgun.wav")
blast=pygame.mixer.Sound("blast.wav")
ting=pygame.mixer.Sound("ting.wav")
buySound=pygame.mixer.Sound("buySound.wav")
#pygame.mixer.music.load("ocean.wav")
pygame.mixer.music.load("pirate_music.mp3")
pygame.mixer.music.play(500,0)

angle=0
angleIN=0
xpos=800
ypos=450
speed=3
speedIN=0
acceleration=0.01

water=pygame.image.load("water5.jpg").convert()

#island=pygame.image.load("island.png").convert_alpha()
island=pygame.image.load("island2.png").convert_alpha()
colourBoat=pygame.image.load("colourBoat.png").convert_alpha()
map1=pygame.image.load("map.jpg").convert()

arrow1=pygame.image.load("arrow1.png").convert_alpha()
lightning=pygame.image.load("lightning.png").convert_alpha()
titlePic=pygame.image.load("boatTitle.png").convert_alpha()
wPic=pygame.image.load("wTEXT.png").convert()
skyPic=pygame.image.load("blueSky.png").convert_alpha()
skyPic.set_alpha(230)
sunRay=pygame.image.load("sunRay.png").convert_alpha()

lootBoxPic=pygame.image.load("lootBox.png").convert_alpha()

shopPic=pygame.image.load("shop.jpg").convert()
closePic=pygame.image.load("close.jpg").convert()
ballsPic=pygame.image.load("ballsPic.png").convert()
speedPic=pygame.image.load("speedPic.png").convert()
healthPic=pygame.image.load("healthPic.png").convert()
damagePic=pygame.image.load("damagePic.png").convert()
lightPic=pygame.image.load("lightPic.png").convert()
hpPic=pygame.image.load("hpPic.png").convert()
reloadPic=pygame.image.load("reloadPic.png").convert()
crewPic=pygame.image.load("crewPic.png").convert()

sailColour=pygame.image.load("flagColour.png").convert()
boatColour=pygame.image.load("boatColour.png").convert()
cannonsColour=pygame.image.load("cannonsColour.png").convert()
floorColour=pygame.image.load("floorColour.png").convert()

shield=pygame.image.load("shield.png").convert_alpha()

gui1Pic=pygame.image.load("gui1.png").convert_alpha()
boatPic=pygame.image.load("boatCross.png").convert_alpha()
onBoatPic=pygame.image.load("onBoat.png").convert_alpha()
#water=pygame.transform.scale(water,(500,500))
mapxpos,mapypos=-2000,-3000
enemyLIST=[[500,500,0,10,1]]##Last one is level
upwardTextLIST=[[0,0,0,"l",(0,0,0)]]#x , y , starty,text, colour

lootBoxLIST=[]
waterEffectList=[]
fontObj = pygame.font.Font('freesansbold.ttf', 20)##font
fontObjsmall=pygame.font.Font('freesansbold.ttf', 12)
money=0
balls=120
fireShot=False
menu=True
screen=pygame.Rect(-200,-200,1800,1100)
mousex,mousey=0,0

maxHealth=10
health=10
##shop items texts
buyspeedtext = fontObjsmall.render(str("1 Speed // 100 C "), True, (255,255,255))##Display speed text to shop
buyballtext = fontObjsmall.render(str("10 Balls // 2 C "), True, (255,255,255))##Display ball text to shop
buyhealthtext = fontObjsmall.render(str("1HP // 2 C "), True, (255,255,255))##Display health text to shop
buydamagetext = fontObjsmall.render(str("1DMG // 100 C "), True, (255,255,255))##Display health text to shop
buyhptext = fontObjsmall.render(str("1Max HP // 50 C "), True, (255,255,255))##Display health text to shop
buylighttext = fontObjsmall.render(str("Lighting //1000 C "), True, (255,255,255))##Display health text to shop
buyreloadtext = fontObjsmall.render(str("1 Reload// 100 C "), True, (255,255,255))##Display health text to shop
buycrewtext = fontObjsmall.render(str("1 Crew // 50 C "), True, (255,255,255))##Display health text to shop


defendtext = fontObj.render(str("Defending"), True, (0,0,0))

reloadtext = fontObj.render(str("Reload"), True, (0,0,0))
movetext = fontObj.render(str("Speed"), True, (0,0,0))
damagetext = fontObj.render(str("Damage"), True, (0,0,0))
allocationtext = fontObj.render(str("Crew Allocation"), True, (0,0,0))

reloadTimer=0
angleMenu=0
damage=1
lightningPower=False
onBoat=False
defend=False
explosionLIST=[[0,0,4,False]]
reloadTime=90
crew=6

allocatedMove=3
allocatedDamage=1##Allocated in rooms
allocatedReload=2

enemyImageLIST=[]
sailSetColour=(255,255,255)
boatSetColour=(159,115,42)
cannonsSetColour=(0,0,0)#Sets original colours
floorSetColour=(64,34,1)
cycle=0

###Loading Shadows
shadright=pygame.image.load("shad1.png").convert_alpha()
shadup=pygame.image.load("shadup.png").convert_alpha()
shaddown=pygame.image.load("shaddown.png").convert_alpha()
shadleft=pygame.image.load("shadleft.png").convert_alpha()



####AREAS OF MAP



for i in range(200):
    newBox=[random.randint(mapxpos+500,mapxpos+9500),random.randint(mapypos+500,mapypos+9500),random.randint(1,10)]
    lootBoxLIST.append(newBox)#x , y  , item


################Loading boat images
for i in range(53):
    boatIMG=(pygame.image.load(str("q"+str(i+1)+".png")).convert_alpha())
    imageLIST.append(boatIMG)

    enemyImage=(pygame.image.load(str("q"+str(i+1)+".png")).convert_alpha())
    for x in range(enemyImage.get_size()[0]):
        for y in range(enemyImage.get_size()[1]):
            if enemyImage.get_at([x, y]) == (255,255,255):
                enemyImage.set_at([x, y], (0,0,0))

    enemyImageLIST.append(enemyImage) 
    if i ==6:
            imageLIST.append(boatIMG)
            enemyImageLIST.append(enemyImage)
    elif i==14:
        for t in range(5):
            imageLIST.append(boatIMG)
            enemyImageLIST.append(enemyImage)
    elif i==16:
        for t in range(5):
            imageLIST.append(boatIMG)
            enemyImageLIST.append(enemyImage)
    elif i==17:
        for t in range(5):
            imageLIST.append(boatIMG)
            enemyImageLIST.append(enemyImage)
    elif i ==19:
        for t in range(2):
            imageLIST.append(boatIMG)
            enemyImageLIST.append(enemyImage)
    elif i==34:
        for t in range(20):
            imageLIST.append(boatIMG)
            enemyImageLIST.append(enemyImage)
    elif i==49:
        for t in range(20):
            imageLIST.append(boatIMG)
            enemyImageLIST.append(enemyImage)
    elif i==50:
        for t in range(10):
            imageLIST.append(boatIMG)
            enemyImageLIST.append(enemyImage)
    elif i==52:
        for t in range(5):
            imageLIST.append(boatIMG)
            enemyImageLIST.append(enemyImage)










######Loading explosion 1 images
for i in range(7):
    explosionIMGLIST.append(pygame.image.load(str("ex"+str(i+1)+".png")).convert_alpha())

            

def showBoat(xpos,ypos,angle,big):##Big to check if it is big one on menu
    if cycle<1000:
        if (angle<=45 and angle>=0) or (angle>325 ):
            displaysurf.blit(shadright,(xpos+20,ypos))
            
        elif (angle>45 and angle<=135):
            displaysurf.blit(shadup,(xpos+20,ypos))
        elif(angle>135 and angle<=225):
            displaysurf.blit(shadleft,(xpos+20,ypos))
        elif(angle>225 and angle<=325):
            displaysurf.blit(shaddown,(xpos+20,ypos))






        
        
        

    number=0
    yposPICTURE=ypos
    for pic in imageLIST:
        orig_rect=imageLIST[number].get_rect()
        rot_image=pygame.transform.rotate(imageLIST[number],angle-90)
        rot_rect=orig_rect.copy()
        rot_rect.center=rot_image.get_rect().center
        rot_image=rot_image.subsurface(rot_rect).copy()
        if big==True:
            rot_image=pygame.transform.scale(rot_image,(600,450))

            
        displaysurf.blit(rot_image,(xpos,yposPICTURE))
        if big==True:
            yposPICTURE-=4
        yposPICTURE-=1
        number+=1


def shoot1():##use 2d list bulletLISTto store x,y,anlge and speed
    global fireShot,enemyLIST,health
    number=0
    if fireShot==True:
        shoot.play()
        bulletLIST.append([xpos+50,ypos+50,angle+90,20,1,0])
        bulletLIST.append([xpos+50,ypos+50,angle+100,20,1,0])
        bulletLIST.append([xpos+50,ypos+50,angle+80,20,1,0])

        bulletLIST.append([xpos+50,ypos+50,angle-90,20,1,0])
        bulletLIST.append([xpos+50,ypos+50,angle-100,20,1,0])
        bulletLIST.append([xpos+50,ypos+50,angle-80,20,1,0])
        
        fireShot=False
    for bullets in bulletLIST:
        bulletGone=False
        pygame.draw.circle(displaysurf,(0,0,0),(int(bulletLIST[number][0]),int(bulletLIST[number][1])),5,0)##Moving and removing bullets
        bulletLIST[number][0]+=bulletLIST[number][3]*math.cos(math.radians(bulletLIST[number][2]))
        bulletLIST[number][1]-=bulletLIST[number][3]*math.sin(math.radians(bulletLIST[number][2]))
        bulletLIST[number][3]-=0.1
        numberEnemy=0
        for badbois in range(len(enemyLIST)):
            box=pygame.Rect((enemyLIST[numberEnemy][0])+20,(enemyLIST[numberEnemy][1])+20,80,80)
            boxPlayer=pygame.Rect(xpos+30,ypos+30,40,40)##Detect player being hit
            
            if box.collidepoint(bulletLIST[number][0],bulletLIST[number][1]) and  bulletLIST[number][4]==1:##Detecting shot hitting enemy
                blast.play()
                newText=[bulletLIST[number][0],bulletLIST[number][1],bulletLIST[number][1],str(allocatedDamage),(255,0,0)]
                upwardTextLIST.append(newText)
                newExplosion=[bulletLIST[number][0],bulletLIST[number][1],0,False]
                explosionLIST.append(newExplosion)
                enemyLIST[numberEnemy][3]-=allocatedDamage
                bulletLIST.pop(number)
                bulletGone=True
            numberEnemy+=1

        if bulletGone==False:
            if boxPlayer.collidepoint(bulletLIST[number][0],bulletLIST[number][1]) and bulletLIST[number][4]==0:#########BULLET LIST USES 5RD ITEM 0 for enemy 1 for player bullet
                blast.play()
                newExplosion=[bulletLIST[number][0],bulletLIST[number][1],0,False]
                explosionLIST.append(newExplosion)
                if defend==True:
                    damage=(bulletLIST[number][5])*0.25
                    health-=damage
                    newText=[bulletLIST[number][0],bulletLIST[number][1],bulletLIST[number][1],str(damage),(255,0,0)]
                    upwardTextLIST.append(newText)
                    pygame.draw.rect(displaysurf,(255,255,0),(0,0,1600,900),0)
                    ting.play()
                else:
                    health-=bulletLIST[number][5]
                    newText=[bulletLIST[number][0],bulletLIST[number][1],bulletLIST[number][1],str(bulletLIST[number][5]),(255,0,0)]
                    upwardTextLIST.append(newText)
                    pygame.draw.rect(displaysurf,(255,0,0),(0,0,1600,900),0)
                bulletLIST.pop(number)
                bulletGone=True
            


        
        try:
            if bulletLIST[number][3]<18:
                bulletLIST.pop(number)
        except:
            number=number


        number+=1

def enemies():
    global enemyLIST,money,explosionLIST,upwardTextLIST,lootBoxLIST,bulletLIST
    enemyNumber=0
    move=True
    for badBois in enemyLIST:
        
        number=0
        enemypos=enemyLIST[number][1]
        angleEnemy=90+360-math.atan2(enemypos-ypos,enemyLIST[enemyNumber][0]-xpos)*180/math.pi






            
        if enemyLIST[number][3]<=(enemyLIST[number][4])*10 and enemyLIST[number][3]>((enemyLIST[number][4])*10)/2:
            pygame.draw.rect(displaysurf,(255,255,0),(enemyLIST[number][0],enemyLIST[number][1]-50,10*enemyLIST[number][3],5))
        elif enemyLIST[number][3]<=((enemyLIST[number][4])*10)/2 and enemyLIST[number][3]>((enemyLIST[number][4])*10)/5:
            pygame.draw.rect(displaysurf,(255,165,0),(enemyLIST[number][0],enemyLIST[number][1]-50,10*enemyLIST[number][3],5))
        else:
            pygame.draw.rect(displaysurf,(255,0,0),(enemyLIST[number][0],enemyLIST[number][1]-50,10*enemyLIST[number][3],5))
        pygame.draw.rect(displaysurf,(0,0,0),(enemyLIST[number][0],enemyLIST[number][1]-50,((enemyLIST[number][4])*100),5),2)
        lvltext = fontObj.render(str("Level")+str(enemyLIST[number][4]), True, (0,0,0))
        displaysurf.blit(lvltext,(enemyLIST[number][0]+20,enemyLIST[number][1]-75))
                                                   
        if screen.collidepoint(enemyLIST[number][0],enemyLIST[number][1]):

            ##fighting player
            playerbox=pygame.Rect(xpos-300,ypos-300,700,700)
            smallplayerbox=pygame.Rect(xpos,ypos,100,100)
            if playerbox.collidepoint(enemyLIST[enemyNumber][0],enemyLIST[enemyNumber][1]):##Moved here so can change angle
                move=False
                angleEnemy=180+360-math.atan2(enemypos-ypos,enemyLIST[enemyNumber][0]-xpos)*180/math.pi

                angleEnemyAdd=random.randint(-20,20)
                enemyLIST[enemyNumber][2]+=1
                if enemyLIST[enemyNumber][2]>=90:
                    shoot.play()
                    bulletLIST.append([enemyLIST[enemyNumber][0]+50,enemyLIST[enemyNumber][1]+50,angleEnemy+angleEnemyAdd,20,0,(enemyLIST[number][4])*2])##Extra value is damage
                    bulletLIST.append([enemyLIST[enemyNumber][0]+50,enemyLIST[enemyNumber][1]+50,angleEnemy+10+angleEnemyAdd,20,0,(enemyLIST[number][4])*2])
                    bulletLIST.append([enemyLIST[enemyNumber][0]+50,enemyLIST[enemyNumber][1]+50,angleEnemy-10+angleEnemyAdd,20,0,(enemyLIST[number][4])*2])

                    bulletLIST.append([enemyLIST[enemyNumber][0]+50,enemyLIST[enemyNumber][1]+50,angleEnemy+180+angleEnemyAdd,20,0,(enemyLIST[number][4])*2])
                    bulletLIST.append([enemyLIST[enemyNumber][0]+50,enemyLIST[enemyNumber][1]+50,angleEnemy+190+angleEnemyAdd,20,0,(enemyLIST[number][4])*2])
                    bulletLIST.append([enemyLIST[enemyNumber][0]+50,enemyLIST[enemyNumber][1]+50,angleEnemy+170+angleEnemyAdd,20,0,(enemyLIST[number][4])*2])
                    enemyLIST[enemyNumber][2]=0
            angleEnemy2=angleEnemy-270
            if cycle<1000:
                if (angleEnemy2<=45 and angleEnemy2>=0) or (angleEnemy2>325 ):
                    displaysurf.blit(shadright,(enemyLIST[number][0]+20,enemyLIST[number][1]))
                    
                elif (angleEnemy2>45 and angleEnemy2<=135):
                    displaysurf.blit(shadup,(enemyLIST[number][0]+20,enemyLIST[number][1]))
                elif(angleEnemy2>135 and angleEnemy2<=225):
                    displaysurf.blit(shadleft,(enemyLIST[number][0]+20,enemyLIST[number][1]))
                elif(angleEnemy2>225 and angleEnemy2<=325):
                    displaysurf.blit(shaddown,(enemyLIST[number][0]+20,enemyLIST[number][1]))
            if smallplayerbox.collidepoint(enemyLIST[enemyNumber][0],enemyLIST[enemyNumber][1]):
                if xpos<enemyLIST[enemyNumber][0]:
                    enemyLIST[enemyNumber][0]+=2##Move FROM player fast
                elif xpos>enemyLIST[enemyNumber][0]:
                    enemyLIST[enemyNumber][0]-=2

                if ypos<enemyLIST[enemyNumber][1]:
                    enemyLIST[enemyNumber][1]+=2##Move FROM player fast
                elif ypos>enemyLIST[enemyNumber][1]:
                    enemyLIST[enemyNumber][1]-=2
            
            for pics in enemyImageLIST:
                #image=pygame.transform.scale(imageLIST[number],(130,140))
                image=pygame.transform.rotate(enemyImageLIST[number],angleEnemy)
                displaysurf.blit(image,(enemyLIST[enemyNumber][0],enemypos))
                enemypos-=1
                number+=1



        if move==True:
            if xpos<enemyLIST[enemyNumber][0]:
                enemyLIST[enemyNumber][0]-=1##Move enemies to player
            elif xpos>enemyLIST[enemyNumber][0]:
                enemyLIST[enemyNumber][0]+=1

            if ypos<enemyLIST[enemyNumber][1]:
                enemyLIST[enemyNumber][1]-=1##Move enemies to player
            elif ypos>enemyLIST[enemyNumber][1]:
                enemyLIST[enemyNumber][1]+=1
        box=pygame.Rect((enemyLIST[enemyNumber][0])+20,(enemyLIST[enemyNumber][1])+20,80,80)##Gets enemy rect
        if enemyLIST[enemyNumber][3]<=0:

                     
            newExplosion=[(enemyLIST[enemyNumber][0]),(enemyLIST[enemyNumber][1]),0,True]
            explosionLIST.append(newExplosion)
            newBox=[enemyLIST[enemyNumber][0]+20,enemyLIST[enemyNumber][1]+20,random.randint(20,40)]
            lootBoxLIST.append(newBox)#x , y  , item
            enemyLIST.pop(enemyNumber)

            for i in range(1):
                
                if mapxpos>=-2900 and mapypos>=-4190:
                    newEnemy=[random.randint(200,1000),random.randint(200,1000),0,10,1]
                elif mapxpos<-2900 and mapxpos>=-5660 and mapypos>=-2280:
                   newEnemy=[random.randint(200,1000),random.randint(200,1000),0,20,2]
                elif mapxpos<-2900 and mapxpos>=-5660 and mapypos<-2280 and mapypos>=-4206:
                   newEnemy=[random.randint(200,1000),random.randint(200,1000),0,30,3]
                   
                enemyLIST.append(newEnemy)


                
        elif clicked==True and box.collidepoint(mousex,mousey) and lightningPower==True:

            displaysurf.blit(lightning,(mousex-200,mousey-1000))
            newExplosion=[(enemyLIST[enemyNumber][0]),(enemyLIST[enemyNumber][1]),0,True]
            explosionLIST.append(newExplosion)
            newBox=[enemyLIST[enemyNumber][0]+20,enemyLIST[enemyNumber][1]+20,random.randint(20,40)]
            lootBoxLIST.append(newBox)#x , y  , item
            enemyLIST.pop(enemyNumber)

            for i in range(1):
                
                if mapxpos>=-2900 and mapypos>=-4190:
                    newEnemy=[random.randint(200,1000),random.randint(200,1000),0,10,1]
                elif mapxpos<-2900 and mapxpos>=-5660 and mapypos>=-2280:
                   newEnemy=[random.randint(200,1000),random.randint(200,1000),0,20,2]
                elif mapxpos<-2900 and mapxpos>=-5660 and mapypos<-2280 and mapypos>=-4206:
                   newEnemy=[random.randint(200,1000),random.randint(200,1000),0,30,3]
                   
                enemyLIST.append(newEnemy)



def islandFunc():
    global colourBoat
    displaysurf.blit(island,(mapxpos+2000,mapypos+2000))
    
    colourBoat=pygame.transform.scale(colourBoat,(150,300))
    displaysurf.blit(colourBoat,(mapxpos+2000,mapypos+4000))





def gui():
    global allocatedMove,allocatedDamage,allocatedReload
    ##Night
    #skyPic.set_alpha(200)
    #displaysurf.blit(skyPic,(0,0))
    guiPic=pygame.transform.scale(gui1Pic,(400,400))##All gui stuff
    angleLoad=reloadTimer
    angleLoad%=360
    if angleLoad>0:
        if reloadTimer>=(90-(allocatedReload*5)):
            pygame.draw.arc(displaysurf,(0,255,0),(12,645,250,250),math.radians(0),math.radians(angleLoad)*4.45,20)
        else:
            pygame.draw.arc(displaysurf,(255,210,0),(12,645,250,250),math.radians(0),math.radians(angleLoad)*4.45,20)
            
    displaysurf.blit(guiPic,(1,580))##Left corner
    



    
    displaysurf.blit(map1, (65,695),(-20-(mapxpos/12),-10-(mapypos/12), 150,150))

    arrowsAngle=angle-90
    arrowIMG=pygame.transform.rotate(arrow1,arrowsAngle)##Arrow
    arrowIMG=pygame.transform.scale(arrowIMG,(20,20))
    displaysurf.blit(arrowIMG,(130,750))
    
    pygame.draw.rect(displaysurf,(0,255,0),(xpos,ypos-50,10*health,5))##Player health bar
    pygame.draw.rect(displaysurf,(0,0,0),(xpos,ypos-50,10*maxHealth,5),2)
    if defend==True:
        displaysurf.blit(shield,(xpos,ypos-150))

    displaysurf.blit(boatPic,(1400,700))##Shows boat cross-section
    
    movementRoomRECT=pygame.Rect(1470,762,28,87)
    cannonRoomRECT=pygame.Rect(1500,762,28,87)
    reloadRoomRECT=pygame.Rect(1475,740,47,20)
    healRoomRECT=pygame.Rect(1490,725,20,18)

    barxpos=1430
    barypos=850
    crewNumber=0
    moreNeeded=False
    allocatedTotal=allocatedMove+allocatedDamage+allocatedReload
    displaysurf.blit(allocationtext,(1420,875))
    
    if movementRoomRECT.collidepoint(mousex,mousey):
        pygame.draw.rect(displaysurf,(255,255,255),movementRoomRECT,4)##Movemnt crew
        displaysurf.blit(movetext,(1350,840))
        for i in range(speed):
            if crewNumber<allocatedMove:
                pygame.draw.rect(displaysurf,(0,255,0),(barxpos,barypos,20,10),0)
            else:
                moreNeeded=True
            pygame.draw.rect(displaysurf,(0,0,0),(barxpos,barypos,20,10),2)
            barypos-=10
            crewNumber+=1
        if clicked==True and moreNeeded==True and allocatedTotal<crew:
            allocatedMove+=1

            
    elif cannonRoomRECT.collidepoint(mousex,mousey):
        pygame.draw.rect(displaysurf,(255,255,255),cannonRoomRECT,4)##Damage Crew
        displaysurf.blit(damagetext,(1340,840))
        for i in range(damage):
            if crewNumber<allocatedDamage:
                pygame.draw.rect(displaysurf,(255,0,0),(barxpos,barypos,20,10),0)
            else:
                moreNeeded=True
            pygame.draw.rect(displaysurf,(0,0,0),(barxpos,barypos,20,10),2)
            barypos-=10
            crewNumber+=1
        if clicked==True and moreNeeded==True and allocatedTotal<crew:
            allocatedDamage+=1
            
    elif reloadRoomRECT.collidepoint(mousex,mousey):
        pygame.draw.rect(displaysurf,(255,255,255),reloadRoomRECT,4)##Reload Crew
        displaysurf.blit(reloadtext,(1350,840))
        for i in range(round((100-reloadTime)/5)):
            if crewNumber<allocatedReload:
                pygame.draw.rect(displaysurf,(128,0,128),(barxpos,barypos,20,10),0)
            else:
                moreNeeded=True
            pygame.draw.rect(displaysurf,(0,0,0),(barxpos,barypos,20,10),2)
            barypos-=10
            crewNumber+=1
        if clicked==True and moreNeeded==True and allocatedTotal<crew:
            allocatedReload+=1
            
    elif healRoomRECT.collidepoint(mousex,mousey):
        pygame.draw.rect(displaysurf,(255,255,255),healRoomRECT,4)


        
    
def mapOpen():
    mapShow=True
    while mapShow==True:
        displaysurf.blit(map1,(400,50))
        pygame.draw.rect(displaysurf,(0,0,0),(450-(mapxpos/12),100-(mapypos/12),5,5),0)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_m:
                    mapShow=False
        pygame.display.update()




def shop():
    global mapxpos,mapypos,angle,mousex,mousey,balls,money,speed,health,damage,lightningPower,maxHealth,reloadTime,crew
    box=pygame.Rect((mapxpos+2000,mapypos+2000,1000,550))
    if box.collidepoint(xpos,ypos) :##Detecting boat on island
        mapxpos=-1200
        mapyos=-1900
        angle=180
        shopOpen=True
        while shopOpen==True:
            clicked=False
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.MOUSEMOTION:
                    mousex,mousey=event.pos
                elif event.type==pygame.MOUSEBUTTONUP:
                    mousex,mousey=event.pos
                    clicked=True
            shopPic.set_alpha(10)
            displaysurf.blit(shopPic,(300,150))
            
            displaysurf.blit(closePic,(1250,180))
            displaysurf.blit(ballsPic,(500,350))
            displaysurf.blit(speedPic,(500,420))
            displaysurf.blit(healthPic,(500,490))
            displaysurf.blit(damagePic,(500,560))
            displaysurf.blit(hpPic,(500,630))
            displaysurf.blit(lightPic,(700,350))
            displaysurf.blit(reloadPic,(700,420))
            displaysurf.blit(crewPic,(700,490))
            
            ballsRect=pygame.Rect(500,350,50,50)
            closeRect=pygame.Rect(1250,180,20,20)
            speedRect=pygame.Rect(500,420,50,50)
            healthRect=pygame.Rect(500,490,50,50)
            damageRect=pygame.Rect(500,560,50,50)
            hpRect=pygame.Rect(500,630,50,50)
            lightRect=pygame.Rect(700,350,50,50)
            reloadRect=pygame.Rect(700,420,50,50)
            crewRect=pygame.Rect(700,490,50,50)
            
            moneytext = fontObj.render(str("Money: "+str(money)+str("C")), True, (0,0,0))
            displaysurf.blit(moneytext,(400,283))
            balltext = fontObj.render(str("Balls: "+str(balls)), True, (0,0,0))##Display text to shop
            displaysurf.blit(balltext,(700,283))
            hptext = fontObj.render(str("Health: "+str(health)+str("/")+str(maxHealth)), True, (0,0,0))##Display text to shop
            displaysurf.blit(hptext,(1000,283))
    
            displaysurf.blit(buyballtext,(400,370))
            
            displaysurf.blit(buyspeedtext,(390,440))

            displaysurf.blit(buyhealthtext,(400,510))

            displaysurf.blit(buydamagetext,(400,580))

            displaysurf.blit(buyhptext,(390,650))

            displaysurf.blit(buylighttext,(580,370))

            displaysurf.blit(buyreloadtext,(580,440))

            displaysurf.blit(buycrewtext,(580,510))
            
            if clicked==True:
                if closeRect.collidepoint(mousex,mousey):
                    shopOpen=False
                    ting.play()
                elif ballsRect.collidepoint(mousex,mousey) and money>=2:
                    balls+=10
                    money-=2
                    ting.play()
                elif speedRect.collidepoint(mousex,mousey) and money>=100:
                    speed+=1
                    money-=100
                    ting.play()
                elif healthRect.collidepoint(mousex,mousey) and money>=2 and health<maxHealth:
                    health+=1
                    money-=2
                    if health>maxHealth:
                        health=maxHealth
                    ting.play()
                elif damageRect.collidepoint(mousex,mousey) and money>=100:
                    damage+=1
                    money-=100
                    ting.play()
                elif hpRect.collidepoint(mousex,mousey) and money>=50:
                    maxHealth+=1
                    money-=50
                    ting.play()
                elif lightRect.collidepoint(mousex,mousey) and money>=1000 and lightningPower==False:
                    lightningPower=True
                    money-=1000
                    ting.play()
                elif reloadRect.collidepoint(mousex,mousey) and money>=100:
                    reloadTime-=5
                    money-=100
                    ting.play()
                elif crewRect.collidepoint(mousex,mousey) and money>=50:
                    crew+=1
                    money-=50
                    ting.play()


                
            pygame.display.update()
            clock.tick(40)

            
def recolour(old,new):
    global imageLIST
    number=0
    for i in imageLIST:
        for x in range(imageLIST[number].get_size()[0]):
            for y in range(imageLIST[number].get_size()[1]):
                if imageLIST[number].get_at([x, y]) == old:
                    imageLIST[number].set_at([x, y], new)
        number+=1






    

def colourShop():
    global mapxpos,mapypos,sailSetColour,boatSetColour,cannonsSetColour,floorSetColour
    colourPart=(255,255,255)
    newColour=(0,0,0)
    box=pygame.Rect((mapxpos+2000,mapypos+4000,150,300))
    if box.collidepoint(xpos,ypos) :##Detecting boat on island
        mapxpos=-1900
        mapyos=-4000
        angle=180
        shopOpen=True
        part="sail"
        while shopOpen==True:
            clicked=False
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.MOUSEMOTION:
                    mousex,mousey=event.pos
                elif event.type==pygame.MOUSEBUTTONUP:
                    mousex,mousey=event.pos
                    clicked=True
            shopPic.set_alpha(10)
            displaysurf.blit(shopPic,(300,150))


            displaysurf.blit(closePic,(1250,180))
            displaysurf.blit(sailColour,(368,320))
            displaysurf.blit(boatColour,(428,320))
            displaysurf.blit(floorColour,(488,320))
            displaysurf.blit(cannonsColour,(548,320))
            showBoat(450,450,0,False)



            
            colourLIST=[(255,0,0),(0,255,0),(0,0,255),(0,0,0),(255,255,255),(159,115,42),(64,34,1),(50,50,50),(150,150,150),(255,255,0),(128,0,128),(205,105,180),(253,106,2),(249,166,2),(80,208,255)]
            numberColour=0
            colourx=700
            coloury=400
            for i in range(3):
                for i in range(5):
                    pygame.draw.rect(displaysurf,colourLIST[numberColour],(colourx,coloury,50,50),0)
                    colourRect=pygame.Rect(colourx,coloury,50,50)
                    if clicked==True and colourRect.collidepoint(mousex,mousey):
                        if  sailSetColour!=colourLIST[numberColour] and boatSetColour!=colourLIST[numberColour] and cannonsSetColour!=colourLIST[numberColour] and floorSetColour!=colourLIST[numberColour]:
                            recolour(colourPart,colourLIST[numberColour])
                            if part=="sail" :
                                sailSetColour=colourLIST[numberColour]
                            elif part=="boat":
                                boatSetColour=colourLIST[numberColour]
                            elif part=="cannons":
                                cannonsSetColour=colourLIST[numberColour]
                            elif part=="floor":
                                floorSetColour=colourLIST[numberColour]
                    coloury+=60
                    numberColour+=1
                colourx+=60
                coloury=400
                    

    
            closeRect=pygame.Rect(1250,180,20,20)
            sailRect=pygame.Rect(368,320,50,30)
            boatRect=pygame.Rect(428,320,50,30)
            floorRect=pygame.Rect(488,320,50,30)
            cannonsRect=pygame.Rect(548,320,50,30)
            redRect=pygame.Rect(700,400,50,50)



            #0,0,0    159,115,42          000      64,34,1


            if clicked==True:
                        if closeRect.collidepoint(mousex,mousey):
                            shopOpen=False
                        if sailRect.collidepoint(mousex,mousey):
                            part="sail"
                        if boatRect.collidepoint(mousex,mousey):
                            part="boat"
                        if cannonsRect.collidepoint(mousex,mousey):
                            part="cannons"
                        if floorRect.collidepoint(mousex,mousey):
                            part="floor"
                            
            if part=="sail":
                colourPart=sailSetColour
            elif part=="boat":
                colourPart=boatSetColour
            elif part=="cannons":
                colourPart=cannonsSetColour
            elif part=="floor":
                colourPart=floorSetColour


                        

















            pygame.display.update()
            clock.tick(40)    
    
def water2():
    for i in range(50):
        for t in range(50):
            displaysurf.blit(water,(mapxpos+(i*200),mapypos+(t*200)))

def onBoatFunction():
    global onBoat
    while onBoat==True:   
        displaysurf.fill((0,191,255))
        for i in range(20):
            for t in range(10):
                displaysurf.blit(water,(i*200,400+t*200))
        enemyNumber=0
        for badBois in enemyLIST:
            number=0
            enemypos=enemyLIST[number][1]
            angleEnemy=90+360-math.atan2(0,0)*180/math.pi
            for pics in imageLIST:
                image=pygame.transform.scale(imageLIST[number],(600,800))
                image=pygame.transform.rotate(image,angleEnemy)
                displaysurf.blit(image,(0,enemypos))
                enemypos-=10
                number+=1
            enemyNumber+=1
                
        displaysurf.blit(onBoatPic,(0,0))
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_o:
                    onBoat=False
        pygame.display.update()





def explosions():
    global explosionLIST
    explodeNUM=0
    if len(explosionLIST)>0:
        for explodes in explosionLIST:
            IMG=explosionIMGLIST[explosionLIST[explodeNUM][2]]
            if explosionLIST[explodeNUM][3]==True:
                IMG=pygame.transform.scale(IMG,(100,100))
                
            displaysurf.blit(IMG,(explosionLIST[explodeNUM][0],explosionLIST[explodeNUM][1]))
            explosionLIST[explodeNUM][2]+=1
            if explosionLIST[explodeNUM][2]==6:
                explosionLIST.pop(explodeNUM)
            explodeNUM+=1



def upwardText():
    global upwardTextLIST
    textsNumber=0
    if len(upwardTextLIST)>0:
        for texts in upwardTextLIST:
            text = fontObj.render(str(upwardTextLIST[textsNumber][3]), True, upwardTextLIST[textsNumber][4])
            displaysurf.blit(text,(upwardTextLIST[textsNumber][0],upwardTextLIST[textsNumber][1]))
            upwardTextLIST[textsNumber][1]-=2
            if upwardTextLIST[textsNumber][2]-upwardTextLIST[textsNumber][1]>=50:
                upwardTextLIST.pop(textsNumber)
            textsNumber+=1
        

def lootBoxFunction():
    global money,lootBoxLIST
    number=0
    if len(lootBoxLIST)>0:
        for boxes in lootBoxLIST:
            displaysurf.blit(lootBoxPic,(lootBoxLIST[number][0],lootBoxLIST[number][1]))
            boxRect=pygame.Rect(lootBoxLIST[number][0]-20,lootBoxLIST[number][1]-20,40,40)
            lootBoxLIST[number][0]-=allocatedMove*math.cos(math.radians(angle))
            lootBoxLIST[number][1]+=allocatedMove*math.sin(math.radians(angle))
            
            if boxRect.collidepoint(xpos+30,ypos+30):
                money+=lootBoxLIST[number][2]
                newText=[xpos+30,ypos,ypos,str("+")+str(lootBoxLIST[number][2]),(255,255,0)]
                upwardTextLIST.append(newText)
                lootBoxLIST.pop(number)
            number+=1

def night():
    global cycle
    if cycle>1000:
        displaysurf.blit(skyPic,(0,0))

    if cycle>1200:
        cycle=0

def lightRay():
    displaysurf.blit(sunRay,((cycle*1.7)-200,100))

while True:
    cycle+=1
    clicked=False
    number=0
    if reloadTimer<(90-(allocatedReload*5)) and defend==False:
        reloadTimer+=1
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_d:
                angleIN=-2
            if event.key==K_a:
                angleIN=2
            if event.key==K_w:
                menu=False
            if event.key==K_SPACE and balls>=6 and reloadTimer>=(90-(allocatedReload*5)):
                fireShot=True
                balls-=6
                reloadTimer=0
            if event.key==K_p:
                money+=100
            if event.key==K_m:
                mapOpen()
            if event.key==K_o:
                onBoat=True
                onBoatFunction()
            if event.key==K_c:
                defend=True
        if event.type==pygame.MOUSEMOTION:
            mousex,mousey=event.pos
        elif event.type==pygame.MOUSEBUTTONUP:
            mousex,mousey=event.pos
            clicked=True
        if event.type==KEYUP:
            if event.key==K_d or event.key==K_a:
                angleIN=0
            if event.key==K_c:
                defend=False

    if menu==True:
        displaysurf.fill((30,144,255))
        showBoat(500,500,angleMenu,True)
        displaysurf.blit(wPic,(900,750))
        angleMenu+=1
        displaysurf.blit(titlePic,(-75,-200))
        pygame.display.update()


    else:
        
        enemyNumber=0
        mapxpos-=allocatedMove*math.cos(math.radians(angle))
        mapypos+=allocatedMove*math.sin(math.radians(angle))
        for i in enemyLIST:
            enemyLIST[enemyNumber][0]-=allocatedMove*math.cos(math.radians(angle))
            enemyLIST[enemyNumber][1]+=allocatedMove*math.sin(math.radians(angle))
            enemyNumber+=1
        ######Stopping enemy at edge
            
        if mapypos>0:
            mapypos-=allocatedMove
        elif mapypos<-9100:
            mapypos+=allocatedMove

        if mapxpos>0:
            mapxpos-=allocatedMove
        elif mapxpos<-8400:
            mapxpos+=allocatedMove

        
        angle+=angleIN
        angle%=360

        if health<=0:
            enemyLIST=[[100,100,0,10,1]]
            mapxpos=-2000
            mapypos=-2000
            health=maxHealth
            money=0
            balls=120
            displaysurf.fill((0,0,0))
            dietext = fontObj.render(str("You Died"), True, (255,255,255))
            displaysurf.blit(dietext,(800,450))
            pygame.display.update(updateRect)
            time.sleep(3)
        
            
        water2()
        lightRay()
        lootBoxFunction()
        enemies()
        shoot1()
        islandFunc()
        showBoat(xpos,ypos,angle,False)
        explosions()
        night()
        upwardText()
        gui()
        shop()
        colourShop()
        
        ##TEXT AT GUI
        allocatedTotal=allocatedMove+allocatedDamage+allocatedReload
        
        moneytext = fontObj.render(str(money), True, (255,215,0))
        displaysurf.blit(moneytext,(280,697))
        moneytext = fontObj.render(str(balls), True, (255,215,0))
        displaysurf.blit(moneytext,(290,762))
        crewtext = fontObj.render(str(allocatedTotal)+str("/")+str(crew), True, (255,215,0))
        displaysurf.blit(crewtext,(280,827))
        speedtext = fontObj.render((str(allocatedMove*3)+str(" Knots")), True, (255,255,255))
        displaysurf.blit(speedtext,(102,850))
        
        #healthtext = fontObj.render(str("Health: "+str(health)), True, (255,0,0))
        #displaysurf.blit(healthtext,(1000,10))
        
        fpstext = fontObj.render(str(int(clock.get_fps())), True, (255,215,0))
        displaysurf.blit(fpstext,(10,10))

         
        updateRect=(0,0,1600,900)
        pygame.display.update()
        clock.tick(40)




############################Add how to play. Space to shoot. A D to turn. Hold c to defend but cant reload.

##Let player stand on boat  meh
        
##Add islands

##Add Inventory

##FIX map

##Make boat speed up and slow down

##Make sik GUI        MEH

##Add player death                DONE

##Add reload time            DONE

##Boat sink animations!!!!!    DONE


##spawn bads by map pos
        ##sort out ai fighting--------------let enemy shoot---------    DONE
        ##Add health                     DONE
        ##allow multiple boats at once
        ##Add animations to them
        ##Add Levels of boats
        ##Add special enemies



##Turn enemy                           DONE
##Let me shoot boat                   DONE
##Give boat AI                                   DONE
##Add money+buying system       DONE         Speed,Acceleration
##Add islands                                   DONE    -----------------------------------------      
##Add water effects
##Add explosions + sinking_-----------------------------------------------------DONE
##Add menu and saving or such           MEH        
##Add quests
##Sort ai spawning 
##Spawn Level of boats depending on where player is
##White boxes on shop items
##Display more stats  DONE
##Random boxes of loot  LOOT BOX?                       DONE
##Make objects stay when at wall edge
##Add text of reward from kill                              DONE
##Add shadows


"""things to buy
turn speed----------------------
maximum health---------------DONE
crew members
food
reload time-------------------DOne
acceleration
special weapons
special ammo
defence Effect--------------
"""

##UP text                                             DONE

##Add defence room




###Crew deaths in fights

##Islands u can buy and trade

##Food counter


##Let player change sail colour and whole boat parts    DONE


##Flood cross section. Click to rid

##Add removing crew----------------------------sort fighting mainly--------------------

##Make reload change by 5 and cost 1 crew YH

##Shield instead of defending text YH


##Add special weapons

##Add perks/items/inventory

##Stop player colouring parts of boat da same  DONE


##Make music load w enemies quite in shops

##Add cannon range/speed













