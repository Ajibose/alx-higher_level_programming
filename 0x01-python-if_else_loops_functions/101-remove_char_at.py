#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = ""
    for i in range(str):
        ch = str[i]
        if (i != n):
            str_copy = str_copy + ch

    return (str_copy)
        
