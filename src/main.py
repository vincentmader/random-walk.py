#!/usr/bin/env python3
from datetime import datetime as dt

import matplotlib.pyplot as plt
import numpy as np

MPL_THEME = "./mpl-styles/dark.mplstyle"
plt.style.use(MPL_THEME)


def random_displacement():
    direction = np.random.choice(4, 1)
    # Direction: Up.
    if direction == 0:
        return np.array([0, 1])
    # Direction: Down.
    elif direction == 1:
        return np.array([0, -1])
    # Direction: Left.
    elif direction == 2:
        return np.array([-1, 0])
    # Direction: Right.
    elif direction == 3:
        return np.array([1, 0])


def plot_positions(positions):
    for pos_id in range(1, len(positions)):
        alpha = pos_id / len(positions)
        color = [alpha, alpha, alpha]
        p_1x = positions[pos_id][0]
        p_1y = positions[pos_id][1]
        p_2x = positions[pos_id-1][0]
        p_2y = positions[pos_id-1][1]
        plt.plot([p_1x, p_2x], [p_1y, p_2y], color=color)

    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([])


def plot_avg_squared_distances(positions):
    plt.title(r"mean squared distance $\langle|\vec r|^2\rangle$ vs. time $t$")

    plt.plot(average_squared_distances, color="white")

    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)


if __name__ == "__main__":
    initial_position = np.array([0, 0])
    positions = [initial_position]
    average_squared_distances = [0]

    plt.figure(figsize=(12, 6))
    while True:
        start = dt.now()

        new_pos = positions[-1] + random_displacement()
        positions.append(new_pos)

        squared_distances = [pos[0]**2 + pos[1]**2 for pos in positions]
        average_squared_distance = np.average(squared_distances)
        average_squared_distances.append(average_squared_distance)

        plt.subplot(1, 2, 1)
        plot_positions(positions)

        plt.subplot(1, 2, 2)
        plot_avg_squared_distances(positions)

        finish = dt.now()
        duration = int((finish - start).microseconds / 1000)
        plt.xlabel(f"step execution time: {duration} ms", color="cyan")

        plt.pause(0.00000001)
        plt.clf()


plt.show()
