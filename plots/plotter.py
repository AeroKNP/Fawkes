import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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

# Plotting the intercept trajectory in 3D
def plot_3D_intercept(ax,x,y,z,xtarget,ytarget,ztarget):
    
    ax.plot(x,y,z,color='blue',label='Interceptor')
    ax.plot(xtarget,ytarget,ztarget,color='red',label='Target')
    ax.set_xlabel("X Co ordinate")
    ax.set_ylabel("Y Co ordinate")
    ax.set_zlabel("Z Co ordinate")

    ax.grid()
    ax.legend()

# Animating the intercept trajectory in 3D
def animate_3D_intercept(x,y,z,
                         xtarget,ytarget,ztarget,
                         t):

    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111,projection='3d')

    line_int, = ax.plot([],[],[],color='blue',label='Interceptor')
    line_tgt, = ax.plot([],[],[],color='red',label='Target')

    time_text = ax.text2D(
        0.05,
        0.95,
        "",
        transform=ax.transAxes
    )

    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.set_zlabel("Z Coordinate")

    ax.legend()

    ax.set_xlim(min(min(x),min(xtarget)),
                max(max(x),max(xtarget)))

    ax.set_ylim(min(min(y),min(ytarget)),
                max(max(y),max(ytarget)))

    ax.set_zlim(min(min(z),min(ztarget)),
                max(max(z),max(ztarget)))

    ax.set_box_aspect([1,1,1])

    def update(frame):

        line_int.set_data(x[:frame],y[:frame])
        line_int.set_3d_properties(z[:frame])

        line_tgt.set_data(
            xtarget[:frame],
            ytarget[:frame]
        )
        line_tgt.set_3d_properties(
            ztarget[:frame]
        )

        time_text.set_text(
            f"T = {t[frame]:.2f} s"
        )

        return (
            line_int,
            line_tgt,
            time_text
        )

    ani = FuncAnimation(
        fig,
        update,
        frames=range(0,len(t),30),
        interval=1,
        blit=False
    )

    ani.save(
        "intercept_animation.mp4",
        writer="ffmpeg",
        fps=60,
        dpi=150
    )

    plt.show()