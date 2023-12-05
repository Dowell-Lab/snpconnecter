#!/bin/bash
#SBATCH --mail-type=ALL # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --nodes=1 # Run on a single node
#SBATCH --ntasks=1     # Number of CPU (processer cores i.e. tasks) In this example I use 1. I only need one, since none of the commands I run are parallelized.
#SBATCH --mem=1gb # Memory limit
#SBATCH --time=01:00:00 # Time limit hrs:min:sec

module load python/3.11.3

echo preGWASdbtobed
echo $infile 
echo $outdir
echo $rootname

python GWASdbtobed.py $infile $outdir $rootname
