from collections import deque

def valid_anagram(s,t) -> bool:
    #Memory performance is excellent (between 63.60% and 98.67%), runtime performance varies widely (12.94% to 62.97%)
    table = dict()
    for i in range(0, len(s)):
        if s[i] not in table:
            table[s[i]] = 1
        else:
            table[s[i]] += 1

    for i in range(0, len(t)):
        if t[i] not in table:
            return False
        if table[t[i]] > 1:
            table[t[i]] -= 1
        else:
            table.pop(t[i])
    if len(table) > 0:
        return False
    return True

def valid_parentheses(s: str) -> bool:
    parens = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    soln_stack = deque()
    for i in range(0, len(s)):
        if s[i] in parens:
            soln_stack.appendleft(s[i])
        else:
            if len(soln_stack) > 0:
                popped = soln_stack.popleft()
                if s[i] != parens[popped]:
                    return False
            else:
                return False
    if len(soln_stack) == 0:
        return True
    else: return False

def valid_palindrome(s) -> bool:
    import re
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    half_length = len(s) // 2
    is_odd = True if len(s) % 2 == 1 else False
    i = half_length - 1
    j = half_length if is_odd is False else half_length + 1
    while i >= 0:
        if s[i] != s[j]:
            return False
        i -= 1
        j += 1
    return True

def palindromic_substrings(s:str) -> int:
    #Beat 58.11% on runtime, 33.77% on memory usage.

    left = 0
    right = 0
    num_palindromes = len(s)
    for i in range(0, len(s)):
        left = i - 1
        right = i + 1
        def loop(left, right, num_palindromes):
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    num_palindromes += 1
                    left -= 1
                    right += 1
                else:
                    break
            return num_palindromes
        num_palindromes = loop(left, right, num_palindromes)
        left = i
        right = i + 1
        if left >= 0 and right < len(s) and s[left] == s[right]:
            num_palindromes = loop(left, right, num_palindromes)
    return num_palindromes
