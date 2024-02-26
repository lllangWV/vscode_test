import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Generate a sine wave
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Introduce some noise
noise = np.random.normal(0, 0.1, y.shape)
noisy_signal = y + noise

# Attempt to smooth the noisy signal
# Intentional mistake: window length is even; it should be odd
window_length = 24  # This should be an odd number
polynomial_order = 3
try:
    smoothed_signal = savgol_filter(noisy_signal, window_length, polynomial_order)
except ValueError as e:
    print(f"Error encountered: {e}")
    # Placeholder for corrected window_length, for demonstration
    window_length = 25
    smoothed_signal = savgol_filter(noisy_signal, window_length, polynomial_order)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Original Sine Wave')
plt.plot(x, noisy_signal, label='Noisy Signal')
plt.plot(x, smoothed_signal, label='Filtered Signal')
plt.legend()
plt.show()