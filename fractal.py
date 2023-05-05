import numpy as np
import matplotlib.pyplot as plt
np.warnings.filterwarnings("ignore")
def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j
def is_stable(c, num_iterations):
    z = c
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2
def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]


c = complex_matrix(-2, 1, -1.5, 1.5, pixel_density=1000)
plt.imshow(is_stable(c, num_iterations=100), cmap="binary")
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()