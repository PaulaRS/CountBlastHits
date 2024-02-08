__author__ = 'Paula Ramos-Silva'

# Reads txt and/or csv files from blast output and creates file with presence/absence of hits specified by the user
# per sample.
#
# ======================================================================
#
# Tested with:
#  Python 3.9.0
#  using dataset from Ramos-Silva P, Wall-Palmer D, Marlétaz F, Marin F, Peijnenburg KTCA.
#  Evolution and biomineralization of pteropod shells. J Struct Biol 2021; 213: 107779.
#  https://doi.org/10.1016/j.jsb.2021.107779
#
# Created 22-03-2016
# Updated 08-02-2024

import argparse
import os
import sys

def main():

    parser = argparse.ArgumentParser(description="Reads txt and csv files from blast output tabular format and prints "
                                                 "list of presence/absence of sequence hits specified by the user")
    parser.add_argument('--seq-hits', dest='seq_hits', help='text file with accession numbers and sequence names '
                                                            'separated by commas')
    parser.add_argument('--file-suffix', dest='file_suffix', help='suffix used to name blast output csv files ex: '
                                                                  '_blasted.txt')
    args = parser.parse_args()

    # list of output files from blast
    csv_files = filter(lambda x: x.endswith(args.file_suffix), os.listdir('.'))

    # output file
    myfile = open ('profile.txt', "a")

    for csv in csv_files:
        # creates dictionary and prints subject_ids listed in seq_hits and corresponding query_ids that have a
        # match in the blast report
        blastmatch_dic = create_dictionary_fromcommasepfile(csv)
        print (csv)
        for k, v in blastmatch_dic.items() :
            print ("{}\t{}".format(k, v))
        lnoh = []

        # counts number of subject_ids (items) in dictionary values (lists) per sequence hit
        # and writes results to file profile.txt
        with open (args.seq_hits, 'r') as seqhs:
            for l in seqhs:
                myl = l.strip()
                acc = myl.split(',')[0]
                if acc in blastmatch_dic.keys():
                    nrofhits = len(blastmatch_dic[acc])
                else:
                    nrofhits = 0

                lnoh.append(nrofhits)

        myfile.write("{}\t{}\n".format(csv, lnoh))

    myfile.close()


# This function creates a dictionary where keys are subject id(s) and values are the list of query_id(s) having
# subject_id as hit in the blast report

def create_dictionary_fromcommasepfile (myfile):

    with open (myfile, 'r') as intable:
        next(intable)
        dic = {}
        for line in intable:
            li = line.rstrip()
            cols = li.split(',')
            query_id = cols[0].split('-')[0] # may change depending on how query ID is named
            subject_id = cols[3]
            dic.setdefault(subject_id,[]).append(query_id)

    return dic


#########################

if __name__=="__main__":
    usage = "python get_presence_absence_from_blast.py -h"
    if len(sys.argv) != 2:
        print("Incorrect arguments.\nFor usage try: ", usage)
        sys.exit()
    main()
