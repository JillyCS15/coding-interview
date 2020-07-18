import random

def estimate_pi(num):
    num_point_circle = 0
    num_point_total = 0

    for _ in range(num):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if is_in_circle(x, y):
            num_point_circle += 1
        num_point_total += 1

    return 4 * (num_point_circle / num_point_total)

def is_in_circle(x, y):
    return True if x**2 + y**2 <= 1 else False
