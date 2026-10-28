def minimax(depth, index, max_turn, scores, target_depth, counter):
    if depth == target_depth:
        counter[0] += 1
        return scores[index]
    left = minimax(depth + 1, index * 2, not max_turn,
                   scores, target_depth, counter)
    right = minimax(depth + 1, index * 2 + 1, not max_turn,
                    scores, target_depth, counter)
    return max(left, right) if max_turn else min(left, right)
def alphabeta(depth, index, max_turn, scores, target_depth,
              alpha, beta, counter):
    if depth == target_depth:
        counter[0] += 1
        return scores[index]
    if max_turn:
        value = float("-inf")
        for child in range(2):
            value = max(value, alphabeta(
                depth + 1, index * 2 + child, False, scores, target_depth,
                alpha, beta, counter
            ))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float("inf")
        for child in range(2):
            value = min(value, alphabeta(
                depth + 1, index * 2 + child, True, scores, target_depth,
                alpha, beta, counter
            ))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
def run_test(title, scores):
    depth = 3
    plain_counter = [0]
    plain_value = minimax(0, 0, True, scores, depth, plain_counter)

    prune_counter = [0]
    prune_value = alphabeta(
        0, 0, True, scores, depth,
        float("-inf"), float("inf"), prune_counter
    )
    print(title)
    print("Leaf scores:", scores)
    print("Minimax root value:", plain_value)
    print("Minimax leaves evaluated:", plain_counter[0])
    print("Alpha-Beta root value:", prune_value)
    print("Alpha-Beta leaves evaluated:", prune_counter[0])
    print("Leaves saved:", plain_counter[0] - prune_counter[0])
    print("Root values agree:", plain_value == prune_value)
    print()
scores_original = [3, 5, 2, 9, 3, 5, 2, 9]
scores_reordered = [2, 9, 3, 5, 2, 9, 3, 5]
run_test("===== ORIGINAL BRANCH ORDER =====", scores_original)
run_test("===== REORDERED BRANCH ORDER =====", scores_reordered)