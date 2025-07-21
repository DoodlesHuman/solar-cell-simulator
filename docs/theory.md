# Solar Cell Simulator - Physics Theory Behind Charge Carrier Simulation in Solar Cells

## 1. Introduction

Solar cells, or photovoltaic cells, convert light energy into electrical energy. The key process underlying this is the generation, motion, and collection of charge carriers (electrons and holes) created by light in a p-n junction.

This simulation models the motion of charge carriers in the presence of an electric field, simulating the drift behavior of electrons and holes in a simplified one-dimensional domain.


## 2. Basic Concepts

### 2.1 Charge Carriers
 - __Electrons (−1 charge):__ Negatively charged particles that drift opposite to the electric field.

- __Holes (+1 charge):__ Positively charged quasi-particles that move in the direction of the electric field.

### 2.2 Electric Field in a Solar Cell
- The built-in electric field in a p-n junction arises from the difference in charge concentration between the p-type and n-type materials.

- This field drives separation of charge carriers, directing electrons toward the n-side and holes toward the p-side.

In the simulation, this is modeled as a constant electric field, 
$$\vec{E} = constant$$

### 2.3 Drift Motion

- Charge carriers experience a force $$\vec{F} = q\vec{E}$$, where
    
    - **q** is the charge of the particle
    - **$$\vec{E}$$** is the Electric field

- Using Newton's second law $$\vec{F} = m\vec{a}$$. Assuming unit mass:

        $$\vec{a} = q\vec{E}$$

- The simulations uses a time-stepping approach:

    - Update velocity: $$v = v + a⋅\Delta t$$
    - Update position: $$x = x + v⋅\Delta t$$

### 2.4 Light-Induced Carrier Generation
- Photons with energy > bandgap excite electrons from the valence band to the conduction band.

- This creates electron-hole pairs, which we simulate using random generation in a defined light-absorbing region.


## 3. Simulation Assumptions

| Assumption       | Justification                                 |
| ---------------- | --------------------------------------------- |
| 1D Motion        | Simplifies simulation and visualization       |
| Constant Field   | Approximates built-in p-n junction field      |
| Unit Mass        | Makes motion calculation straightforward      |
| No Recombination | Focus on carrier motion, not lifetime         |
| No Diffusion     | Purely drift-based simulation                 |

## 4. What This Simulation Teaches
- How electric fields drive current in PV cells

- How electrons and holes respond differently to fields

- Importance of carrier mobility and separation

- How time-step methods approximate continuous motion

