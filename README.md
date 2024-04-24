# Sandhi-joiner (Powered by Samsaadhanii Sandhi tool)

An interface for [Samsaadhanii's]((www.sanskrit.uohyd.ac.in/scl)) Sandhi tool is built here. The following are the constituents:

1. sandhi.pl, any_sandhi.pl, apavAxa\_any.pl &rarr; sandhi joining perl files from Samsaadhanii
2. all_morf.bin &rarr; morph binary file from Samsaadhanii
3. sandhi\_joiner.py &rarr; accepts two strings or input file and output file and returns the sandhied forms accordingly
4. sandhi\_words.py &rarr; interface for Samsaadhanii's sandhi tool
5. run\_sandhi.sh &rarr; examples to run
6. input.tsv &rarr; input file - tab-delimited words to be sandhied

## Pre-requisites

1. perl
2. python
3. devtrans (using pip)
4. lttoolbox
5. tqdm (using pip)

## Instructions

To run sandhi_joiner.py (for a single instance):

```
python3 sandhi_joiner.py WX deva ext -f "lakRmIvAn" -s "SuBalakRaNaH"
```

To run sandhi_joiner.py (for a multiple instances from an input file):

```
python3 sandhi_joiner.py DN deva ext -i input.tsv -o output.tsv
```

### Input / Output format

Options for Input:
* input\_encoding &rarr; WX, DN, RN, SL, KH, VH
* output\_encoding &rarr; deva, roma
* sandhi_mode &rarr; int, ext
* -f first\_word -s second\_word
* -i input\_file -o output\_file

Output format: sandhied string


