import os
dict={}
for line in open('/data/xzliu/DATA_base/Bacteria_genome_gbk/Bacteria_latestassembly_summary.txt','r', encoding='UTF-8').readlines():
    GCF=line.strip().split('\t')[0]
    Assembly_Name=line.strip().split('\t')[2]
    Organism_Name=line.strip().split('\t')[7]
    Strain=line.strip().split('\t')[8]
    dict[GCF]=[Assembly_Name,Organism_Name,Strain]
fold='b6s'
out=open('Phenazin_best_match_info.txt','w')
for file in os.listdir(fold):
    if file.endswith('.b6'):
        gcf='GCA_'+file.split('_vs_')[1].split('_')[1]
        tmp_dict={}
        for line in open(fold+'/'+file,'r').readlines():
            query=line.strip().split('\t')[0].split('-')[0]
            identity=float(line.strip().split('\t')[2])
            if query not in tmp_dict:
                tmp_dict[query]=[identity,line.strip()]
            else:
                if identity>tmp_dict[query][0]:
                    tmp_dict[query] = [identity, line.strip()]
        for k in tmp_dict:
            if gcf in dict:
                out.write(f"{gcf}\t{dict[gcf][0]}\t{dict[gcf][1]}\t{dict[gcf][2]}\t{tmp_dict[k][1]}\n")
