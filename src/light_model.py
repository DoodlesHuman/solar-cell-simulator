import random

def generate_carriers(num_pairs, region_start, region_end):
    carriers = []
    for _ in range(num_pairs):
        x = random.uniform(region_start, region_end)
        carriers.append(Carrier('electron', x, 0.0))
        carriers.append(Carrier('hole', x, 0.0))
    return carriers