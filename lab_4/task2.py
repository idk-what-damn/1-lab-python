import numpy as np

lengths = np.array([20, 8, 9, 18, 5, 12, 16, 16, 6, 7])
speeds = np.array([44, 70, 44, 66, 46, 38, 38, 37, 66, 67])
k, p = 4, 7

start, end = k - 1, p

selected_lengths = lengths[start:end]
selected_speeds = speeds[start:end]

distance = selected_lengths.sum()
time = np.sum(selected_lengths / selected_speeds)
average_speed = distance / time

print(f"S = {distance} км, T = {round(time, 2)} час, V = {round(average_speed, 2)} км/ч")
