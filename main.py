# # https://leetcode.com/problems/longest-common-prefix/
# def func(lst):
#     s = ""
#     i = 0
#     if lst[0] == "":
#         return ""
#     try:
#         while True:
#             lets = []
#             for elem in lst:
#                 lets.append(elem[i])
#             print(lst)
#             print(lets)
#             if len(set(lets)) == 1:
#                 s += lets[0]
#             else:
#                 return s
#             print(s)
#             i += 1
#     except:
#         return s
#
#
#
# print(func(["ab"]))

## https://leetcode.com/problems/roman-to-integer/
# from horology import Timing
# def romanToInt(s):
#     let = {
#         "I": 1,
#         "V": 5,
#         "X": 10,
#         "L": 50,
#         "C": 100,
#         "D": 500,
#         "M": 1000
#     }
#     s = list(s)
#     for i in range(len(s)):
#         s[i] = let[s[i]]
#     for i in range(len(s) - 1):
#         if s[i] < s[i + 1]:
#             s[i] *= -1
#     return sum(s)
#
#
# romanToInt("MXIV")
#
# for z in range(10):
#     with Timing(name="time: "):
#         romanToInt("III")
#         romanToInt("LVIII")
#         romanToInt("MCMXCIV")
#
# # faster romanToInt
# def romanToInt(s):
#     d = {"C": 100,
#          "D": 500,
#          "M": 1000,
#          'L': 50,
#          'X': 10,
#          'V': 5,
#          'I': 1,
#          }
#     result = 0
#     value = 0
#     for i in range(len(s) - 1, -1, -1):
#         curr_value = d[s[i]]
#         if curr_value < value:
#             result -= curr_value
#         else:
#             result += curr_value
#         value = curr_value
#     return result
#
# romanToInt("MXIV")

# https://leetcode.com/problems/palindrome-number/
# from horology import Timing
#
#
# def isPalindrome(x):
#     x = str(x)
#     return x == x[::-1]


# https://leetcode.com/problems/palindrome-number/
# from horology import Timing
# from time import sleep


# def isPalindrome(x):
#     if x >= 0:
#         rev = 0
#         temp = x
#         while temp != 0:        # temp = 123    temp = 12   temp = 1
#             rev *= 10           # rev  = 0      rev  = 30   rev = 320
#             rev += temp % 10    # rev  = 3      rev  = 32   rev = 321
#             temp = temp // 10   # temp = 12     temp = 1    temp = 0
#         if x == rev:
#             return True
#     return False

# def isPalindrome(x):
#     x = str(x)
#     return x == x[::-1]

## https://leetcode.com/problems/two-sum/
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]


# print(twoSum([2, 7, 11, 15], 9))

## https://leetcode.com/problems/add-two-numbers/description/
# l1 = [2,4,3]
# l2 = [5,6,4]
# l1 = [str(elem) for elem in reversed(l1)]
# num = int(''.join(l1))
# l2 = [str(elem) for elem in reversed(l2)]
# num2 = int(''.join(l2))
# l3 = list(map(int, list(str(num + num2))))
# print(l3)


# # https://leetcode.com/problems/valid-parentheses/
# def isValid(s):
#     sign_open = "({["
#     sign_close = ")}]"
#
#     # if string starts with closed bracket
#     if s[0] in sign_close:
#         return False
#
#     # if opened and closed brackets amount are not same
#     for i in range(len(sign_open)):
#         if s.count(sign_open[i]) != s.count(sign_close[i]):
#             return False
#
#     s_len = len(s)
#     checked = []
#
#     for i in range(s_len):
#         if i in checked:
#             continue
#         else:
#             match_sign = sign_close[sign_open.find(s[i])]
#         for j in range(i + 1, s_len):
#             if s[j] == match_sign and j not in checked:
#                 checked.append(j)
#                 break
#         else:
#             return False
#     return True
# print(isValid("()[]{}"))
# print(isValid("()][{}"))
# print(isValid("()))(("))
# print(isValid("[()()]"))
# # дужки повинні закриватись в тому ж порядку, в якому і відкривались.
# # якщо дужка закрилась то вона ж має відкриватись останньою.
# # ті дужки які вже закрились і відкрились не враховуються при перевірці порядку закривання
# def isValid(s):
#     stack = []
#     for i in s:
#         if i in "({[":
#             stack.append(i)
#         else:
#             if len(stack) == 0:
#                 return False
#             if stack[-1] == "(" and i == ")":
#                 stack.pop()
#             elif stack[-1] == "{" and i == "}":
#                 stack.pop()
#             elif stack[-1] == "[" and i == "]":
#                 stack.pop()
#             else:
#                 return False
#     return True if len(stack) == 0 else False
#
#
# print(isValid("[{()}]"))

