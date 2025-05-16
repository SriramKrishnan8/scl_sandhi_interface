#!/usr/bin/env python3

from rules import rules_dict, rules_list
from exceptions import exception_rules

#$DEBUG=1;
pra = "praWamapaxam"
dvi= "xviwIyapaxam"
sam= "saMhiwapaxam"
sa= "sanXiH"
sut= "sUwram/vArwikam"
pra1= "prakriyA"

morph_binary_file = "all_morf.bin"


def get_results(search_key, rules_list, f_rem, sf, res, sandhi_name, sutra):
    """ """

    for rule in rules_list:
        split_rules = rule.split(",")
        cur_key = split_rules[0] + "," + split_rules[1]
        if search_key == cur_key:
            sandhied_sols = split_rules[2]
            possible_sols = sandhied_sols.split("/")
            for sol in possible_sols:
                an = f_rem + sol + sf
                res = res + ":" + an
                an1 = split_rules[3]
                sandhi_name = sandhi_name + ":" + an1
                an2 = split_rules[4]
                sutra = sutra + ":" + an2
    
    return res, sandhi_name, sutra


def sandhi_operation(first, second):
    """ """

    i = []
    res_list = []
    
    res, sandhi_name, sutra, cont = exception_rules(
        first, second, morph_binary_file
    )

    if cont == 0:
        res = ":" + res
        sandhi_name = ":" + sandhi_name + "-sanXiH"
        sutra = ":" + sutra
        result = ",".join((res, sandhi_name, sutra, pra, dvi, sam, sa, sut, pra1))
    else:
        first_rem_1 = first[:-1]
        lf1 = first[-1]
        first_rem_2 = first[:-2]
        lf2 = first[-2:]

        second_rem = second[1:]
        sf = second[0]

        search_str_1 = lf1 + "," + sf
        search_str_2 = lf2 + "," + sf

        if search_str_1 in rules_dict:
            res, sandhi_name, sutra = get_results(
                search_str_1, rules_list,
                first_rem_1, second_rem,
                res, sandhi_name, sutra
            )
        elif search_str_2 in rules_dict:
            res, sandhi_name, sutra = get_results(
                search_str_2, rules_list,
                first_rem_2, second_rem,
                res, sandhi_name, sutra
            )
        else:
            pass

        if not res == "":
            result = ",".join((res, sandhi_name, sutra, pra, dvi, sam, sa, sut, pra1))
        else:
            result = ",".join(((first + second), second, "", pra, dvi, sam, sa, sut, pra1))
    
    return result
