import math

def print_grid():
    input_Xint = input("PLz enter a X positions: ")
    input_Yint = input("PLz enter a Y positions: ")
    input_Time = input("PLz enter a Time values: ")

    X_list = []
    Y_list = []
    T_list = []

    for digit1 in input_Xint.split():
        X_list.append(float(digit1))

    for digit2 in input_Yint.split():
        Y_list.append(float(digit2))

    for digit3 in input_Time.split():
        T_list.append(float(digit3))

    total_list = []

    for t, a, b in zip(T_list, X_list, Y_list):
        total_list.append((t, a, b))

    print(total_list)
    return total_list


def determence_vector(n):
    vector = []
    initial_point = n[0]
    for i in n:
        dx = i[1] - initial_point[1]
        dy = i[2] - initial_point[2]
        vector.append((i[0], dx, dy))
    return vector


def angel_vector(n):
    angel = []
    for i in range(len(n)):
        if i == 0:
            angel.append((n[i][0], 0.0, 0.0))
        else:
            delta_t = n[i][0] - n[i-1][0]
            vx = (n[i][1] - n[i-1][1]) / delta_t
            vy = (n[i][2] - n[i-1][2]) / delta_t
            magnitude = math.sqrt(vx**2 + vy**2)
            angle_deg = math.degrees(math.atan2(vy, vx))
            angel.append((n[i][0], magnitude, angle_deg))
    return angel


after_vector = print_grid()

print(f'displacements = {determence_vector(after_vector)}')
print(f'angels = {angel_vector(determence_vector(after_vector))}')