# #┐(￣ヘ￣)┌┐(￣ヘ￣)┌┐(￣ヘ￣)┌┐(￣ヘ￣)┌┐(￣ヘ￣)┌┐(￣ヘ￣)┌┐(￣ヘ￣)┌┐(￣ヘ￣)┌┐(￣ヘ￣)┌┐(￣ヘ￣)┌┐(￣ヘ￣)┌┐(￣ヘ￣)┌┐(￣ヘ￣)┌
# #https://leetcode.com/problems/string-compression/
# using i and j loops(a bit worse with memory)
# def compress_1(chars):
#     compressed = []
#     chars_len = len(chars)
#     elem = 0
#     if len(chars) == 1:
#         return chars
#     for i in range(chars_len):
#         if chars[i] == elem:
#             continue
#         for j in range(i, chars_len):
#             if chars[i] != chars[j] or j == chars_len - 1:
#                 if i == 0:
#                     i += 1
#                 num = j - i + 1
#                 elem = chars[i]
#                 compressed.append(elem)
#                 if num != 1:
#                     compressed.extend(str(num))
#                 break
#
#     return compressed
# print(compress_1(["a", "b", "b", "b", "b", "b", "b", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"]))
# # # using built-in count
# def compress_2(chars):
#     comp = []
#     for elem in chars:
#         if elem in comp:
#             continue
#         comp.append(elem)
#         num = chars.count(elem)
#         if num != 1:
#             for e in str(num):
#                 comp.append(e)
#
#     return comp
# print(compress_2(["a", "b", "b", "b", "b", "b", "b", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"]))
# from horology import Timing
# for _ in range(10):
#     with Timing(name="time: "):
#         compress_1(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
# print()
# for _ in range(10):
#     with Timing(name="time: "):
#         compress_2(["a","b","b","b","b","b","b","b","b","b","b","b","b"])

# # #spizhzheno
# def compress(chars):
#
#     n, ptr, cnt = len(chars), 0, 1
#
#     for i in range(1, n + 1):
#
#         if i < n and chars[i] == chars[i - 1]:
#             cnt += 1
#
#         else:
#             chars[ptr] = chars[i - 1]
#             ptr += 1
#
#             if cnt > 1:
#                 s = str(cnt)
#                 m = len(s)
#                 chars[ptr: ptr + m] = s
#                 ptr += m
#
#             cnt = 1
#
#     return ptr
#
# for _ in range(10):
#     with Timing(name="time: "):
#         compress_1(["a","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c"])
# for _ in range(10):
#     with Timing(name="time: "):
#         compress_2(["a","b","b","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c"])

### Merge Two Sorted Lists
### https://leetcode.com/problems/merge-two-sorted-lists/

## checked timing when I added swapped to the 2nd
# to reduce amount of assigning with not swapped check
# def mergeTwoLists_selection_0(array, list2):
#     array.extend(list2)
#     size = len(array)
#     for ind in range(size):
#         min_index = ind
#         for j in range(ind + 1, size):
#             if array[j] < array[min_index]:
#                 min_index = j
#         array[ind], array[min_index] = array[min_index], array[ind]
#         # print(array)
#     return array
#
#
# def mergeTwoLists_selection(array, list2):
#     array.extend(list2)
#     size = len(array)
#     for ind in range(size):
#         swapped = False
#         min_index = ind
#         for j in range(ind + 1, size):
#             if array[j] < array[min_index]:
#                 min_index = j
#                 swapped = True
#         if swapped:
#             array[ind], array[min_index] = array[min_index], array[ind]
#         # print(array)
#     return array


# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# def lengthOfLongestSubstring(s):
#     if len(s) == 1:
#         return 1
#     longest = 0
#     i = 0
#     while i < len(s):
#         temp = ''
#         while i != len(s) and s[i] not in temp:
#             temp += s[i]
#             i += 1
#             # print(f"temp: {temp}")
#         # else:
#             # print(f"this temp: {temp}")
#         i = i - len(temp) + 1
#         if len(temp) > longest:
#
#             longest, temp = len(temp), ''
#             # print(f"longest: {longest}")
#             if longest > len(s[i:]):
#                 return longest
#
#     return longest
#

# def lengthOfLongestSubstring_1(s):
#     seen = {}
#     l = 0
#     output = 0
#     for r in range(len(s)):
#         if s[r] not in seen:
#             output = max(output, r - l + 1)
#         else:
#             if seen[s[r]] < l:
#                 output = max(output, r - l + 1)
#             else:
#                 l = seen[s[r]] + 1
#         seen[s[r]] = r
#
#     return output
#
# lengthOfLongestSubstring_1("aacddwefggasd")


# # 26. Remove Duplicates from Sorted Array
# # https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/946693673/

# def removeDuplicates(nums):
#     i = 0
#     for j in range(1, len(nums)):
#         if nums[i] != nums[j]:
#             i += 1
#             nums[i] = nums[j]
#     return i + 1
#
#
# def removeDuplicates_1(nums):
#     # nums_s = list(set(nums))
#     # l = len(nums_s)
#     # # якщо треба щоб масив був забитий до оригінального розміру
#     # nums_s.extend([0 for elem in range(len(nums) - len(nums_s))])
#     # return l
#
#     # якщо не треба повертати масив
#     return len(set(nums))

# # 151. Reverse words in string
# string = "the sky is blue"
# print(' '.join(string.split(" ")[::-1]))

# # the next
