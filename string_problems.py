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

