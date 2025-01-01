def calculate_trapping_water(building_heights):
    if not building_heights:
        return 0

    n = len(building_heights)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = building_heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], building_heights[i])

    right_max[n - 1] = building_heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], building_heights[i])

    water_trapped = 0
    for i in range(n):
        water_trapped += min(left_max[i], right_max[i]) - building_heights[i]

    return water_trapped


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

result = calculate_trapping_water(height)
print(f"Total water trapped: {result} units")