def handle_negative_index(pokemon_distances: list) -> int:
    result = pokemon_distances.pop(0)
    pokemon_distances.insert(0, pokemon_distances[-1])
    return result


def handle_overflow_index(pokemon_distances: list) -> int:
    result = pokemon_distances.pop(-1)
    pokemon_distances.append(pokemon_distances[0])
    return result


distances = list(map(int, input().split()))
total_sum_of_distances = 0

while len(distances) > 0:
    idx = int(input())
    current_distance = 0
    if idx < 0:
        current_distance = handle_negative_index(distances)
    elif idx >= len(distances):
        current_distance = handle_overflow_index(distances)
    else:
        current_distance = distances.pop(idx)
    # Using list comprehension with inline if-else for a maximum "Pythonic" transformation,
    # fully in the spirit of the Lists Advanced topic.
    distances = [distance + current_distance if distance <= current_distance
                 else distance - current_distance for distance in distances]

    total_sum_of_distances += current_distance

print(total_sum_of_distances)
