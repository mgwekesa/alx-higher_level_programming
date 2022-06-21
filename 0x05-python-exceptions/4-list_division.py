#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    index = 0
    res_list = []
    err_res = ""
    while index < list_length:
        try:
            div_res = my_list_1[index] / my_list_2[index]
        except ValueError:
            div_res = 0
        except (TypeError):
            div_res = 0
            print("wrong type")
        except ZeroDivisionError:
            div_res = 0
            print("division by 0")
        except IndexError:
            div_res = 0
            print("out of range")
        finally:
            res_list.insert(index, div_res)
        index += 1
    return res_list
