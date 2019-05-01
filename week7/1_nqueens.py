def is_solution(board, n):
    for pos, r in enumerate(board):
        # If there is a duplicate row, this is not a solution.
        if board.count(r) > 1:
            return False

        # For every other number.
        for otherpos, other in enumerate(board):
            if r == other:
                continue

            dist = otherpos - pos

            if other - r == dist:
                return False

    return True


print(is_solution([0, 1, 4, 2, 3], 5)) # false
print(is_solution([0, 2, 4, 1, 3], 5)) # true
print(is_solution([2, 0, 3, 1], 4)) # true
print(is_solution([0, 0, 0, 0], 4)) # false
