import math

def feed(obstacles, player_pos):
    print get_space_vector(obstacles)
    print player_pos

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

