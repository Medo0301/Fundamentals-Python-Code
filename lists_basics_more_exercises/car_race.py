ZERO_TIME_REDUCER = 0.8

times_of_race = [int(x) for x in input().split()]
left_racer_time = 0
right_racer_time = 0
finish = len(times_of_race) // 2
left_racer_times = times_of_race[:finish]
right_racer_times = times_of_race[-1:finish:-1]

for idx in range(len(left_racer_times)):
    if left_racer_times[idx] == 0:
        left_racer_time *= ZERO_TIME_REDUCER
    else:
        left_racer_time += left_racer_times[idx]

    if right_racer_times[idx] == 0:
        right_racer_time *= ZERO_TIME_REDUCER
    else:
        right_racer_time += right_racer_times[idx]

if left_racer_time <= right_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_time:.1f}")