from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
# Jouw python instructies zet je vanaf hier:
q = 0
while q < 9:
    robotArm.grab()
    if robotArm.scan() == "white":
        q = q + 1
        robotArm.moveRight()
    robotArm.drop()
    robotArm.moveRight()
q = q + 1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
