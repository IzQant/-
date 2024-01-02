import os
import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
pandaUid = p.loadURDF(os.path.join(pybullet_data.getDataPath(),"franka_panda/panda.urdf"), useFixedBase=True)

for i in range(10000):
    p.stepSimulation()
    time.sleep(1 / 200)
