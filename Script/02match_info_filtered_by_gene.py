import os
input='Phenazin_best_match_info.txt'

out=open('Phenazin_best_match_info_filtered_by_gene.txt','w')
element_dict={}
element_info_dict={}
for line in open(input,'r').readlines():
    GCF = line.strip().split('\t')[0]
    species = line.strip().split('\t')[2]
    strain = line.strip().split('\t')[3]
    query = line.strip().split('\t')[4]
    contig=line.strip().split('\t')[5]
    indenty = float(line.strip().split('\t')[6])
    hit_start=line.strip().split('\t')[12]
    hit_end=line.strip().split('\t')[13]
    key = (GCF, species,strain,contig)
    value=(indenty,hit_start,hit_end)
    if key not in element_dict:
        element_dict[key]=[query]
        element_info_dict[key]=[value]
    elif key in element_dict and query not in element_dict[key]:
        element_dict[key].append(query)
        element_info_dict[key].append(value)

for k in element_dict:
    if len(element_dict[k])>=5:
        for i in element_dict[k]:
            idex=element_dict[k].index(i)
            #print(idex)
            out.write(f'{k[0]}\t{k[1]}\t{k[2]}\t{k[3]}\t{i}\t{element_info_dict[k][idex][0]}\t{element_info_dict[k][idex][1]}\t{element_info_dict[k][idex][2]}\n')


