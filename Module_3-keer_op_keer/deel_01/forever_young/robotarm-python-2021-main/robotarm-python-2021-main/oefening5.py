from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
for s in range(7):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for i in range(7):
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
