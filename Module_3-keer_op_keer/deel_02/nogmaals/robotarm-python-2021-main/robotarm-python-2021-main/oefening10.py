from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
# Jouw python instructies zet je vanaf hier:
m = 9
e = 8
for t in range(5):
    robotArm.grab()
    for w in range(m):
        robotArm.moveRight()
    robotArm.drop()
    for q in range(e):
        robotArm.moveLeft()
    m = m - 2
    e = e - 2
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
