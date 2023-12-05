#!/bin/bash
#SBATCH --mail-type=ALL # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --nodes=1 # Run on a single node
#SBATCH --ntasks=1     # Number of CPU (processer cores i.e. tasks) In this example I use 1. I only need one, since none of the commands I run are parallelized.
#SBATCH --mem=1gb # Memory limit
#SBATCH --time=01:00:00 # Time limit hrs:min:sec


module load bedtools/2.28.0


sort -k 1,1 -k2,2n ${outdir}${rootname}.unsorted.bed >${outdir}${rootname}.sorted.bed

bedtools closest -a ${outdir}${rootname}.sorted.bed -b $genebed -d >${outdir}${rootname}.closestgene.sorted.bed
bedtools intersect -a ${outdir}${rootname}.sorted.bed -b $bidirs -wa -wb > ${outdir}${rootname}.inbidir.sorted.bed
~                                                                                                                                                          
~         
