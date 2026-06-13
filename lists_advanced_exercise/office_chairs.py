rooms = int(input())
free_chairs = 0
problem = False

for room in range(rooms):
    chairs_and_visitors = input().split()
    visitors = int(chairs_and_visitors[1])
    chairs = len(chairs_and_visitors[0])

    if chairs < visitors:
        print(f"{visitors - chairs} more chairs needed in room {room + 1}")
        problem = True
    else:
        free_chairs += (chairs - visitors)

if not problem:
    print(f"Game On, {free_chairs} free chairs left")
    