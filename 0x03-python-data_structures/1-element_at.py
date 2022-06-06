#!/usr/bin/python3

def element_at(my_list, idx):
    ln = len(my_list)
    if (idx >= 0 or idx < ln):
        return (my_list[idx])
    else:
        return None
