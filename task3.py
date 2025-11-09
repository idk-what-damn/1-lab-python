import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib
import numpy as np


def task3():
    fig, ax = plt.subplots(figsize=(8, 8))

    body = patches.Ellipse((0, 0), 3, 4, fill=True, color='lightgray', alpha=0.8)
    ax.add_patch(body)


    head = patches.Circle((0, 3), 1.5, fill=True, color='lightgray', alpha=0.8)
    ax.add_patch(head)

    ear_left = patches.Ellipse((-0.8, 4.5), 0.4, 2.0, fill=True, color='lightgray')
    ear_right = patches.Ellipse((0.8, 4.5), 0.4, 2.0, fill=True, color='lightgray')
    ax.add_patch(ear_left)
    ax.add_patch(ear_right)

    ear_inner_left = patches.Ellipse((-0.8, 4.2), 0.2, 1.5, fill=True, color='pink')
    ear_inner_right = patches.Ellipse((0.8, 4.2), 0.2, 1.5, fill=True, color='pink')
    ax.add_patch(ear_inner_left)
    ax.add_patch(ear_inner_right)

    eye_left = patches.Circle((-0.6, 3.3), 0.2, fill=True, color='black')
    eye_right = patches.Circle((0.6, 3.3), 0.2, fill=True, color='black')
    ax.add_patch(eye_left)
    ax.add_patch(eye_right)


    eye_glint_left = patches.Circle((-0.65, 3.35), 0.05, fill=True, color='white')
    eye_glint_right = patches.Circle((0.55, 3.35), 0.05, fill=True, color='white')
    ax.add_patch(eye_glint_left)
    ax.add_patch(eye_glint_right)


    nose = patches.Circle((0, 2.8), 0.15, fill=True, color='pink')
    ax.add_patch(nose)

    for i in range(3):
        ax.plot([-0.2, -1.5], [2.7 + i * 0.1, 2.5 + i * 0.1], 'k-', linewidth=1.5)
        ax.plot([0.2, 1.5], [2.7 + i * 0.1, 2.5 + i * 0.1], 'k-', linewidth=1.5)

    paw_left = patches.Circle((-1.0, 0.5), 0.3, fill=True, color='lightgray')
    paw_right = patches.Circle((1.0, 0.5), 0.3, fill=True, color='lightgray')
    ax.add_patch(paw_left)
    ax.add_patch(paw_right)

    back_paw_left = patches.Ellipse((-1.2, -1.5), 0.6, 0.8, fill=True, color='lightgray')
    back_paw_right = patches.Ellipse((1.2, -1.5), 0.6, 0.8, fill=True, color='lightgray')
    ax.add_patch(back_paw_left)
    ax.add_patch(back_paw_right)


    tail = patches.Circle((0, -1.8), 0.4, fill=True, color='white', alpha=0.9)
    ax.add_patch(tail)

    cheek_left = patches.Circle((-0.9, 2.9), 0.25, fill=True, color='pink', alpha=0.4)
    cheek_right = patches.Circle((0.9, 2.9), 0.25, fill=True, color='pink', alpha=0.4)
    ax.add_patch(cheek_left)
    ax.add_patch(cheek_right)

    mouth_arc = patches.Arc((0, 2.6), 0.6, 0.3, angle=0, theta1=180, theta2=360,
                            linewidth=2, color='black')
    ax.add_patch(mouth_arc)

    brow_left = patches.FancyBboxPatch((-1.0, 3.7), 0.4, 0.08, boxstyle="round,pad=0.02",
                                       fill=True, color='black')
    brow_right = patches.FancyBboxPatch((0.6, 3.7), 0.4, 0.08, boxstyle="round,pad=0.02",
                                        fill=True, color='black')
    ax.add_patch(brow_left)
    ax.add_patch(brow_right)


    ax.set_xlim(-3, 3)
    ax.set_ylim(-2.5, 6)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Мой любимый зайчик', fontsize=16, pad=20, color='darkviolet')

    for i in range(20):
        x_pos = -2.8 + i * 0.3
        height = 0.2 + np.random.random() * 0.3
        ax.plot([x_pos, x_pos], [-2.5, -2.5 + height], 'g-', linewidth=2)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print(f"Matplotlib version: {matplotlib.__version__}")
    task3()