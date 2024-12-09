import pandas as pd

from scipy.stats import spearmanr
from Bio.Data.CodonTable import unambiguous_dna_by_id
from Bio.SeqUtils import seq3

def aa_dict_creator(letters_3: bool = True , CODON_TABLE: int = 2, full: bool = True) -> dict[str, list[str]]:
    aa_dict = {}
    stop_codons = {codon:'_' for codon in unambiguous_dna_by_id[CODON_TABLE].stop_codons}
    c_aa_dic = unambiguous_dna_by_id[CODON_TABLE].forward_table | stop_codons
    for (codon, aa) in c_aa_dic.items():
        if letters_3:
            aa = seq3(aa)
        if full == True:
            if codon[:2] == 'CT':
                aa = 'Leu1' if letters_3==True else 'L1'
            elif codon == 'TTG' or codon == 'TTA':
                aa = 'Leu2' if letters_3==True else 'L2'
            if codon[:2] == 'TC':
                aa = 'Ser2' if letters_3==True else 'S1'
            elif codon == 'AGT' or codon == 'AGC':
                aa = 'Ser1' if letters_3==True else 'S2'
        if aa not in aa_dict:
            aa_dict[aa] = []
        aa_dict[aa].append(codon)
    return dict(sorted(aa_dict.items()))

def correlation_calculation(cu_records: pd.DataFrame) -> pd.Series:
    observed_cu = cu_records.iloc[0]
    stat_values: pd.Series = cu_records.apply(spearmanr, axis=1, b=observed_cu)
    spear_corr = pd.DataFrame(data={'rho': stat_values.str[0],
                                    'pvalue': stat_values.str[1]})
    return spear_corr