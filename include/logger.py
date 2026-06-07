# Creating the file and initialsing the columns
def init_file(writer):

    writer.writerow(["Time","X","Y","Z","Vx","Vy","Vz",
                     "Phi","Theta","Psi","P","Q","R"])

# Logging the state in the file
def log_state(writer,t,state):
    
    writer.writerow([t,state.x,state.y,state.z,state.vx,state.vy,state.vz,
                    state.phi,state.theta,state.psi,state.p,state.q,state.r])
