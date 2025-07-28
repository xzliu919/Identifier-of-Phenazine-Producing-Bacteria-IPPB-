import os,sys
index_file='130W_bacteria.db'
out=open('001tblastn_bacteria.sh','w')
query_file='Phz-AA_191sp.fasta'#sys.argv[1]
out_dir='./b6s'
for line in open(index_file,'r').readlines():
    db=line.strip()
    db_path='/data/xzliu/DATA_base/Bacteria_genome_gbk/bacteria_130w/'+db
    out.write(f'tblastn -query {query_file} -out {out_dir}/{query_file}_vs_{db}.b6  -db {db_path}  -outfmt 6 -evalue 1e-5  -num_threads 2 \n')

    #out.write(f"tblastn -query {query_file} -out {out_dir}/{query_file}_vs_{db}.b6  -db {db_path} -outfmt '6 qseqid sseqid pident qstart qend sstart send length evalue bitscore qcovs qcovhsp sseq' -evalue 1e-5  -num_threads 2  -max_target_seqs 10 \n")
