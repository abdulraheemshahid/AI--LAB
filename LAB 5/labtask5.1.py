def minimax(cur_depth, node_index, max_turn, scores, target_depth):
    if cur_depth == target_depth:
        return scores[node_index]
    if max_turn:
        left_value = minimax(
            cur_depth + 1, node_index * 2, False, scores, target_depth
        )
        right_value = minimax(
            cur_depth + 1, node_index * 2 + 1, False, scores, target_depth
        )
        return max(left_value, right_value)
    else:
        left_value = minimax(
            cur_depth + 1, node_index * 2, True, scores, target_depth
        )
        right_value = minimax(
            cur_depth + 1, node_index * 2 + 1, True, scores, target_depth
        )
        return min(left_value, right_value)
scores = [3, 5, 2, 9, 0, 7]
target_depth = 3
scores += [0] * (2 ** target_depth - len(scores))
print("Leaf scores:", scores)
print("Minimax tree depth:", target_depth)
best_value = minimax(0, 0, True, scores, target_depth)
print("The optimal Minimax value is:", best_value)