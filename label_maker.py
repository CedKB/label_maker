import argparse
import os.path
import sys
from datetime import date
import warnings

import pandas as pd
from Bio import SeqIO, BiopythonWarning

warnings.simplefilter('ignore', BiopythonWarning)


parser = argparse.ArgumentParser(description="Label Maker", formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("-src", required=True, type=str, help="Mode (genbank or txt)")
parser.add_argument("-out", required=True, type=str, help="Path to output file")
parser.add_argument("-c", required=True, type=str, help="Initials of the creator")

args = parser.parse_args()


if not os.path.isfile(args.src):
    raise ValueError("ERROR, source file could not be found")

file_extension = args.src.split(".")[-1]

if file_extension == "txt":
    with open(args.src, "r") as file:
        file_buffer = file.read()
        labels_raw = file_buffer.splitlines()

elif file_extension in ["gb", "gbk"]:
    record = SeqIO.parse(args.src, "genbank")
    labels_raw = []
    for rec in record:
        labels_raw.append(rec.name)

else:
    raise ValueError("ERROR, please make sure to use the right file extensions (txt, gb, gbk)")


cols = ["Name", "Code", "Lid first line", "Lid second line", "Strain", "Date", "Creator", "AB"]
labels_df = pd.DataFrame(columns=cols)

for lr in labels_raw:
    
    buffer = lr.split("_")
    if buffer[2] == "0" :
        ab_buffer = "Cam"
    if buffer[2] == "1" :
        ab_buffer = "Amp"
    if buffer[2] == "2":
        ab_buffer = "Kan"
        
    entry = {
        "Name" : "_".join(buffer[:5]) + "_\n" + "_".join(buffer[5:]),
        "Code" : "_".join(buffer[:5]),
        "Lid first line" : "_".join(buffer[:3]),
        "Lid second line" : "_".join(buffer[3:5]),
        "Strain" : "E. coli Top 10",
        "Date" : date.today().strftime("%d.%m.%Y"),
        "Creator" : args.c,
        "AB" : ab_buffer
    }
    
    labels_df = labels_df.append(entry, ignore_index=True)   


labels_df.to_excel(args.out, index=False)