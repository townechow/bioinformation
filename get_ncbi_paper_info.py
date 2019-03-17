'''
读取 NCBI 中文献的信息
python ====>3.7
biopython ===>  1.73
'''

import os
from Bio import SeqIO
from Bio import Entrez
Entrez.email = "zhou@eoutlook.com"     # Always tell NCBI who you are
filename = "D:/pyprojects/gi_186972394.gbk"
if not os.path.isfile(filename):
    print("Downloading...")
    net_handle = Entrez.efetch(db="nucleotide",id="186972394",rettype="gb", retmode="text")
    out_handle = open(filename, "w")
    out_handle.write(net_handle.read())
    out_handle.close()
    net_handle.close()
    print("Saved")

print("Parsing...")
record = SeqIO.read(filename, "genbank")
# print(record)

record_id = record.id
record_name = record.name
record_des = record.description
record_lt_an = record.letter_annotations
record_seq = record.seq

record_info = "record_name: %s\n\
record_id: %s\n\
record_description: %s\n\
record_letter_annotations: %s\n\
record_seq: %s"\
% (record_name, record_id, record_des, record_lt_an,  'record_seq')
print(record_info)

''' more info in record.annotations by keys: 
dict_keys(['molecule_type', 'topology', 'data_file_division', 'date', 'accessions', 'sequence_version', 
'keywords', 'source', 'organism', 'taxonomy', 'references'])
'''

# record_an = record.annotations
record_source = record.annotations["source"]
record_kw = record.annotations["keywords"]
record_organism = record.annotations["organism"]
record_date = record.annotations["date"]
record_seq_v = record.annotations["sequence_version"]

record_info_more = "record_source: %s\n\
record_kw: %s\n\
record_organism: %s\n\
record_date: %s\n\
record_seq_v:%s" \
% (record_source,record_kw, record_organism, record_date,record_seq_v)

print(record_info_more)

