from include.state import State
import numpy as np

# Transformation function to transform euler angles from body centered to ground frame of refrence
def transform(state):
    # Current angles
    phi=state.phi
    theta=state.theta
    
    # Roll rate in body centered frame of refrence
    body_roll_rate=np.array([
        [state.p],
        [state.q],
        [state.r]
    ])

    # Transformation matrix
    transformation_matrix=np.array([
        [1.0,np.sin(phi)*np.tan(theta),np.cos(phi)*np.tan(theta)],
        [0.0,np.cos(phi),-np.sin(phi)],
        [0.0,np.sin(phi)/np.cos(theta),np.cos(phi)/np.cos(theta)]
    ])

    # Roll rate in ground centered frame of refrence
    return transformation_matrix@body_roll_rate

# Default kinematics function applicable in absence of any external disturbances
def kinematics(t,state):
    # Getting translational derivatives
    dxdt=state.vx
    dydt=state.vy
    dzdt=state.vz

    # Getting rotational derivatives
    roll_rate=transform(state).flatten()
    phi_dot=roll_rate[0]
    theta_dot=roll_rate[1]
    psi_dot=roll_rate[2]

    return State([dxdt,dydt,dzdt,0.0,0.0,0.0,phi_dot,theta_dot,psi_dot,0.0,0.0,0.0])