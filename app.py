import numpy as np
import pandas as pd
import operator
import math

# BGLM = {}
# with open('BGLM.txt') as f:
#     for line in f:
#         obj = line.strip().split("   ")
#         BGLM[obj[0]] = float(obj[1])

# Collection = []
# with open('Collection.txt') as f:
#     for line in f:
#         obj = line.strip().split(" ")
#         Collection.append(obj)


# C 
def c(w_i,d_j):
    x = pd.value_counts(d_j)
    return x[w_i]

topic = []
# E-step_rand

def P_T_W_D(word_i, doc_j, k):
    numerator = P_W_T(word_i, topic[k])*P_T_D(topic[k], doc_j)
    denominator = 0
    for i in range(k):
        denominator += P_W_T(word_i, topic[i])*P_T_D(topic[i], doc_j)

    return numerator/denominator
    

# M-step
len_docs = 2265
k = 3
doc = []
def P_W_T(word_i, topic_k):
    numerator = 0
    for j in range(2265):
        numerator += c(word_i, doc[j])*P_T_W_D(word_i,doc[j],k)
        
        denominator = 0
        for w in doc[j]:
            denominator += c(w, doc[j])*P_T_W_D(w,doc[j],k)
    return numerator/denominator
    
def P_T_D(topic_k, doc_j):
    numerator = 0 
    denominator = 0
    for w in doc_j:
        numerator += c(w,doc_j)*P_T_W_D(w,doc_j,k)
        denominator += len(doc_j)
    return numerator/denominator



