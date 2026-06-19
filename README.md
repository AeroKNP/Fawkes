# Fawkes

A C++ simulation of an autonomous quadrotor interceptor — built from first principles, modeling full 12-state rigid body dynamics, cascaded attitude control, and multi-phase guidance to autonomously pursue and intercept a moving target.

No external physics or control libraries are used. Rigid body dynamics, the rotation/transformation math, the cascade controller, the motor mixer, and the guidance laws are all implemented from scratch.

This simulator is being built as groundwork for an eventual real-world interceptor drone — the goal is to validate guidance and control logic in simulation before any of it touches real hardware.

---

## Overview

Fawkes simulates a quadrotor with four motors, tracking a moving target through three sequential guidance phases:

1. **Rise** — vertical liftoff from the ground
2. **Pure Pursuit** — closes in once airborne, steering directly toward the target's current position
3. **Proportional Navigation** — engages once sufficiently aligned and moving fast enough, driving the intercept using line-of-sight rate

Proportional navigation here is not a standard 3D guidance law — it uses a custom approach that decomposes the 3D intercept geometry into three planes (xy, xz, yz) and solves the line-of-sight rate and commanded acceleration independently in each, before recombining them into a 3D command.

The simulation runs until the interceptor either reaches the target (within a defined strike range) or crashes into the ground.

---

## Features

- **12-state rigid body dynamics** — position, velocity, Euler angles, and body angular rates
- **Cascaded PID attitude control** — outer-loop rate commands feeding an inner-loop PID for torque
- **Motor mixing** — converts commanded thrust and torque into individual motor RPMs, with force/RPM clamping to respect motor limits
- **Multi-phase guidance** — rise, pure pursuit, and proportional navigation, switched automatically based on closing geometry and speed
- **Moving target dynamics** — target follows its own independent equations of motion
- **RK4 numerical integration**
- **Custom math layer** — hand-built `Vector3` and `Matrix` classes (no Eigen or external dependencies)
- **CSV telemetry logging** for post-run analysis
- **Python-based plotting** for 3D trajectory visualization (interceptor vs. target)

---

## Project Structure

```
Fawkes/
├── apps/             # Entry point (main.cpp)
├── include/          # Headers
├── src/              # Implementation files
├── plots/            # Python plotting scripts
├── results/          # Generated CSV telemetry (gitignored)
├── refrences/         # Supporting derivations and reference material
└── CMakeLists.txt
```

---

## Configuration

All mission parameters are currently set directly in `apps/main.cpp` — initial state, target starting position, motor specs, and controller gains. There's no external config file yet, so changing a scenario means editing and rebuilding.

**Target dynamics** are not fixed to one scenario — the target's motion model can be changed, and its starting position can be placed anywhere, to test the interceptor against different intercept geometries.

**Parameter randomization:** since real-world drag coefficient and frontal area are never known exactly, the simulation randomizes these (and similar physical parameters) by some percentage on every run, rather than using fixed textbook values. The intent is to use this as a controller-robustness testbed — tune the cascade and guidance gains until the interceptor reliably achieves intercept across many randomized runs, not just one idealized case.

---

## Dependencies

**C++ simulation:**
- A C++17-capable compiler (e.g. `g++`)
- CMake (>= 3.10)

**Plotting (optional, for visualization):**
```bash
pip install pandas matplotlib
```

---

## Building

Fawkes uses CMake. From the project root:

```bash
mkdir build
cd build
cmake ..
make
```

The `fawkes` executable is generated inside `build/`.

> Re-run `cmake ..` whenever a `.cpp` file is added or removed, so it gets picked up in the build.

To rebuild from a clean state:

```bash
rm -rf build
mkdir build
cd build
cmake ..
make
```

---

## Running

Run the executable from the **project root** (not from inside `build/`), so telemetry output lands in the correct location:

```bash
./build/fawkes
```

You'll be prompted for a filename to store the run's telemetry data, written to `results/<filename>.csv`.

---

## Visualizing Results

After a run, generate a 3D trajectory plot, run from the **project root** (not from inside `plots/`):

```bash
python plots/main.py
```

This plots the interceptor's trajectory against the target's, saved as an image in `plots/`.

---

## Status

The C++ port is fully functional end-to-end — it compiles, runs, and successfully simulates interception of a moving target through all three guidance phases.

---

## License

This project is licensed under the MIT License.