
def array_rank(arr):
    sorted_arr = sorted(arr) #sorting
    
    rank_dict = {}  # Dictionary
    rank = 1
    for num in sorted_arr:
        if num not in rank_dict:
            rank_dict[num] = rank
            rank += 1
    
    # Replacing each element in the array with its corresponding rank
    ranked_arr = [rank_dict[num] for num in arr]
    
    return ranked_arr

# Example usage
arr = [10, 8, 15, 12, 6, 20, 1]
ranked_array = array_rank(arr)
print(ranked_array)