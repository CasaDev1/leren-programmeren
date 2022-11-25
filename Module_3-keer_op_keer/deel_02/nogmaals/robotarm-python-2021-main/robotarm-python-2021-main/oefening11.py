from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
# Jouw python instructies zet je vanaf hier:
for e in range(8):
    robotArm.moveRight()
q = 0
while q < 9:
    robotArm.grab()
    if robotArm.scan() == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
    if q == 8:
        q = 9
    else: 
        robotArm.moveLeft()
    q = q + 1


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
