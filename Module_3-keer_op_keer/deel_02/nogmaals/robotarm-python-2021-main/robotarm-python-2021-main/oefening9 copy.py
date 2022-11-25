from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
# Jouw python instructies zet je vanaf hier:


for e in range(1,5):
    for z in range(e):
        robotArm.grab()
        for i in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for c in range(5):
            robotArm.moveLeft()

    robotArm.moveRight()        
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
