# raw

Unchangable raw data

### MutSpec&CodonUsage.csv

The table consists these columns:
- 1st Species  
    Species names in "Genus_Species" form in Latin
- 2nd Taxonomy  
    Taxonomy in "Domain_Kingdom_ ... _Family_Genus" form in Latin
- 3-14th Mutational spectum
    There are 12 columns here:  
    'A>T', 'A>G', 'A>C', 'T>A', 'T>G', 'T>C', 'G>A', 'G>T', 'G>C', 'C>A', 'C>T', 'C>G'
- 15-910th Codon usages
    Codon usage gene in 64 columns per every mtDNA gene  
    The first 64 columns are total codon usage of 12 genes except ND6(on the opposite strand). Columns are named in the form 'Codon_12'. For example, 'AAA_12', 'TGC_12',...)  
    Next all columns are named in the same way but gene name, '_ND6', '_CytB' instead of '_12'. For example, 'AAA_ND6', 'TGC_CytB'
    - 15-78th   Sum of 12 genes
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