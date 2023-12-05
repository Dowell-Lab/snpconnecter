
module load python/3.11.3

python makegenefile.py
sort -k 1,1 -k2,2n /scratch/Shares/dowell/dbnascent/out/meta_analysis/snpconnecter/outputdata/geneswithpairs.bed >/scratch/Shares/dowell/dbnascent/out/meta_analysis/snpconnecter/outputdata/geneswithpairs.sorted.bed
