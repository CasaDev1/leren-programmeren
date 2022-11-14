from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for z in range(1,8):
    robotArm.grab()
    for i in range(1,9):
        robotArm.moveRight()
    robotArm.drop()
    for b in range(1,9):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
