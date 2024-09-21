from aitd import *
import pickle

seqs = [
    Sequence("DNA", "Seq1", "ATGTGGAAAACACTGCATCAACTGGCGATCCCACCACGGCTGTATCAAATCTGTGGCTGGTTTATACCGTGGCTGGCAATTGCCAGTGTGGTCGTGCTTACCGTCGGCTGGATCTGGGGATTCGGCTTTGCTCCGGCTGATTATCAGCAGGGAAATAGCTACCGCATTATCTACCTGCATGTGCCTGCGGCGATCTGGTCGATGGGCATTTATGCATCAATGGCAGTGGCAGCGTTTATTGGCCTTGTCTGGCAGATGAAAATGGCCAACCTGGCGGTGGCGGCGATGGCCCCCATTGGTGCCGTGTTTACCTTTATTGCCCTGGTTACCGGCTCTGCATGGGGAAAACCGATGTGGGGCACCTGGTGGGTATGGGATGCACGTCTGACTTCTGAACTGGTGCTGCTGTTTTTGTATGTGGGTGTGATTGCCCTGTGGCACGCCTTCGACGACCGCCGTCTGGCGGGCCGTGCGGCAGGTATCCTGGTGCTGATTGGCGTGGTGAATCTGCCGATTATTCATTACTCCGTGGAGTGGTGGAACACCCTGCATCAGGGATCAACGCGGATGCAGCAAAGTATCGATCCGGCGATGCGTTCGCCGCTGCGCTGGTCGATTTTTGGCTTCCTGCTCCTGTCTGCCACGCTGACGCTGATGCGGATGCGTAATTTGATTTTGCTGATGGAAAAACGCCGTCCGTGGGTGAGTGAACTGATACTGAAAAGAGGCCGTAAATGA"),
    Sequence("DNA", "Seq2", "ATGAATATTCGCCGTAAAAACCGCTTGTGGATTGCCTGTGCCGTGTTGGCAGGGCTGGCGCTGACTATCGGTCTGGTGCTATATGCGCTGCGCTCGAATATCGATCTCTTTTATACGCCGGGGGAAATTCTCTACGGCAAGCGTGAAACTCAGCAGATGCCGGAAGTCGGTCAGCGTCTGCGCGTTGGCGGGATGGTGATGCCGGGTAGTGTGCAGCGCGATCCCAATTCGCTGAAAGTGACCTTCACCATTTACGACGCTGAAGGCTCAGTGGATGTCTCTTACGAAGGCATTTTGCCGGATCTGTTCCGTGAAGGGCAGGGCGTTGTGGTGCAGGGCGAGCTGGAAAAAGGCAATCATATCCTCGCAAAAGAAGTGCTGGCGAAACATGATGAAAACTACACGCCGCCAGAAGTTGAGAAAGCGATGGAAGCTAACCACCGTCGCCCGGCGAGTGTTTATAAGGACCCAGCATCATGA"),
    Sequence("DNA", "Seq3", "GACTCAGGCCCAGGGCGCTGCCCGGGTGGCCGCGGCGCTGGACGACGGCTCGGCCCTTGGCCGCTTCGAGCGGATGCTGGCGGCGCAGGGCGTGGATCCCGGTCTGGCCCGAGCCCTGTGCTCGGGAAGTCCCGCAGAACGCCGGCAGCTGCTGCCTCGCGCCCGGGAGCAGGAGGAGCTGCTGGCGCCCGCAGATGGTGAGCGTCGGGGGAGTCCCCGTCCTTCCGCCTCCGCCATCCCCTTCCCTTCCCGAGGCCCCGCCCCTTCCCGAGCCCGCGCCTCTCAGCCCCTCTCCCCGCAGGCACCGTGGAGCTGGTCCGGGCGCTGCCGCTGGCGCTGGTGCTGCACGAGCTCGGGGCCGGGCGCAGCCGCGCTGGGGAGCCGCTCCGCCTGGGGGTGGGCGCAGAGCTGCTGGTCGACGTGGGTCAGAGGCTGCGCCGTGGTGAGCGCCGCCCCCGCCCTGCTGGCCCCGCACCCCCGCCCAGCTCCGGCCGCGCGGCCTCTAACAGCCCCTCGCTCTGCAGGGACCCCCTGGCTCCGCGTGCACCGGGACGGCCCCGCGCTCAGCGGCCCGCAGAGCCGCGCCCTGCAGGAGGCGCTCGTACTCTCCGACCGCGCGCCATTCGCCGCCCCCTCGCCCTTCGCAGAGCTCGTTCTGCCGCCGCAGCAATAAAGCTCCTTTGCCGCGAAACCTTGTCAGTGCTTGGGCGGGAGCGGAAGGATCCAGGGCTGCGGAGGCGGGGGCCGTCTCGATGAACACGTGACCCCCGGCGGGCTCCGCCTTCCGCGCACGCGCTGAGAGCCTGTCAGCGGCTGCGCCCGTGTGCGCATGCGCAGCTCCGGGGACGCCTGCGCCCTGCCTGTGAGCGTGTGGCGCCCGCTTTCCCTGAGCCGGCGGGGCAGAGCGCAGGGAGCTGGAGGTCGGCGCTTCCTCTCGTGCTTGGTCCACTGACGCGCGGCCCCGCCGCGAGGTGCGGACGCCGGGGCTGGGAGGGGAGGAGGTAGCCCTGAGGACTCGCTGGACTCCGGGGTAGTTTCCCAGCTCCGGCTACTGCGCGGGGCTGGCGGGGCACACCCCAGGGCGCGCTGGAGGCCGGAGCGAGGCTGGGGCGCCCGTGGGAGGCTCCCAGCAGGCACCGGTGTTCTCGCGGCCAAGCACAGTTATAACGCGCTCGCGCGGCGCTTCGAGTGGTCCTGGAACCTTTCTGGCCACGAGGGCGCTGGCCTTGCTGGGGAGGGCACAAACCCAGAACCGCCCGGGCGGGGGTGCAGTGAGTCCTCGGGAGGGTGCCCTCAGCAGGAGGGGGCAGTGACCGGGAGTCCTGAGACCTCCACCTAGCAAACCTTCTGCGGGGGCCCGTGGGAAAGGCTCAAAGGTCACCAACGCAAAGGCAGGGCGTCGGCTGTGAGCCCGGAGGAGCTGCTGGGAAGCCTGGATGTGAGGAGGGTGGGGTTTTGTGGCGGGTGGAAGTGTCGTGCGTCTCTGCCAGGAGAGGTTAAACACAGCCGGCGGGCAGAGTCTGAGCTCCGGGGGTAGGTCGTGCAGGTTTTCTGCTGGGAGTGTGGAGGAAGGCCGCGGTTGGTTGAAGTGGCTGGAGGTAACAGGAAAGTGTTGGAGGAATCGGTTGCTCTCGGGGATTGCAAGCCAGAGAGTTACCCACCTCCTTTTAAGAAATGGGTTTATTGCAAATAGATAACGTGGTTAGTTCAGGCAAGGCATGCACTTGGAATGCTTTCCGTCAGCAAGAGGTTCACCTTGCTGAGGTGCAGGTGCAGGGCAGGGTGCGGTGACAGGCTGGTGATCCCAGGTAGAGGACAGGAGTGACAGGTGTGGTTGCCCAGGTGTGGATGTTTGGTGGAGGTGGAGTTCTGAGCTCAGGTGAGCAGCTGCAAATGCCTGTTAAGCCTGAACGTGGGCTGGGTCCTTCAGATGGGTGGCTGGTCTCAAGTCGCAGGGGCAGCCCAGGCACTGTCCTGGGCCTTCCCTTCTGGCTCCTGACGCCTGTGCTTGTTTCCAGGAGCATCAGATCCATGCTGCTGCTGACTCGGAGCCCCACAGCTTGGCACAGGCTCTCTCAGCTCAAGCCTCGGGTCCTCCCTGGGACCCTGGGAGGCCAGGCCCTGCATCTGAGGTCCTGGCTTTTGTCAAGGCAGGGCCCTGCAGAGACAGGTGGGCAGGGCCAGCCCCAGGGCCCTGGGCTTCGAACCCGGCTGCTGATCACAGGCCTGTTCGGGGCTGGACTCGGTGGGGCCTGGCTGGCCCTGAGGGCTGAGAAGGAGAGGCTGCAGCAGCAAAAGCGAACAGAAGCCCTGCGCCAGGCAGCTGTGGGCCAGGGCGACTTCCACCTGCTGGATCACAGAGGCCGGGCTCGCTGCAAGGCTGACTTCCGGGGCCAGTGGGTGCTGATGTACTTTGGCTTCACTCACTGCCCTGACATCTGCCCAGACGAGCTGGAGAAGCTGGTGCAGGTGGTGCGGCAGCTGGAAGCAGAGCCTGGTTTGCCTCCAGTGCAGCCTGTCTTCATCACTGTGGACCCCGAGCGGGACGACGTTGAAGCCATGGCCCGCTACGTCCAGGACTTCCACCCAAGACTGTTGGGTCTGACCGGCTCCACCAAACAGGTTGCCCAGGCTAGTCACAGTTACCGCGTGTACTACAATGCAGGCCCCAAGGATGAGGACCAGGACTACATCGTGGACCACTCCATTGCCATCTACCTGCTCAACCCTGACGGCCTCTTCACGGATTACTACGGCCGGAGCAGATCGGCTGAGCAGATCTCAGACAGTGTGCGGCGGCACATGGCGGCTTTCCGCAGTGTCCTGTCTTGAGCCACTGCAGTCTGGGCCCCATCATTAAACGGGCTGCGTTTAA")
]
tree = getattr(xerlist.TreePlanterList, "UPGMA")(
    seqs, getattr(xerlist.ProcessorList, "needleman-wunsch")
)

with open("test\\data\\tree\\EcoliccmC.EcoliccmE.HsapiensSCO2.tree","wb") as f:
    pickle.dump(tree,f)

print(tree[0],tree[1])

getattr(xerlist.DisplayList, "custom")(tree[0],tree[1],3+1)
