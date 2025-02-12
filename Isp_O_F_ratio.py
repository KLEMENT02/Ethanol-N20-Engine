import matplotlib.pyplot as plt

# Data for O/F ratio and Isp
OF_ratio = [3, 3.5, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6, 6.5, 7]
Isp = [215.12, 221.20, 225.18, 225.77, 226.29, 226.73, 227.12, 227.44, 227.69, 227.89, 228.01, 228.07, 228.07, 228.00, 
       227.87, 227.68, 227.44, 227.14, 226.81, 226.45, 225.22, 222.99, 220.73]

# Create the plot
plt.figure(figsize=(8,6))
plt.plot(OF_ratio, Isp, 'bo', linewidth=1.5, markersize=5)

# Add title and labels
plt.title('Specific Impulse (Isp) vs O/F for Chamber Pressure of 20 bar')
plt.xlabel('O/F Ratio')
plt.ylabel('Specific Impulse, Isp (s)')

# Add grid
plt.grid(True)

# Show the plot
plt.show()
