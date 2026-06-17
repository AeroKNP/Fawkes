import numpy as np
from include import constants as cons
from include.mixer import get_rpm
from src.gravity import gravity
from src.guidance import guidance

phase="IDLE"

# This is the controller responsible to calculate the required RPMs at any point of time
def contorller_output(t,state,extra_paras=None):

    extra=extra_paras[0:3]
    dt=extra_paras[2]
    motors=extra_paras[3]
    Cascade=extra_paras[4]

    # Updating the mission phase based on the current state and target state
    update_mission_phase(state,extra[0])

    # Getting the net acceleration required in the global frame
    req_state_deri=guidance(phase,t,state,extra)-gravity(t,state)
    anet=np.array([req_state_deri.vx,req_state_deri.vy,req_state_deri.vz])

    # Converting to body frame
    Anet=cons.global_to_body_matrix(state.phi,state.theta,state.psi)@anet

    # Calculate magnitude of the required acceleration
    anet_mag = np.linalg.norm(Anet)

    # Getting the error vector
    error_vec = np.array([-Anet[1], Anet[0], 0.0])

    # Getting required torque based on the error vector
    Torque=Cascade.run_cascade(error_vec,state,dt)

    # Getting the required RPMs based on the required torque and thrust
    Thrust=anet_mag*cons.mass
    RPMs=get_rpm(Thrust,Torque,motors)

    return RPMs

# This function updates the mission phase based on the current state and target state
def update_mission_phase(state,target_state):

    # Unpacking the variables
    global phase

    vM=np.array([state.vx,state.vy,state.vz])
    rT=np.array([target_state[0],target_state[1],target_state[2]])
    rM=np.array([state.x,state.y,state.z])
    rTM=rT-rM

    cos_theta=np.dot(vM,rTM)/max((np.linalg.norm(vM)*np.linalg.norm(rTM)),cons.den_min)

    # If the drone is close to the ground and in IDLE or rise phase, switch to rise phase
    if state.z<0.5 and (phase=="IDLE" or phase=="rise"):
        phase="rise"
    
    # If the drone is in rise or pure pursuit phase
    elif(phase=="rise" or phase=="pure_pursuit"):
        # If the drone is well aligned with the target then check its speed else stay in pure pursuit phase
        if cos_theta>0.5:
            # If the drone is moving fast enough, switch to prop_nav phase, else switch to pure pursuit phase
            if np.linalg.norm(vM)>0.5:
                phase="prop_nav"
            else:
                phase="pure_pursuit"
        else:
            phase="pure_pursuit"

    # If the drone is in prop_nav phase then stay in prop_nav phase    
    else:
        phase="prop_nav"

