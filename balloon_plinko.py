import math
from typing import Tuple


TOTAL_DEGS = 360
HALF_DEGS = TOTAL_DEGS // 2

START_LOCATION = (0, 0, 1500)


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


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


class Balloon:
    def __init__(self, x: int, y: int, z: int, r: int):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

    def in_radius(self, x: float, y: float) -> bool:
        return distance(x, y, self.x, self.y) < self.r

    def slide(self, x: float, y: float) -> Tuple[float, float]:
        x_diff = x - self.x
        y_diff = y - self.y
        theta = inverse_tan(x_diff, y_diff)
        new_x = self.x + (self.r * cos(theta))
        new_y = self.y + (self.r * sin(theta))
        return new_x, new_y

    def __repr__(self) -> str:
        return f"Balloon({self.x}, {self.y}, {self.z}, r={self.r})"


if __name__ == "__main__":
    n = int(input())
    balloons = list()
    for _ in range(n):
        balloon = Balloon(*map(int, input().split()))
        balloons.append(balloon)
    balloons.sort(key=lambda b: b.z, reverse=True)
    cur_x, cur_y, _ = START_LOCATION
    for balloon in balloons:
        if balloon.z > START_LOCATION[2]:
            continue
        if balloon.in_radius(cur_x, cur_y):  # collision
            cur_x, cur_y = balloon.slide(cur_x, cur_y)
    cur_x = int(cur_x)
    cur_y = int(cur_y)
    print(f"{cur_x} {cur_y}")
