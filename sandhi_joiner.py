#!/usr/bin/env python3

import os
import sys
import subprocess as sp

import argparse

import re
import json
from tqdm import tqdm

import devtrans as dt


sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from sandhi_words import sandhi_join
from transliteration import *


sandhi_modes = {
    "int" : "i",
    "ext" : "e"
}


def run_sandhi_join(first_word, second_word, internal):
    """ """
    
    return sandhi_join(first_word, second_word, internal)


def run_sandhi(input_first, input_second, input_encoding,
                output_encoding="roma", sandhi_mode="e"):
    """ """
    
    first_word = input_transliteration(input_first.strip(), input_encoding)[0]
    second_word = input_transliteration(input_second.strip(), input_encoding)[0]
    
    internal = True if sandhi_mode == "i" else False
    
    sandhied_word = run_sandhi_join(first_word, second_word, internal)
    
    sandhi_word_out = output_transliteration(sandhied_word, output_encoding)[0]

    return sandhi_word_out


def run_file_contents(input_file, output_file, input_encoding,
                      output_encoding="roma", sandhi_mode="e"):
    """ """
    
    try:
        ifile = open(input_file, 'r', encoding='utf-8')
    except OSError as e:
        print(f"Unable to open {path}: {e}", file=sys.stderr)
        sys.exit(1)
        
    input_text = ifile.read()
    ifile.close()

    if input_text.strip() == "":
        print("Specified input file does not have any sentence.")
        sys.exit(1)
    
    i_list = [word for word in input_text.split("\n")]
    input_list = list(filter(None, i_list))

    output_list = []
    for i in tqdm(range(len(input_list))):
        input_ = input_list[i]#.strip()
        split_input = input_.split("\t")
        
        input_first = split_input[0]
        input_second = split_input[1]
        
        sandhied_word = run_sandhi(
            input_first, input_second, input_encoding,
            output_encoding, sandhi_mode
        )
        
        output_list.append(sandhied_word)
    
    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.write("\n".join(output_list))
#        json.dump(output_list, out_file, ensure_ascii=False)


def main():
    """ """
    
    # Parsing Arguments
    parser = argparse.ArgumentParser()
    
    # Mandatory Arguments
    parser.add_argument(
        "input_enc", default="WX",
        choices=["DN", "KH", "RN", "SL", "VH", "WX"],
        help="input encoding"
    )
    parser.add_argument(
        "output_enc", default="roma",
        choices=["deva", "roma", "WX"],
        help="output encoding"
    )
    parser.add_argument(
        "sandhi_mode", default="ext",
        choices=["int", "ext"],
        help="int - internal sandhi; or ext - external sandhi"
    )
    
    # Options (one of -f & -s or -i & -o is mandatory)
    parser.add_argument(
        "-f", "--input_first", type=str,
        help="input string"
    )
    parser.add_argument(
        "-s", "--input_second", type=str,
        help="input string"
    )
    parser.add_argument(
        "-i", "--input_file", type=argparse.FileType('r', encoding='UTF-8'),
        help="reads from file if specified"
    )
    parser.add_argument(
        "-o", "--output_file", type=argparse.FileType('w', encoding='UTF-8'),
        help="for writing to file"
    )
    
    args = parser.parse_args()
    
    if args.input_file and (args.input_first or args.input_second):
        print("Please specify either input texts ('-f', '-s') or input file ('-i, -o')")
        sys.exit()
    
    input_enc = args.input_enc
    output_enc = args.output_enc
    sandhi_mode = sandhi_modes.get(args.sandhi_mode, "e")
    
    if args.input_file:
        i_file = args.input_file.name
        o_file = args.output_file.name if args.output_file else "output.txt"
        run_file_contents(
            i_file, o_file, input_enc,
            output_encoding=output_enc, sandhi_mode=sandhi_mode
        )
    elif args.input_first and args.input_second:
        res = run_sandhi(args.input_first, args.input_second, input_enc,
            output_encoding=output_enc, sandhi_mode=sandhi_mode)
        if args.output_file:
            with open(args.output_file.name, 'w', encoding='utf-8') as o_file:
                out_file.write(res)
        else:
            print(res)
    else:
        print("Please specify one of text ('-t') or file ('-i & -o')")
        sys.exit()
    

if __name__ == "__main__":
    main()
