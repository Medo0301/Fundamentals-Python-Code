population = list(map(int, input().split(", ")))
min_wealth = int(input())

if sum(population) / len(population) < min_wealth:
    print("No equal distribution possible")
else:
    while min(population) < min_wealth:
        min_population = min(population)
        max_population = max(population)

        idx_min_population = population.index(min_population)
        idx_max_population = population.index(max_population)

        needed_population = min_wealth - min_population

        population[idx_min_population] += needed_population
        population[idx_max_population] -= needed_population

    print(population)
