import numpy as np
import pandas as pd
import operator
import math
import random

# BGLM = {}
# with open('BGLM.txt') as f:
#     for line in f:
#         obj = line.strip().split("   ")
#         BGLM[obj[0]] = float(obj[1])

Collection = []
with open('Collection.txt') as f:
    for line in f:
        x = [str(i) for i in line.split() if i.isdigit()]
        Collection.append(x)


len_docs = len(Collection)
len_topic = 3
doc = Collection



words = []
for line in Collection:
    for w in line:
        words.append(w)
words_counts = pd.value_counts(words)



# C 
def c(w_i,d_j):
    x = pd.value_counts(Collection[j])
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
def P_W_T(word_i, topic_k):
    numerator = 0
    for j in range(len_docs):
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


wi_Tk = [[ random.random() for y in range(len(words_counts)) ] for x in range( len_topic ) ]
Tk_dj = [[ random.random() for y in range(len(Collection)) ] for x in range( len_topic ) ]


for k in range(len_topic):
    numerator = 0
    denominator = 0
    for j in range(len(Collection)):
        numerator += c(i,j)*P_T_W_D(i,j,k)
        for i in range(len(Collection[j])):
            for ip in range(len(Collection[j])):
                denominator += c(ip,j)*P_T_W_D(ip,j,k)
    
            wi_Tk[i][k] = numerator/denominator

            