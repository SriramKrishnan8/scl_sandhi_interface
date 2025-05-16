import os, sys

import subprocess as sp
import re

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from scl_sandhi import sandhi_operation

import sandhi

s = sandhi.Sandhi()

svaras = "aAiIuUqQLeEoO"
natva_permissing_letters = svaras + "MkKgGfpPbBmyrvRh"
#natva_permissing_letters = "aAiIuUqQLeEoOMkKgGfpPbBmyrvRh"
natva_inhibiting_letters = "cCjJFtTdDNwWxXnlsS"

second_solution_pairs_wx = [('w', 'h'), ('H', 's'), ('k', 'h'), ('t', 's')]

list_of_preverbs = [
    "A", "aBi", "anu", "api", "ava", "awi", "aXi", "ni", "nis", "pari",
    "pra", "prawi", "sam", "su", "upa", "ux", "vi", "xus", "parA", "ku",
    "niH", "nir", "saw", "asaw", "apa", "Afa", "Af", "UrI", "xur"
]


def natva_inhibited(aft_r):
    index_n = aft_r.find("n")
    if (index_n == (len(aft_r) - 1)):
        return (True, index_n)
    if index_n == -1:
        return (False, index_n)
    bef_n = aft_r[:index_n]
    bef_n_status = [False]
    bef_n_status = [True for (i,v) in enumerate(bef_n) if (v in natva_inhibiting_letters)]
    status = True if (True in bef_n_status) else False
    return (status, index_n)


def natva_status(first, second, letter):
    if (letter in first):
        index_r = first.rfind(letter)
        aft_r = first[(index_r + 1):]
        (status, index) = natva_inhibited(aft_r)
        if status:
            return (first, second)
        if ("n" in second):
            (status, index) = natva_inhibited(second)
            if not status:
                second = second[:index] + "N" + second[(index + 1):]
    return (first, second)

    
def natva(first, second):
    (first, second) = natva_status(first, second, "r")
    (first, second) = natva_status(first, second, "R")
    (first, second) = natva_status(first, second, "q")
    (first, second) = natva_status(first, second, "Q")
    (first, second) = natva_status(first, second, "L")
    return (first, second)


def get_sandhied_form(first, second, natva_needed = True):
    if ((not (first == "")) and (not (second == ""))):
        if ((first == "an") and (second[0] in svaras)):
            result_list = [str(first + second)]
            return result_list
            
        if natva_needed:
            (first, second) = natva(first, second)

        # To access the old perl program for performing the sandhi operation
        # Uncomment the import statement at the top to import the sandhi module
#        p = sp.Popen(['perl', 'sandhi.pl', first, second], stdout=sp.PIPE)
#        result = (p.communicate()[0]).decode('utf-8')
        
        # To access the new python implementation of the sandhi operation
        result = sandhi_operation(first, second)
#        
        result_string = re.search(r':?(.*?),', result).group(1)
        result_list = result_string.split(':')

        # The following is Hrishikesh's sandhi package from pip  
#        result_list = [ item[0] for item in s.sandhi(first, second) ]
        
        return result_list
    else:
        if (first == ""):
            return [second]
        elif (second == ""):
            return [first]
        else:
            return []

            
def sandhi_join(first, second, internal):
    internal = True if ((not internal) and (first in list_of_preverbs)) else internal
    sandhied_word_list = get_sandhied_form(first, second, internal)
        
    if (len(sandhied_word_list) == 0):
        return (first + second)
    else:
        sandhied_word = ""
        if (first == "") or (second == ""):
            sandhied_word = sandhied_word_list[0]
        elif (first[-1],second[0]) in second_solution_pairs_wx:
            sandhied_word = sandhied_word_list[1]
        else:
            sandhied_word = sandhied_word_list[0]
        
        sandhied_word = sandhied_word.replace("><", "H")
        sandhied_word = sandhied_word.replace("  ", " ")
        
        if internal:
            sandhied_word = sandhied_word.replace(" ", "")
        
        return sandhied_word.strip()
    

