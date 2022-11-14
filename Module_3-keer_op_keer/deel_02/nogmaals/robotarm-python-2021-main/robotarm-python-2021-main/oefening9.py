from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
# Jouw python instructies zet je vanaf hier:
for b in range(11):
    robotArm.grab()
    for t in range(1,6): robotArm.moveRight()
    robotArm.drop()
    for e in range(1,6):robotArm.moveLeft()
    if robotArm.grab() == False:
        robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
