from include import constants as cons
from include.state import State

# Simulating the gravity derivatives
def gravity(t,state):

    # Approximating g to remain constant in the operating range 
    dvzdt=-cons.g_surface

    return State([0.0,0.0,0.0,0.0,0.0,dvzdt,0.0,0.0,0.0,0.0,0.0,0.0])