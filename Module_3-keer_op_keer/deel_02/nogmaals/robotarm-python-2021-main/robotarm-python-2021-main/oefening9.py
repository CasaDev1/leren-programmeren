from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
# Jouw python instructies zet je vanaf hier:

skip_nummrers = [1,3,6,10]
for k in range(0,10):
    if k in skip_nummrers:
        robotArm.moveRight()
    robotArm.grab()
    for k in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for k in range(5):
        robotArm.moveLeft()
    

        
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
