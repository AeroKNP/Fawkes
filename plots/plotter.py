import matplotlib.pyplot as plt

# Plotting the translational co ordinates against time
def plot_translation(ax,t,x,y,z):

    plt.subplots_adjust(hspace=0.5,wspace=0.5)

    ax[0][0].plot(t,x)
    ax[0][0].set_xlabel("Time")
    ax[0][0].set_ylabel("X Co ordinate")
    ax[0][0].grid()

    ax[0][1].plot(t,y)
    ax[0][1].set_xlabel("Time")
    ax[0][1].set_ylabel("Y Co ordinate")
    ax[0][1].grid()

    ax[1][0].plot(t,z)
    ax[1][0].set_xlabel("Time")
    ax[1][0].set_ylabel("Z Co ordinate")
    ax[1][0].grid()

# Plotting the rotational angles against time
def plot_rotational(ax,t,phi,theta,psi):
    plt.subplots_adjust(hspace=0.5,wspace=0.5)

    ax[0][0].plot(t,phi)
    ax[0][0].set_xlabel("Time")
    ax[0][0].set_ylabel("Phi")
    ax[0][0].grid()

    ax[0][1].plot(t,theta)
    ax[0][1].set_xlabel("Time")
    ax[0][1].set_ylabel("Theta")
    ax[0][1].grid()

    ax[1][0].plot(t,psi)
    ax[1][0].set_xlabel("Time")
    ax[1][0].set_ylabel("Psi")
    ax[1][0].grid()