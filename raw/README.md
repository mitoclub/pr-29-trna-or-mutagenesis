# raw

Unchangable raw data

### MutSpec&CodonUsage.csv

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
    Columns are named in the form 'Codon_Gene'. For example, 'AAA_ND6', 'TGC_CytB',...   
    - 15-78th   ND6
    - 79-142th  CytB 
    - 143-206th ND4
    - 207-270th ND4L
    - 271-334th ATP8
    - 335-398th ND3
    - 399-462th COX1
    - 463-526th ATP6
    - 527-590th COX3
    - 591-654th COX2
    - 655-718th ND2
    - 719-782th ND5
    - 783-846th ND1