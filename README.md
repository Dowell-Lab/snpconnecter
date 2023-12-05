# snpconnecter
Method for linking GWAS SNPs to genes based on DBNascent bidirectional region and gene pairs.


1) Go to https://www.ebi.ac.uk/gwas/ 
	1a) search your favorite disesase/disorder (in this case leukemia)

![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)
	1b) Download the SNPs for that disorder

2) Clone this project and edit the script GWAStogenes_alltissues.sh to point to all the paths on your computer with the files you need. The current paths are for the BioFrontiers super computer fiji. This project assumes you are using slurm on fiji. If you are not useing slurm on fiji you will also need to edit runGWAStobed.sh, diseasetobidir.sh, runbidirtogene.sh to fit your super computer. 

3) run the script by typeing 
	bash GWAS_alltissues.sh

4) the output will be in the output directory
	inputfilename_tissue

5) There are additional notebooks in the jupyter_notebooks directory that can look at the output. 


![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)


