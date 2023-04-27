# raw

Unchangable raw data

### MutSpec_CU_tRNA.csv

All data about mutational spectrum, codon usage and tRNA we analyse
The table consists these columns:
- **Species**  
    Species names in "Genus_Species" form in Latin
- **Class**  
    Taxonomy in "Domain_Kingdom_ ... _Family_Genus" form in Latin
- **Mutational spectrum**  
    There are 12 columns here:  
    'A>T', 'A>G', 'A>C', 'T>A', 'T>G', 'T>C', 'G>A', 'G>T', 'G>C', 'C>A', 'C>T', 'C>G'
- **Codon usage**  
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
- **Amino acid usage**  
    Amino acid usage of 12 genes on heavy chain  
    23 columns: 'Ala', 'Arg', 'Asn', 'Asp', 'Cys', 'Gln', 'Glu', 'Gly', 'His', 'Ile', 'Leu1', 'Leu2', 'Lys', 'Met', 'Phe', 'Pro', 'Ser1', 'Ser2', 'Thr', 'Trp', 'Tyr', 'Val', 'Xaa'  
    'Xaa' is stop codons
- **Anticodons of tRNAs**  
    22 columns with tRNAs' anticodons to corresponding amino acids:  
    'Ala_Ac', 'Arg_Ac', 'Asn_Ac', 'Asp_Ac', 'Cys_Ac', 'Gln_Ac', 'Glu_Ac', 'Gly_Ac', 'His_Ac', 'Ile_Ac', 'Leu1_Ac', 'Leu2_Ac', 'Lys_Ac', 'Met_Ac', 'Phe_Ac', 'Pro_Ac', 'Ser1_Ac', 'Ser2_Ac', 'Thr_Ac', 'Trp_Ac', 'Tyr_Ac', 'Val_Ac'  
    Columns are named in the form 'Amino acid_Ac'. For example, 'Leu_Ac', 'Tyr_Ac',...  
    Leucine and Serine both have 2 tRNAs. Ser1 refers to AGY codons (Ser2 to UCN, Leu1 to CUN Leu2 to UUR).  
    This data was given from [mitotRNAdb](http://mttrna.bioinf.uni-leipzig.de/mtDataOutput/).  
- **Gibbs energy**  
    22 columns with calculated Gibbs energy based on secondary structure of tRNAs  
    'Ala_Ge', 'Arg_Ge', 'Asn_Ge', 'Asp_Ge', 'Cys_Ge', 'Gln_Ge', 'Glu_Ge', 'Gly_Ge', 'His_Ge', 'Ile_Ge', 'Leu1_Ge', 'Leu2_Ge', 'Lys_Ge', 'Met_Ge', 'Phe_Ge', 'Pro_Ge', 'Ser1_Ge', 'Ser2_Ge', 'Thr_Ge', 'Trp_Ge', 'Tyr_Ge', 'Val_Ge'  
- **Taxonomy**  
    Extanded taxonomy from NCBI 
### mitotRNAdb.mfa
Multifasta file with all records from [mitotRNAdb](http://mttrna.bioinf.uni-leipzig.de/mtDataOutput/)