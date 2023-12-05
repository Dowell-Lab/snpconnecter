#edit these
indir=/scratch/Shares/dowell/dbnascent/out/meta_analysis/snpconnecter/inputdata/
outdir=/scratch/Shares/dowell/dbnascent/out/meta_analysis/snpconnecter/outputdata/
diseasesnps=EFO_0000565_associations_export.tsv
useremail=allenma@fiji.colorado.edu
eandodir=/scratch/Users/allenma/eofiles/

#repository files
bidirs=/scratch/Shares/dowell/dbnascent/out/meta_analysis/mumerge/bidirectionals_dreg_tfit/hg38_tfit_dreg_bidirectionals.bed
bidirstogenes=/scratch/Shares/dowell/rutendo/projects/DBNascent_Analysis/data/gene_bidir_significant_pairs/sig_inter_nobs_dist_filtered.txt.gz
#genebed=/scratch/Shares/dowell/dbnascent/out/meta_analysis/snpconnecter/outputdata/geneswithpairs.sorted.bed
genebed=/scratch/Shares/dowell/rutendo/projects/DBNascent_Analysis/data/counts/normalized/genes_analyzed.bed

#build variables
infile=${indir}${diseasesnps}
rootname=`basename $diseasesnps _associations_export.tsv`

for tissue in blood breast embryo heart intestine kidney lung prostate skin uterus umbilical_cord
do 

outdirthisrun=${outdir}${rootname}_${tissue}/

echo $outdirthisrun


mkdir -p $outdirthisrun

jid0=$(sbatch --mail-user=$useremail --job-name=${rootname}_${tissue} --error=${eandodir}${rootname}snptobed.%j.err --out=${eandodir}${rootname}snptobed.%j.out  --export=infile=$infile,outdir=$outdirthisrun,rootname=$rootname runGWAStobed.sh) #will make two files, a bed file for snps and a dataframe for linking snps to the bed file
jid0=$(echo $jid0 | cut -d ' ' -f 4-)
echo $jid0
jid1=$(sbatch --dependency=afterany:$jid0 --mail-user=$useremail --job-name=${rootname}_${tissue} --error=${eandodir}${rootname}snpinbidir.%j.err --out=${eandodir}${rootname}snpinbidir.%j.out  --export=outdir=$outdirthisrun,rootname=$rootname,bidirs=$bidirs,genebed=$genebed diseasetobidir.sh) #will sort the bed file from the above snp and use bedtools to overlap with the master bidirectionals file. will make a sorted bed, a closest gene bed and a inbidirecitonal.bed
jid1=$(echo $jid1 | cut -d ' ' -f 4-)
echo $jid1
jid2=$(sbatch --dependency=afterany:$jid1 --mail-user=$useremail --job-name=${rootname}_${tissue} --error=${eandodir}${rootname}bidirtogene.%j.err --out=${eandodir}${rootname}bidirtogene.%j.out  --export=outdir=$outdirthisrun,rootname=$rootname,bidirstogenes=$bidirstogenes,tissue=$tissue  runbidirtogene.sh)  #will take the inbidirectional.bed and find the genes assosated
jid2=$(echo $jid2 | cut -d ' ' -f 4-)
echo $jid2
done
