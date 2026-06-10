# Contains constants either of enviornment or parameters of rockets which will be used during the simulation
import numpy as np

g_surface=9.7803
rho_surface=1.225
Cd=0.8
Area=0.05
mass=2
Ixx=0.022
Iyy=0.022
Izz=0.040

# Converts any array from body frame to global frame
def body_to_global_matrix(phi,theta,psi):
    return  np.array([
        [np.cos(theta)*np.cos(psi),np.sin(phi)*np.sin(theta)*np.cos(psi)-np.cos(phi)*np.sin(psi),np.cos(phi)*np.sin(theta)*np.cos(psi)+np.sin(phi)*np.sin(psi)],
        [np.cos(theta)*np.sin(psi),np.sin(phi)*np.sin(theta)*np.sin(psi)+np.cos(phi)*np.cos(psi),np.cos(phi)*np.sin(theta)*np.sin(psi)-np.sin(phi)*np.cos(psi)],
        [-np.sin(theta),np.sin(phi)*np.cos(theta),np.cos(phi)*np.cos(theta)]
    ])

# Converts any array from global frame to body frame
def global_to_body_matrix(phi,theta,psi):
    return body_to_global_matrix(phi,theta,psi).T
