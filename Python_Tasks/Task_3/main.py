# Task 3: Test all 15 functions from solutions.py

from solutions import (
    word_freq, char_freq, first_non_repeating, are_anagrams,
    first_repeating, move_zeros, second_highest, remove_duplicates,
    missing_number, two_sum_first, closest_to_zero, common_elements,
    rotate_right, max_consecutive_sum, all_target_pairs
)

# Q1
print("Q1:", word_freq("python is easy and python is powerful"))
print("Q1 extra:", word_freq("cat dog cat cat"))

# Q2
print("Q2:", char_freq("banana"))
print("Q2 extra:", char_freq("hello"))

# Q3
print("Q3:", first_non_repeating("swiss"))
print("Q3 extra:", first_non_repeating("aabb"))

# Q4
print("Q4:", are_anagrams("listen", "silent"))
print("Q4 extra:", are_anagrams("hello", "world"))

# Q5
print("Q5:", first_repeating("programming"))
print("Q5 extra:", first_repeating("abcdef"))

# Q6
print("Q6:", move_zeros([0, 3, 0, 1, 2, 0, 4]))
print("Q6 extra:", move_zeros([1, 0, 2]))

# Q7
print("Q7:", second_highest([10, 20, 40, 30, 40, 20]))
print("Q7 extra:", second_highest([5, 5, 5]))

# Q8
print("Q8:", remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print("Q8 extra:", remove_duplicates([1, 1, 2, 3, 2]))

# Q9
print("Q9:", missing_number([1, 2, 4, 5, 6], 6))
print("Q9 extra:", missing_number([1, 3, 4], 4))

# Q10
print("Q10:", two_sum_first([2, 7, 11, 15], 9))
print("Q10 extra:", two_sum_first([3, 2, 4], 6))

# Q11
print("Q11:", closest_to_zero([-8, -3, 2, 5, -2]))
print("Q11 extra:", closest_to_zero([-4, -1, 3]))

# Q12
print("Q12:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Q12 extra:", common_elements([2, 2, 3, 1], [2, 1]))

# Q13
print("Q13:", rotate_right([1, 2, 3, 4, 5], 2))
print("Q13 extra:", rotate_right([1, 2, 3], 1))

# Q14
print("Q14:", max_consecutive_sum([4, 7, 2, 9, 5]))
print("Q14 extra:", max_consecutive_sum([1, 10, 2]))

# Q15
print("Q15:", all_target_pairs([2, 4, 3, 5, 7, 8, 1], 9))
print("Q15 extra:", all_target_pairs([1, 2, 3, 4], 5))
