from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
# Jouw python instructies zet je vanaf hier:
for y in range(1,6):
    for q in range(1,7):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for w in range(1,3):
        robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
