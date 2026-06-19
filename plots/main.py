import matplotlib.pyplot as plt
import pandas as pd
import plotter

# Reading the data from the CSV File
filename=input("Enter the finalname which you want to plot (without extension): ")
df=pd.read_csv(f"results/{filename}.csv")

# Creating the arrays
t=df["t"].to_numpy()
x=df["x"].to_numpy()
y=df["y"].to_numpy()
z=df["z"].to_numpy()
vx=df["vx"].to_numpy()
vy=df["vy"].to_numpy()
vz=df["vz"].to_numpy()
phi=df["phi"].to_numpy()
theta=df["theta"].to_numpy()
psi=df["psi"].to_numpy()
p=df["p"].to_numpy()
q=df["q"].to_numpy()
r=df["r"].to_numpy()
xtarget=df["xtarget"].to_numpy()
ytarget=df["ytarget"].to_numpy()
ztarget=df["ztarget"].to_numpy()

# Plotting the graphs
fig=plt.figure(figsize=(12,14))
ax=fig.add_subplot(111,projection="3d")
plotter.plot_3D_intercept(ax,x,y,z,xtarget,ytarget,ztarget)
plt.savefig("plots/plot.png",dpi=300)
