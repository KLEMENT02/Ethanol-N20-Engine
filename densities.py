import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Constants and Data
R = 8.314  # Ideal gas constant (J/mol*K)
Hv = 16.1  # Enthalpy of Vaporization (KJ/mol)
P1 = 31.27  # Pressure in Bar
T1 = 273.15  # Temperature in Kelvin
T2 = np.linspace(273.15, 36.42 + 273.15, 100)  # Temperature range in Kelvin

# Experimental data
T_data = np.array([-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 36.42])  # Temperature (°C)
rho_liq_data = np.array([995.4, 975.2, 953.9, 931.4, 907.4, 881.6, 853.5, 822.2, 786.6, 743.9, 688.0, 589.4, 452])  # Liquid density (kg/m³)
rho_vap_data = np.array([46.82, 54.47, 63.21, 73.26, 84.86, 98.41, 114.5, 133.9, 158.1, 190.0, 236.7, 330.4, 452])  # Vapor density (kg/m³)

# Ethanol Properties
E = 1100e-6  # 1/°C (thermal expansion coefficient)
B = 8.9e9  # N/m² (bulk modulus)
rho0 = 789  # Ethanol density at 20°C (kg/m³)
T0 = 20  # Reference temperature (°C)
P0 = 101325  # Reference pressure in Pa (1 atm)

# Functions
def clausius_clapeyron(Hv, R, T1, P1, T2):
    """Computes vapor pressure using the Clausius-Clapeyron equation."""
    return P1 / np.exp((Hv * 1000 / R) * (1 / T2 - 1 / T1))

def interp_densities(T_data, rho_liq_data, rho_vap_data, T_interp):
    """Interpolates liquid and vapor densities."""
    rho_liq_interp = interp1d(T_data, rho_liq_data, kind='linear', fill_value='extrapolate')(T_interp)
    rho_vap_interp = interp1d(T_data, rho_vap_data, kind='linear', fill_value='extrapolate')(T_interp)
    return rho_liq_interp, rho_vap_interp

def calc_rho_etanol(rho0, E, B, T_grid, P_grid, T0, P0):
    """Calculates ethanol density based on temperature and pressure."""
    return (rho0 / (1 + E * (T_grid - T0))) / (1 - (P_grid - P0) / B)

# Compute Vapor Pressure of N₂O
P2 = clausius_clapeyron(Hv, R, T1, P1, T2)

# Compute Interpolated Densities of N₂O
T_interp = T2 - 273.15  # Convert from Kelvin to Celsius
rho_liq_interp, rho_vap_interp = interp_densities(T_data, rho_liq_data, rho_vap_data, T_interp)

# Temperature and Pressure range for ethanol
T = np.linspace(0, 40, 100) 
P = np.linspace(1e5, 80e5, 100)  # Pascal
T_grid, P_grid = np.meshgrid(T, P)

# Compute Ethanol Density
rho_grid = calc_rho_etanol(rho0, E, B, T_grid, P_grid, T0, P0)

# Plotting Graphs
plt.figure(figsize=(12, 10))

# Vapor Pressure of N₂O
plt.subplot(2, 2, 1)
plt.plot(T_interp, P2, linewidth=1.5)
plt.title("Vapor Pressure of N₂O")
plt.xlabel("Temperature (°C)")
plt.ylabel("Vapor Pressure (bar)")
plt.grid(True)

# Density of N₂O (Liquid and Vapor)
plt.subplot(2, 2, 2)
plt.plot(T_interp, rho_liq_interp, 'b', linewidth=1.5, label='Liquid')
plt.plot(T_interp, rho_vap_interp, 'r', linewidth=1.5, label='Vapor')
plt.title("Density of N₂O (Liquid and Vapor)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Density (kg/m³)")
plt.legend()
plt.grid(True)

# Ethanol Density Surface Plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(T_grid, P_grid / 1e5, rho_grid, cmap='viridis', edgecolor='none')
ax.set_title('Ethanol Density vs Temperature and Pressure')
ax.set_xlabel('Temperature (°C)')
ax.set_ylabel('Pressure (bar)')
ax.set_zlabel('Density (kg/m³)')

# Ethanol Density Contour Plot
plt.figure(figsize=(8, 6))
contour = plt.contourf(T_grid, P_grid / 1e5, rho_grid, 20, cmap='viridis')
plt.title("Ethanol Density - Contours")
plt.xlabel("Temperature (°C)")
plt.ylabel("Pressure (bar)")
plt.colorbar(contour)
plt.grid(True)

# Show all plots
plt.show()
