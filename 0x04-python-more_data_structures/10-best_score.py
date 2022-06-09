#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        max_k = list(a_dictionary)[0]
        for key in a_dictionary:
            max_k = key if a_dictionary[key] > a_dictionary[max_k] else max_k
        return max_k
    return None
