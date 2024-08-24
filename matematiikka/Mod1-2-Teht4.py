# Aseta matriisi A ja laske -6A

import numpy as np

A = [36, 28, 36, 32, 20, 33]

t = np.array(A)
print(t)
result = (-6*t)
print(result)

# Tulosta vastaus matriisi muodossa
formatted_result = f"matrix([{', '.join(map(str, result))}])"
print(formatted_result)
