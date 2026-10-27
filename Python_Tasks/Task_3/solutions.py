# Task 3: Python Coding & Problem-Solving
# Q1. Find the Frequency of Each Word in a Sentence
def word_freq(sentence):
    freq = {}
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1
    return freq


# Q2. Find the Frequency of Each Character in a Word
def char_freq(word):
    freq = {}
    for char in word:
        freq[char] = freq.get(char, 0) + 1
    return freq


# Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating(word):
    freq = char_freq(word)
    for char in word:
        if freq[char] == 1:
            return char
    return None


# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    return char_freq(s1) == char_freq(s2)


# Q5. Find the First Repeating Character in a String
def first_repeating(word):
    seen = set()
    for char in word:
        if char in seen:
            return char
        seen.add(char)
    return None


# Q6. Move All Zeros to the End of a List
def move_zeros(nums):
    non_zeros = [num for num in nums if num != 0]
    zeros = [num for num in nums if num == 0]
    return non_zeros + zeros


# Q7. Find the Second Highest Distinct Number in a List
def second_highest(nums):
    unique_nums = sorted(set(nums), reverse=True)
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]


# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates(nums):
    result = []
    seen = set()
    for num in nums:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result


# Q9. Find the Missing Number from 1 to N
def missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


# Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum_first(nums, target):
    seen = []
    for num in nums:
        need = target - num
        for earlier in seen:
            if earlier == need:
                return [earlier, num]
        seen.append(num)
    return []


# Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    return min(nums, key=lambda num: (abs(num), -num))


# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    second_set = set(list2)
    result = []
    seen = set()
    for num in list1:
        if num in second_set and num not in seen:
            result.append(num)
            seen.add(num)
    return result


# Q13. Rotate a List to the Right by K Positions
def rotate_right(nums, k):
    if not nums:
        return []
    k = k % len(nums)
    return nums[-k:] + nums[:-k] if k else nums[:]


# Q14. Find the Maximum Sum of Two Consecutive Elements
def max_consecutive_sum(nums):
    return max(nums[i] + nums[i + 1] for i in range(len(nums) - 1))


# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def all_target_pairs(nums, target):
    pairs = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.add(tuple(sorted((nums[i], nums[j]))))
    return [list(pair) for pair in sorted(pairs)]
