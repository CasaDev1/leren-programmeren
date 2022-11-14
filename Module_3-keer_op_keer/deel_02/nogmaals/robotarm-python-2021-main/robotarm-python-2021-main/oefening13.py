from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
# Jouw python instructies zet je vanaf hier:
q = 1
while q < 9:
    robotArm.grab()
    if robotArm.scan() == "":
        break
    for w in range(q):
        robotArm.moveRight()
    robotArm.drop()
    for r in range(q):   
        robotArm.moveLeft()
    q = q + 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
