import math
def minimax(depth, index, max_turn, scores, target_depth, counter):
    if depth == target_depth:
        counter[0] += 1
        return scores[index]
    if max_turn:
        left_value = minimax(
            depth + 1, index * 2, False, scores, target_depth, counter
        )
        right_value = minimax(
            depth + 1, index * 2 + 1, False, scores, target_depth, counter
        )
        return max(left_value, right_value)
    else:
        left_value = minimax(
            depth + 1, index * 2, True, scores, target_depth, counter
        )
        right_value = minimax(
            depth + 1, index * 2 + 1, True, scores, target_depth, counter
        )
        return min(left_value, right_value)
def alphabeta(depth, index, max_turn, scores, target_depth,
              alpha, beta, counter):
    if depth == target_depth:
        counter[0] += 1
        return scores[index]
    if max_turn:
        value = float("-inf")
        for i in range(2):
            child_value = alphabeta(
                depth + 1, index * 2 + i, False, scores, target_depth,
                alpha, beta, counter
            )
            value = max(value, child_value)
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float("inf")
        for i in range(2):
            child_value = alphabeta(
                depth + 1, index * 2 + i, True, scores, target_depth,
                alpha, beta, counter
            )
            value = min(value, child_value)
            beta = min(beta, value)

            if alpha >= beta:
                break
        return value

scores = [3, 5, 2, 9, 0, 7]
target_depth = math.ceil(math.log2(len(scores)))
scores += [0] * (2 ** target_depth - len(scores))
minimax_counter = [0]
minimax_value = minimax(0, 0, True, scores, target_depth, minimax_counter)
alphabeta_counter = [0]
alphabeta_value = alphabeta(
    0, 0, True, scores, target_depth,
    float("-inf"), float("inf"), alphabeta_counter
)
print("Leaf scores:", scores)
print("Tree depth:", target_depth)
print()
print("===== Minimax =====")
print("Root value:", minimax_value)
print("Leaves evaluated:", minimax_counter[0])
print()
print("===== Alpha-Beta Pruning =====")
print("Root value:", alphabeta_value)
print("Leaves evaluated:", alphabeta_counter[0])
print()
print("===== Comparison =====")
print("Same root value:", minimax_value == alphabeta_value)
print("Leaves saved by Alpha-Beta:",
      minimax_counter[0] - alphabeta_counter[0])