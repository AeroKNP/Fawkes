from src.kinematics import kinematics
from src.gravity import gravity
from src.environment import drag
from src.guidance import guidance

# Getting the total derivatives function
def derivatives(t,state,extra_paras=None):

    # total=kinematics(t,state)+gravity(t,state)+drag(t,state)+guidance(t,state,extra_paras)
    total = kinematics(t,state)+guidance(t,state,extra_paras)

    return total