# raw

Unchangable raw data

### MutSpec_CU_tRNA.csv

All data about mutational spectrum, codon usage and tRNA we analyse
The table consists these columns:
- **1st Species**  
    Species names in "Genus_Species" form in Latin
- **2nd Taxonomy**  
    Taxonomy in "Domain_Kingdom_ ... _Family_Genus" form in Latin
- **3-14th Mutational spectrum**  
    There are 12 columns here:  
    'A>T', 'A>G', 'A>C', 'T>A', 'T>G', 'T>C', 'G>A', 'G>T', 'G>C', 'C>A', 'C>T', 'C>G'
- **15-846th Codon usage**  
    64 columns with codon usage for each mtDNA gene  
    The first 64 columns are total codon usage for 12 genes except ND6 (on the opposite strand). Columns are named in the form 'Codon_12'. For example, 'AAA_12', 'TGC_12',...  
    The rest columns are named in the same way but with gene name. . For example, 'AAA_ND6', 'TGC_COX3',...
    - 15-78th   Sum of each codon usage for 12 genes  
    - 79-142th  ND6 
    - 143-206th CytB
    - 207-270th ND4
    - 271-334th ND4L
    - 335-398th ATP8
    - 399-462th ND3
    - 463-526th COX1
    - 527-590th ATP6
    - 591-654th COX3
    - 655-718th COX2
    - 719-782th ND2
    - 783-846th ND5
    - 847-910th ND1
- **911-932th Anticodons**  
    22 columns with tRNAs' anticodons to corresponding amino acids  
    Columns are named in the form 'Amino acid_Ac'. For example, 'Leu_Ac', 'Tyr_Ac',...  
    Leucine and Serine both have 2 tRNAs. Ser1 refers to AGY codons (Ser2 to UCN, Leu1 to CUN Leu2 to UUR).  
    This data was given from [mitotRNAdb](http://mttrna.bioinf.uni-leipzig.de/mtDataOutput/).  

### mitotRNAdb.mfa
Multifasta file with all records from [mitotRNAdb](http://mttrna.bioinf.uni-leipzig.de/mtDataOutput/)