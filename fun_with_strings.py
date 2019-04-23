#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#author: Debora Beuret

def longest_substrings(s1, s2):
    s1 = s1.lower() #to make the function case-insensitive
    s2 = s2.lower()
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]    #creates a matrix with len(s1)+1 lines and len(s2)+1 columns
    length, i_longest = 0, 0   #length = length of the longest substring in common, i_longest = index where the longest substring ends
    list_longest = []
    for x in range(1, 1 + len(s1)):  #iterates through lines
        for y in range(1, 1 + len(s2)):  #iterates through columns
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > length:
                    length = m[x][y]
                    i_longest = x
                    substring = s1[i_longest - length: i_longest]
                    list_longest = [substring]
                elif m[x][y] == length:
                    length = m[x][y]
                    i_longest = x
                    substring = s1[i_longest - length: i_longest]
                    list_longest.append(substring)
            else:
                m[x][y] = 0
    if len(list_longest) == 0:
        return None
    return list_longest

print(longest_substrings('Tod', 'Leben'))
print(longest_substrings('Haus', 'Maus'))
print(longest_substrings('mozart', 'Mozzarella'))