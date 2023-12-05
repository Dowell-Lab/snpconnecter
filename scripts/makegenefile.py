import pandas as pd

fn1="/scratch/Shares/dowell/rutendo/projects/DBNascent_Analysis/data/gene_bidir_significant_pairs/sig_inter_nobs_dist_filtered.txt.gz"
outfile="/Users/allenma/snpconnecter/outputdata/geneswithpairs.bed"

df = pd.read_csv(fn1, compression='gzip', sep="\t")
allgenesinpairs = df[["transcript1_chrom", "transcript1_start", "transcript1_stop", "transcript_1"]].drop_duplicates()
allgenesinpairs.to_csv(outfile, sep="\t", index=False, header=False)
