from include.state import State
from include.integrators import rk4_step
from src.dynamics import derivatives
from include import logger
import csv

# Initialising the state variable
state=State([0.0,0.0,0.0,0.0,0.0,100.0,0.0,0.0,0.0,0.0,0.0,0.0])
t=0.0
t_final=100.0
dt=0.1

# Initialising the file making 
filename=input("Enter the filename to store the simulation data(without extension): ")
file=open(f"data/{filename}.csv","w",newline="")
writer=csv.writer(file)
logger.init_file(writer)

# Propagation loop
while t<t_final:
    state=rk4_step(state,t,dt,derivatives)
    t+=dt
    logger.log_state(writer,t,state)

    # If strikes ground then stop the simulation
    if state.z<0.0:
        break

# Closing the file
file.close()
print("Simulation Ended")