import math
# Devuelve el vector que indica que posiciones
# estan vacias y cuales tienen un obstaculo.
def get_space_vector(obstacles):
    n_rays = 6
    delta_angle = math.pi * 2.0 / n_rays
    start_angle = delta_angle/2.0 

    max_dist = 410 # Si la barra esta mas lejos que esto
                   # no se considera en el space_vector.

    min_dist = 120 # Si la barra esta mas cerca, ya paso
                   # al jugador.
    
    result = []

    for i in range(n_rays):
        current_angle = start_angle + delta_angle*i
        r = 0
        for obs in obstacles:
            dist = obs.vert_mag
            if obs.is_on_angle(current_angle) and min_dist < dist < max_dist:
                r = 1
                break

        result.append(r)

    return result


def get_closer_obstacles(obstacles, delta, player_pos):
    if obstacles == None or len(obstacles) == 0:
        return []

    closer = None

    for obs in obstacles:
        if obs.vert_mag > player_pos - 3:
            if closer == None:
                closer = obs
            elif obs.vert_mag < closer.vert_mag:
                closer = obs


    if closer == None:
        return []

    close_obs = []
    closer_mag = closer.vert_mag
    for obs in obstacles:
        if closer.vert_mag - 10 <= obs.vert_mag <= closer.vert_mag + delta:
            close_obs.append(obs)

    return close_obs

def find_direction(obstacles, player_angle):
    should_move = False

    for obs in obstacles:
        if obs.is_on_angle(player_angle):
            should_move = True
            break

    if not should_move:
        return [False, False]

    steps = 13
    for i in range(steps):
        delta_angle = math.pi * 2.0 / steps
        left_angle = (player_angle - delta_angle*i)%(math.pi*2)
        right_angle = (player_angle + delta_angle*i)%(math.pi*2)

        left_empty = True
        right_empty = True
        for obs in obstacles:
            if obs.is_on_angle(left_angle):
                left_empty = False
            if obs.is_on_angle(right_angle):
                right_empty = False

        if left_empty:
            return [True, False]
        if right_empty:
            return [False, True]

    return [True, False]




