class State:
    # Intitialising the state variable
    def __init__(self,initial_state=None):

        if initial_state is None:
            initial_state=[0.0]*12

        (self.x)=initial_state[0]
        (self.y)=initial_state[1]
        (self.z)=initial_state[2]
        (self.vx)=initial_state[3]
        (self.vy)=initial_state[4]
        (self.vz)=initial_state[5]
        (self.phi)=initial_state[6]
        (self.theta)=initial_state[7]
        (self.psi)=initial_state[8]
        (self.p)=initial_state[9]
        (self.q)=initial_state[10]
        (self.r)=initial_state[11]

    # Setting the state to some value
    def set_state(self,state):
        (self.x)=state[0]
        (self.y)=state[1]
        (self.z)=state[2]
        (self.vx)=state[3]
        (self.vy)=state[4]
        (self.vz)=state[5]
        (self.phi)=state[6]
        (self.theta)=state[7]
        (self.psi)=state[8]
        (self.p)=state[9]
        (self.q)=state[10]
        (self.r)=state[11]

    # Getting the state print
    def print_state(self):
        print(f"\nThe co ordinates: ({self.x:.2f},{self.y:.2f},{self.z:.2f})")
        print(f"The velocity vector: ({self.vx:.2f},{self.vy:.2f},{self.vz:.2f})")
        print(f"Orientation: ({self.phi:.2f},{self.theta:.2f},{self.psi:.2f})")
        print(f"Roll Rates: ({self.p:.2f},{self.q:.2f},{self.r:.2f})\n")

    # Adding two states
    def __add__(self,other):
        return State([self.x+other.x,
                      self.y+other.y,
                      self.z+other.z,
                      self.vx+other.vx,
                      self.vy+other.vy,
                      self.vz+other.vz,
                      self.phi+other.phi,
                      self.theta+other.theta,
                      self.psi+other.psi,
                      self.p+other.p,
                      self.q+other.q,
                      self.r+other.r,])
    
    # Subtracting two states
    def __sub__(self,other):
        return State([self.x-other.x,
                      self.y-other.y,
                      self.z-other.z,
                      self.vx-other.vx,
                      self.vy-other.vy,
                      self.vz-other.vz,
                      self.phi-other.phi,
                      self.theta-other.theta,
                      self.psi-other.psi,
                      self.p-other.p,
                      self.q-other.q,
                      self.r-other.r,])
    
    # Multiplying the state with a scalar
    def __mul__(self, other):
        return State([self.x*other,
                      self.y*other,
                      self.z*other,
                      self.vx*other,
                      self.vy*other,
                      self.vz*other,
                      self.phi*other,
                      self.theta*other,
                      self.psi*other,
                      self.p*other,
                      self.q*other,
                      self.r*other,])
    
    def __rmul__(self, other):
        return self.__mul__(other)
    