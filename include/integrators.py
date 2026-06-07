import numpy as np

# Writing the integrator for Euler
def euler_step(state,t,dt,derivatives,extra_parameters=None):
    
    state = state + derivatives(t,state,extra_parameters)*dt

    return state

# Writing the integrator for RK4
def rk4_step(state,t,dt,derivatives,extra_parameters=None):

    k1=derivatives(t,state,extra_parameters)
    k2=derivatives(t+(dt/2),state+(dt/2)*k1,extra_parameters)
    k3=derivatives(t+(dt/2),state+(dt/2)*k2,extra_parameters)
    k4=derivatives(t+(dt),state+(dt)*k3,extra_parameters)

    state = state + (dt/6)*(k1+2*k2+2*k3+k4)

    return state