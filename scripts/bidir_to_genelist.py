import sys
import pandas as pd

def main(outputdirectory, rootname, bidirstogenes,tissue):
    inputfile=outputdirectory+rootname+".inbidir.sorted.bed"
    snpinbidirdf = pd.read_csv(inputfile, sep="\t", index_col=False, names=["snp_chr", "snp_start", "snp_stop", "bidir_chr", "bidir_start", "bidir_stop", "calledby", "n"])
    print (snpinbidirdf.head)
    snpinbidirdf["bidirname"] = snpinbidirdf["bidir_chr"]+":"+ snpinbidirdf["bidir_start"].astype("str")+"-"+ snpinbidirdf["bidir_stop"].astype("str")
    snpinbidirdffilename = outputdirectory+rootname+".snpinbidir.df"
    snpinbidirdf.to_csv(snpinbidirdffilename)
    pairsdf = pd.read_csv(bidirstogenes, compression='gzip', sep="\t")
    pairsdf[["gene", "transcript_id"]] = pairsdf['transcript_1'].str.split(':', n=1, expand=True)
    hasasnp = pairsdf[pairsdf["transcript_2"].isin(snpinbidirdf["bidirname"].unique())]
    hasasnp_thistissue = hasasnp[hasasnp["tissue"]==tissue]
    pairsdf_thistissue = pairsdf[pairsdf["tissue"]==tissue]
    backgroundoutputfile = outputdirectory+rootname+".background.txt"
    genelistoutputfile = outputdirectory+rootname+".genelist.txt"
    hasasnp_thistissue["gene"].drop_duplicates().to_csv(genelistoutputfile, index=False, header=False)
    pairsdf_thistissue["gene"].drop_duplicates().to_csv(backgroundoutputfile, index=False, header=False)
    pairsdf_thistissue.to_csv(backgroundoutputfile+".df")
    hasasnp_thistissue.to_csv(genelistoutputfile+".df")
    closestgenetosnpfile=outputdirectory+rootname+".closestgene.sorted.bed"
    closestgenetosnpdf = pd.read_csv(closestgenetosnpfile, sep="\t", names=["snp_chr", "snp_start", "snp_stop", "gene_chr", "gene_start", "gene_stop", "gene_name","score", "strand","distance"], index_col=False)
    closestgenetosnpdf[["gene", "transcript_id"]] = closestgenetosnpdf['gene_name'].str.split(':', n=1, expand=True)
    closestgenetosnptargetfile=outputdirectory+"/"+rootname+".closest.genelist.txt"
    closestgenetosnpdf["gene"].drop_duplicates().to_csv(closestgenetosnptargetfile, index=False, header=False)

if __name__=="__main__":
        outputdirectory = sys.argv[1]
        rootname=sys.argv[2]
        bidirstogenes=sys.argv[3]
        tissue = sys.argv[4]
        main(outputdirectory, rootname, bidirstogenes,tissue)	
