# CountBlastHits
 
This repository contains the python script **count_blast_hits.py** to calculate presence/absence of
gene/protein hits based in a blast output tabular file. 

# Python packages

Install the following python packages: argparse, os, sys

# Running the script for the first time

For help:
python count_blast_hits.py -h

With arguments:
python get_presence_absence_from_blast.py --seq-hits seq_hits.txt --file-suffix '_blasted.txt'

# Usage

The output of this script was used with [Evolview](https://www.evolgenius.info/evolview/#/treeview)
to produce a sequence [similarity profile](https://ars.els-cdn.com/content/image/1-s2.0-S1047847721000848-gr6.jpg).

# Citation
[Ramos-Silva P, Wall-Palmer D, Marlétaz F, Marin F, Peijnenburg KTCA. 
Evolution and biomineralization of pteropod shells. J Struct Biol 2021; 213: 107779.](https://doi.org/10.1016/j.jsb.2021.107779)
