import numpy as np
import matplotlib.pyplot as plt

B = [60,50,58,71,61,55,75,68,65,63,60,52,69,58,56,54,
     61,71,51,57,55,49,67,72,54,53,61,65,66,52,
     62,70,72,71,71,62,63,68,60,53]

data = np.sort(B)
y = np.arange(1, len(data) + 1) / len(data)

plt.figure(figsize=(6,4))
plt.step(data, y, where="post")
plt.title("Рис.4 Кумулята (B)")
plt.xlabel("x")
plt.ylabel("F*(x)")
plt.grid(True)
plt.show()
