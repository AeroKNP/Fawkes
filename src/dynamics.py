from src.kinematics import kinematics
from src.gravity import gravity
from src.environment import drag

# Getting the total derivatives function
def derivatives(t,state,extra_paras=None):

    total=kinematics(t,state)+gravity(t,state)+drag(t,state)

    return total