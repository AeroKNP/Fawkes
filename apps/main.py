import csv
import numpy as np
from include.state import State
from include.integrators import rk4_step
from include.target import run_target
from src.dynamics import derivatives
from include import logger


# Initialising the state variable
state=State([0.0,0.0,0.0,0.0,0.0,6.0,0.0,0.0,0.0,0.0,0.0,0.0])
t=0.0
t_final=1000.0
dt=0.001

# Initialising the variables for target object 
target_state=np.array([100.0,0.0,70.0,0.0,20.0,0.0])
prev_target_state=target_state.copy()

# Initialising the csv file to store data 
filename=input("Enter the filename to store the simulation data(without extension): ")
file=open(f"data/{filename}.csv","w",newline="")
writer=csv.writer(file)
logger.init_file(writer)

# Propagation loop
while t<t_final:
    
    # Updating the target object
    prev_target_state=target_state.copy()
    target_state=run_target(t,prev_target_state,dt).copy()

    # Updating fawkes and appending the data
    state=rk4_step(state,t,dt,derivatives,[target_state,prev_target_state,dt])
    t+=dt
    logger.log_state(writer,t,state,target_state)

    # If strikes ground or target then stop the simulation
    if state.z<0.0:
        print("Crashed")
        break
    elif np.sqrt((state.x-target_state[0])**2+(state.y-target_state[1])**2+(state.z-target_state[2])**2)<0.1:
        print("Target Intercepted")
        break

# Closing the file
file.close()
print("Simulation Ended")