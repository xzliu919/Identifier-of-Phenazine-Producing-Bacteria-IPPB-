import os
input='Phenazin_best_match_info_filtered_by_gene.txt'
dict={}
target_genes=[]
out=open('Phenazin_components_match_table.txt','w')
for line in open(input,'r').readlines():
    GCF = line.strip().split('\t')[0]
    #print(GCF)
    species=line.strip().split('\t')[1]
    starin=line.strip().split('\t')[2]
    contig=line.strip().split('\t')[3]
    query=line.strip().split('\t')[4].split('-')[0]  #PhzA,PhzB
    if query not in target_genes:
        target_genes.append(query)
    indenty=float(line.strip().split('\t')[5])
    start=float(line.strip().split('\t')[6])
    end=float(line.strip().split('\t')[7])
    #value=(query,contig,line.strip())
    key=(GCF,species,starin,contig)
    V={}
    V[query]=[indenty,start,end]   #query:[indenty,start,end]
    if key not in dict:
        dict[key]=V    #(GCF,species,starin,contig):{PhzA:[indenty,start,end]}
    else:
        dict[key][query]=[indenty,start,end]##(GCF,species,starin,contig):{PhzA:[indenty,start,end]},(GCF,species,starin,contig):{PhzB:[indenty,start,end]}

out.write("GCF\tspecies\tstarin\tcontig\t")
for i in sorted(target_genes):
    out.write(f"{i}\t")
out.write('\n')


for k in dict:
    lis=dict[k]  ##[{PhzA:[indenty,start,end]},{PhzB:[indenty,start,end]}]
    print(lis)
    region_lis=[]
    for i in sorted(target_genes):
        if i in lis.keys():
            region_1=lis[i][1]
            region_2=lis[i][2]
            region_lis.append(region_1)
            region_lis.append(region_2)
    diff=sorted(region_lis)[-1]-sorted(region_lis)[0]
    if 'PhzA' not in lis and 'PhzB' not in lis:
        continue
    else:
        if diff<20000 and 'PhzD' in lis and 'PhzE' in lis and 'PhzF' in lis and 'PhzG' in lis:
            out.write(f"{k[0]}\t{k[1]}\t{k[2]}\t{k[3]}")
            for i in sorted(target_genes):
                if i in lis.keys():
                    out.write(f"\t{lis[i][0]}")
                else:
                    out.write(f"\tNA")
            out.write('\n')

