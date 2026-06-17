import numpy as np
from include import constants as cons
from include.state import State

# Constant
N=10.0

# Check the current mission phase and call the respective guidance function
def guidance(mission_phase,t,state,extra_paras):
    if mission_phase=="prop_nav":
        return prop_nav_guidance(t,state,extra_paras)
    elif mission_phase=="rise":
        return lift_off_guidance(t,state,extra_paras)
    elif mission_phase=="pure_pursuit":
        return pure_pursuit_guidance(t,state,extra_paras)

# Guidance function for lift off phase
def lift_off_guidance(t,state,extra_paras):
    return State([0.0,0.0,0.0,0.0,0.0,2.0,0.0,0.0,0.0,0.0,0.0,0.0])

# Guidance function for pure pursuit phase
def pure_pursuit_guidance(t,state,extra_paras):
    amag=2.0

    target_state=extra_paras[0]
    rT=np.array([target_state[0],target_state[1],target_state[2]])
    rM=np.array([state.x,state.y,state.z])
    rTM=rT-rM

    rhat=rTM/np.linalg.norm(rTM)

    dvxdt=amag*rhat[0]
    dvydt=amag*rhat[1]
    dvzdt=amag*rhat[2]

    return State([0.0,0.0,0.0,dvxdt,dvydt,dvzdt,0.0,0.0,0.0,0.0,0.0,0.0])

# Guidance function for proportional navigation
def prop_nav_guidance(t,state,extra_paras):
    # Unpacking the extra paras
    target_state=extra_paras[0]
    prev_target_state=extra_paras[1]
    dt=extra_paras[2]

    # Calculating the position and velocity of target and missile
    rT=target_state[0:3]
    vT=(rT-prev_target_state[0:3])/dt
    rM=np.array([state.x,state.y,state.z])
    vM=np.array([state.vx,state.vy,state.vz])

    # Position and velocity of target wrt to missile
    rTM=rT-rM
    vTM=vT-vM

    # Representing lamda xy, xz and yz in this order 
    LOS=np.array([np.arctan2(rTM[1],rTM[0]),np.arctan2(rTM[2],rTM[0]),np.arctan2(rTM[2],rTM[1])])

    # Getting lambda dot xy, xz and yz in this order
    LOS_dot=np.array([
        ((rTM[0]*vTM[1]-rTM[1]*vTM[0])/max((rTM[0]**2+rTM[1]**2),cons.den_min)),
        ((rTM[0]*vTM[2]-rTM[2]*vTM[0])/max((rTM[0]**2+rTM[2]**2),cons.den_min)),
        ((rTM[1]*vTM[2]-rTM[2]*vTM[1])/max((rTM[1]**2+rTM[2]**2),cons.den_min))
    ])

    # Getting the closing velocity in xy, xz and yz planes
    vC=np.array([
        -((rTM[0]*vTM[0]+rTM[1]*vTM[1])/max(np.sqrt(rTM[0]**2+rTM[1]**2),cons.den_min)),
        -((rTM[0]*vTM[0]+rTM[2]*vTM[2])/max(np.sqrt(rTM[0]**2+rTM[2]**2),cons.den_min)),
        -((rTM[1]*vTM[1]+rTM[2]*vTM[2])/max(np.sqrt(rTM[1]**2+rTM[2]**2),cons.den_min))
    ])

    # Getting the command accelerations for xy, xz and yz planes
    nC=np.array([
        N*vC[0]*LOS_dot[0],
        N*vC[1]*LOS_dot[1],
        N*vC[2]*LOS_dot[2]
    ])

    dvxdt=-nC[0]*np.sin(LOS[0])-nC[1]*np.sin(LOS[1])
    dvydt=nC[0]*np.cos(LOS[0])-nC[2]*np.sin(LOS[2])
    dvzdt=nC[1]*np.cos(LOS[1])+nC[2]*np.cos(LOS[2])

    return State([0.0,0.0,0.0,dvxdt,dvydt,dvzdt,0.0,0.0,0.0,0.0,0.0,0.0])
