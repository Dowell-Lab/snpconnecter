import pandas as pd
import sys
import numpy as np


def main(inputfile, outputdirectory, rootfilename):
    df = pd.read_csv(inputfile, sep="\t")
    print ("lines in input file", df.shape)
    df = df[["riskAllele", "locations"]]
    df['riskAllele'] = df['riskAllele'].str.split(',')
    df['locations'] = df['locations'].str.split(',')
    df['riskAllelelen'] = df['riskAllele'].apply(len)
    df['locationslen'] = df['locations'].apply(len)
    df=df[df["riskAllelelen"]==df["locationslen"]]
    df = df[["riskAllele", "locations"]]
    print ("lines after remove entrys that don't have the same number of rsIDs as locations in the genome", df.shape)
    df = df.explode(['riskAllele', 'locations'])
    print ("lines after spliting every rsid and location to its own line", df.shape)
    df[['snp_chr', 'snp_start']] = df['locations'].str.split(':', n=1, expand=True)
    df["snp_chr"] = "chr"+df["snp_chr"]
    df = df[df["snp_chr"]!="chr-"]
    df[["rsID", "change"]]= df['riskAllele'].str.split('-', n=1, expand=True)
    print ("lines after remove rsid without a chromosome", df.shape)
    print(df.head)
    df["stop"] = df["snp_start"].apply(int)+1
    fulloutputfile = outputdirectory+rootfilename+".snp_to_bed.txt"
    df.to_csv(fulloutputfile, sep="\t")
    bed = df[["snp_chr", "snp_start", "stop"]]
    print ("lines before dropping duplicates", bed.shape)
    bed = bed.drop_duplicates()
    print ("lines after droping duplicates", bed.shape)
    bedoutputfile = outputdirectory+rootfilename+".unsorted.bed"
    bed.to_csv(bedoutputfile, header=False, index=False, sep="\t")

if __name__=="__main__":
        inputfile = sys.argv[1]
        outputdirectory = sys.argv[2]
        rootfilename = sys.argv[3]
        main(inputfile, outputdirectory, rootfilename)
