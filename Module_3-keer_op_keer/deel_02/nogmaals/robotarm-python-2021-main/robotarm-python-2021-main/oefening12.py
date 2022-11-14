from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
# Jouw python instructies zet je vanaf hier:
rechts = 9
links = 9
for u in range(9):
    robotArm.grab()
    if robotArm.scan() == "red":
        for t in range(rechts - u):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(links - u):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
