import numpy as np

class Cascade:
    
    # Initialsing the cascade controller
    def __init__(self,gains=None,max_I=None):
        
        if gains is None:
            gains=np.zeros((4,3))
        if max_I is None:
            max_I=np.array([0.0,0.0,0.0])
        
        self.kp_outer=gains[0]                          # Sets the outer kp gains for all axes
        self.kp_inner=gains[1]                          # Sets the inner kp gains for all axes  
        self.kd_inner=gains[2]                          # Sets the inner kd gains for all axes
        self.ki_inner=gains[3]                          # Sets the inner ki gains for all axes
        self.error_integral=np.array([0.0,0.0,0.0,])    # Sets the integral value for all axes
        self.max_I=max_I                                # Clamps the integral value for all axes
        self.prev_error=np.array([0.0,0.0,0.0])         # Sets the previous errors for all axes

    def set_controller(self,gains,max_I):

        self.kp_outer=gains[0]
        self.kp_inner=gains[1]        
        self.kd_inner=gains[2]        
        self.ki_inner=gains[3] 
        self.error_integral=np.array([0.0,0.0,0.0,])
        self.max_I=max_I
        self.prev_error=np.array([0.0,0.0,0.0])
    
    # Running the outer loop to give roll rates with proportional controller
    def run_outer_loop(self,error_vec):
        return self.kp_outer*error_vec
    
    # Running the entire cascade controller
    def run_cascade(self,error_vec,state,dt):

        # Getting commanded roll rates from outer loop
        cmd_vector=self.run_outer_loop(error_vec)
        
        # Comparing with actual roll rates to get error 
        error=cmd_vector-np.array([state.p,state.q,state.r])

        dedt=(error-self.prev_error)/dt         # Using previous error to get derivative of eror

        self.error_integral+=error*dt           # Integral term from error 
        self.error_integral=np.clip(self.error_integral,-self.max_I,self.max_I)     # Clamping the integrator value

        torque=(self.kp_inner*error)+(self.kd_inner*dedt)+(self.ki_inner*self.error_integral)       

        # Setting the current error to previous error
        self.prev_error=error

        return torque

