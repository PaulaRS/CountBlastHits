# PresenceAbsenceFromBlast
 
This repository contains the python script **get_presence_absence_from_blast.py** to calculate presence/absence of
gene/protein hits based in a blast output tabular file. 

# Before running the script

Install the following python packages: argparse, os, sys

# Running the script

For help:
python get_presence_absence_from_blast.py -h

With arguments:
python get_presence_absence_from_blast.py --seq-hits seq_hits.txt --file-suffix '_blasted.txt'

# Utilization

The output of this script was used with [Evolview](https://www.evolgenius.info/evolview/#/treeview)
to produce the sequence similarity profile presented [here](https://ars.els-cdn.com/content/image/1-s2.0-S1047847721000848-gr6.jpg).

# Citation
[Ramos-Silva P, Wall-Palmer D, Marlétaz F, Marin F, Peijnenburg KTCA. 
Evolution and biomineralization of pteropod shells. J Struct Biol 2021; 213: 107779.](https://doi.org/10.1016/j.jsb.2021.107779)
