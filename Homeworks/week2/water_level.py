def maxArea(pools):
    if not pools or len(pools) < 2:
        return 0

    left = 0
    right = len(pools) - 1
    max_area = 0

    while left < right:
        height = min(pools[left], pools[right])
        width = right - left

        current_area = width * height
        max_area = max(max_area, current_area)

        if pools[left] < pools[right]:
            left += 1
        else:
            right -= 1

    return max_area


test_cases = [
    [1, 8, 6, 2, 5, 4, 8, 3, 7],  # Ожидаемый результат: 49
    [1, 1],                        # Ожидаемый результат: 1
    [4, 3, 2, 1, 4],               # Ожидаемый результат: 16
    [1, 2, 1],                     # Ожидаемый результат: 2
]

for i, case in enumerate(test_cases):
    result = maxArea(case)
    print(f"{i} тест: площадь = {result}")
