import numpy as np
from include import constants as cons
from include.mixer import get_rpm
from src.gravity import gravity
from src.guidance import guidance

# This is the controller responsible to calculate the required RPMs at any point of time
def contorller_output(t,state,extra_paras=None):

    extra=extra_paras[0:3]
    dt=extra_paras[2]
    motors=extra_paras[3]
    Cascade=extra_paras[4]

    # Getting the net acceleration required in the global frame
    req_state_deri=guidance(t,state,extra)-gravity(t,state)
    anet=np.array([req_state_deri.vx,req_state_deri.vy,req_state_deri.vz]) 

    # Converting to body frame
    Anet=cons.global_to_body_matrix(state.phi,state.theta,state.psi)@anet

    # Getting the error vector 
    error_vec=np.array([-Anet[1],Anet[0],0.0])

    # Getting required torque based on the error vector
    Torque=Cascade.run_cascade(error_vec,state,dt)

    # Getting the required RPMs based on the required torque and thrust
    RPMs=get_rpm(Anet[2],Torque,motors)

    return RPMs
