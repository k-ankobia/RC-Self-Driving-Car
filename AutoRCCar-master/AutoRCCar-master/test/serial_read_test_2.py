import serial #Import Serial Library
 
arduinoSerialData = serial.Serial('com3',115200) #Create Serial port object called arduinoSerialData
crashed = False 
 while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
	
		if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
			
		while (1==1):
		if (arduinoSerialData.inWaiting()>0):
			myData = arduinoSerialData.readline()
			print myData
		print(event)
		
		gameDisplay.fill(white)
    car(x,y)
        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()