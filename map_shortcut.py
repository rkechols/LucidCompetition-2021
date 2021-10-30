import math
import sys


TOTAL_DEGS = 360
HALF_DEGS = TOTAL_DEGS // 2
LEFT = "Left"
RIGHT = "Right"

START_POSITION = [0, 0, 0]


def to_rads(theta: float) -> float:
    return (theta * 2 * math.pi) / TOTAL_DEGS


def to_degs(theta: float) -> float:
    return (theta * TOTAL_DEGS) / (2 * math.pi)


def sin(theta: float) -> float:
    theta_rad = to_rads(theta)
    return math.sin(theta_rad)


def cos(theta: float) -> float:
    theta_rad = to_rads(theta)
    return math.cos(theta_rad)


def inverse_tan(x_delta: float, y_delta: float) -> float:
    if round(x_delta) == 0:
        if y_delta > 0:
            return 90
        else:
            return -90
    theta_rad = math.atan(y_delta / x_delta)
    theta = to_degs(theta_rad)
    if x_delta < 0:
        theta = theta + HALF_DEGS
        if theta > HALF_DEGS:
            theta -= TOTAL_DEGS
    return theta


if __name__ == "__main__":
    N = int(input())
    cur_position = START_POSITION[:]  # copy
    for _ in range(N):
        direction, degrees_str, paces_str = input().split()
        degrees = int(degrees_str)
        paces = int(paces_str)
        if direction == LEFT:
            cur_position[2] = (cur_position[2] + degrees) % TOTAL_DEGS
        else:  # direction == RIGHT
            cur_position[2] = (cur_position[2] - degrees) % TOTAL_DEGS
        cur_position[0] += paces * cos(cur_position[2])
        cur_position[1] += paces * sin(cur_position[2])
        print(cur_position, file=sys.stderr)
    x_diff = cur_position[0] - START_POSITION[0]
    y_diff = cur_position[1] - START_POSITION[1]
    net_distance = math.sqrt((x_diff ** 2) + (y_diff ** 2))
    net_direction = inverse_tan(x_diff, y_diff)
    if net_direction < 0:
        net_direction_pos = -1 * net_direction
        print(f"{RIGHT} {round(net_direction_pos)} {round(net_distance)}")
    else:
        print(f"{LEFT} {round(net_direction)} {round(net_distance)}")
