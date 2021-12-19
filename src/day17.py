def get_trajectories(x1: int, x2: int, y1: int, y2: int):
    trajectories = []

    for x in range(2 * x2):
        for y in range(2 * y2, -2 * y2):
            y_max = 0
            x_pos = 0
            y_pos = 0

            x_vel = x
            y_vel = y

            while True:
                x_pos += x_vel
                if x_vel > 0:
                    x_vel -= 1
                elif x_vel < 0:
                    x_vel += 1

                y_pos += y_vel
                y_vel -= 1

                y_max = max(y_max, y_pos)

                if x_pos >= x1 and x_pos <= x2 and y_pos <= y1 and y_pos >= y2:
                    trajectories.append((y_max, (x, y)))
                    break

                if x_pos > x2 or y_pos < y2:
                    break

    return trajectories


def star1(x1: int, x2: int, y1: int, y2: int) -> int:
    trajectories = get_trajectories(x1, x2, y1, y2)
    max_y, (x, y) = max(trajectories)
    return max_y


def star2(x1: int, x2: int, y1: int, y2: int) -> int:
    trajectories = get_trajectories(x1, x2, y1, y2)
    return len(trajectories)


if __name__ == "__main__":
    res1 = star1(79, 137, -117, -176)
    print(f"Star 1: {res1}")

    res2 = star2(79, 137, -117, -176)
    print(f"Star 2: {res2}")
