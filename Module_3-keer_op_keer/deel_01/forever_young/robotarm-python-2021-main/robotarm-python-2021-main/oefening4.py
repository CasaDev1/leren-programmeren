from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
for t in range(5):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    if t < 4:
        robotArm.moveLeft()
        robotArm.moveLeft()

for z in range(5):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()   

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
