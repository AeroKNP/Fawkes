import numpy as np

# Converts the required torque and thrust to individual motor rpms
def get_rpm(T,Torque,motors):
    
    # Getting the torques and motor parameters
    Tx,Ty,Tz=Torque
    C=motors[0].km/motors[0].kf

    # Individual forces of each motor
    forces=np.array([
        0.25*T+(Tx)/(2*motors[0].position[1])+(Tz)/(4*C),
        0.25*T-(Ty)/(2*motors[0].position[1])-(Tz)/(4*C),
        0.25*T-(Tx)/(2*motors[0].position[1])+(Tz)/(4*C),
        0.25*T+(Ty)/(2*motors[0].position[1])-(Tz)/(4*C)
    ])

    # Clamping the forces above zero while maintaining balance
    min_force=np.min(forces)
    if min_force<0:
        forces=forces-min_force
    
    # Getting the RPMs and clamping them to maxmium while maintaining balance
    RPMs=np.sqrt(forces/motors[0].kf)

    if np.max(RPMs)>motors[0].max_RPM:
        sf=np.max(RPMs)/motors[0].max_RPM
        RPMs=RPMs/sf
    
    return RPMs