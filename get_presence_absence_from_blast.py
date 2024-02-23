__author__ = 'Paula Ramos-Silva'
__dateCreated__ = "22-03-2016"
__dateModified__ = "23-02-2024"

"""
Reads txt and/or csv files in the input/ folder resulting from blast tabular output and prints a list with number of 
hits per subject id. 

usage: python get_presence_absence_from_blast.py -h

Reference:
Paula Ramos-Silva, Deborah Wall-Palmer, Ferdinand Marlétaz, Frédéric Marin, Katja T.C.A. Peijnenburg,
Evolution and biomineralization of pteropod shells, Journal of Structural Biology, Volume 213, Issue 4,
2021, 107779, https://doi.org/10.1016/j.jsb.2021.107779.

Tested with:
Python 3.9.0

"""

import argparse
import os
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Reads txt and csv files from blast output tabular format and prints "
                                                 "list of presence/absence of sequence hits specified by the user")
    parser.add_argument('--seq-hits', dest='seq_hits', help='text file with accession numbers and sequence names '
                                                            'separated by commas')
    parser.add_argument('--file-suffix', dest='file_suffix', help='suffix used to name blast output csv files ex: '
                                                                  '_blasted.txt')
    args = parser.parse_args()

    # list of output files from blast
    csv_files = filter(lambda x: x.endswith(args.file_suffix), os.listdir('input'))
    print(csv_files)

    # output file
    output_folder = Path("output/")
    output_file = output_folder/ "profile.txt"
    profile = open(output_file, "a")

    for csv in csv_files:
        # creates dictionary and prints subject_ids listed in seq_hits and corresponding query_ids that have a
        # match in the blast report
        blast_match_dic = create_dictionary_from_csv(csv)
        print(csv)
        for k, v in blast_match_dic.items():
            print("{}\t{}".format(k, v))
        lnoh = []

        # counts number of subject_ids (items) in dictionary values (lists) per sequence hit
        # and writes results to file profile.txt
        with open(args.seq_hits, 'r') as seqhs:
            for hit in seqhs:
                myhit = hit.strip()
                acc = myhit.split(',')[0]
                if acc in blast_match_dic.keys():
                    nrofhits = len(blast_match_dic[acc])
                else:
                    nrofhits = 0

                lnoh.append(nrofhits)

        profile.write("{}\t{}\n".format(csv, lnoh))

    profile.close()


"""
This function creates a dictionary where keys are subject id(s) and values are the list of query_id(s) having
# subject_id as hit in the blast report
"""


def create_dictionary_from_csv(myfile):
    input_folder = Path("input/")
    file_to_parse = input_folder / myfile
    with open(file_to_parse, 'r') as intable:
        next(intable)
        dic = {}
        for line in intable:
            li = line.rstrip()
            cols = li.split(',')
            query_id = cols[0].split('-')[0]  # may change depending on how query ID is named
            subject_id = cols[3]
            dic.setdefault(subject_id, []).append(query_id)

    return dic


#########################

if __name__ == "__main__":
    usage = "python get_presence_absence_from_blast.py -h"
    if len(sys.argv) < 5:
        print("Incorrect arguments.\nFor usage try: ", usage)
        sys.exit()
    main()
