import numpy as np
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams

# ----------------------------
# 1. Generate Data
# ----------------------------

def generate_circle(n_points=200, noise=0.05):
    angles = np.linspace(0, 2*np.pi, n_points)
    x = np.cos(angles) + noise * np.random.randn(n_points)
    y = np.sin(angles) + noise * np.random.randn(n_points)
    return np.vstack((x, y)).T

# Generate dataset
data = generate_circle()

# ----------------------------
# 2. Plot Data
# ----------------------------

plt.scatter(data[:, 0], data[:, 1])
plt.title("Point Cloud (Noisy Circle)")
plt.show()

# ----------------------------
# 3. Compute Persistent Homology
# ----------------------------

result = ripser(data)
diagrams = result['dgms']

# ----------------------------
# 4. Plot Persistence Diagram
# ----------------------------

plot_diagrams(diagrams, show=True)

# ----------------------------
# 5. Optional: Barcode Plot
# ----------------------------

def plot_barcode(diagrams):
    plt.figure(figsize=(10, 5))

    for i, dgm in enumerate(diagrams):
        for j, interval in enumerate(dgm):
            birth, death = interval
            plt.plot([birth, death], [j, j], label=f"H{i}" if j == 0 else "")

    plt.title("Barcode Diagram")
    plt.xlabel("Filtration Value")
    plt.ylabel("Features")
    plt.legend()
    plt.show()

plot_barcode(diagrams)

# ----------------------------
# 6. Interpret Results
# ----------------------------

print("H0 (connected components):")
print(diagrams[0])

print("\nH1 (loops):")
print(diagrams[1])
