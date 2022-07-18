# TSV to Excell Table

import pandas as pd

try:
    linkUrl = input("tsv file name with extension: ")
    df = pd.read_csv(linkUrl, sep=",", header=0) #sep is your file seperator
    df.to_excel("excell-output.xlsx")
    print("Done")
    
except:
    print("Check the file name or extension")
