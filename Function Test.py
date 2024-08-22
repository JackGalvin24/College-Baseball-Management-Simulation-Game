import random
import sqlite3
import numpy as np
from collections import Counter

POSITIONAL_ARRAY = ['P', 'SS', 'C', 'CF', '3B', 'RF', '1B', '2B', 'DH', 'LF']
POS_WEIGHT_LISTS = {

'P': (['1B', 'LF', 'RF', '3B', 'CF', 'SS', 'C'],[0.22, 0.22, 0.22, 0.22, 0.08, 0.038, 0.002], [.9, .1]),
'SS': (['3B', '2B', 'CF', 'LF', 'RF',  'C'],[0.54, 0.24, 0.1, 0.04, 0.04, 0.04], [.6, .33, .07]),
'C': (['1B', '3B', 'RF', 'SS', 'CF', 'LF'],[.75,.10,.10,.0225,.0225,.005],[.5,.15,.35]),
'CF': (['RF', '2B', 'LF', '2B'],[],[]),
'3B': (['1B', 'SS', 'RF', 'LF', 'CF', 'C'], [.75, .15, ],[]),
'RF': (['LF', 'CF', '1B', '3B', 'C'],[],[]),
'1B': (['RF', 'SS', 'CF', 'LF', 'C', '3B'],[],[]),
'2B': (['SS', 'CF', '3B', 'C', 'LF', 'RF'],[],[]),
'LF': (['CF', 'SS', '2B', 'RF', '1B'],[],[])
}



pos_p = []

#Weight for position 1
pos_1_weight = [0.44, 0.22, 0.13, 0.1, 0.04, 0.02, 0.03, 0.01, 0.007, 0.003]

pos_1 = np.random.choice(POSITIONAL_ARRAY, 1, False, pos_1_weight)

pos_p.append(pos_1.tolist()[0])

if pos_p[0] == 'DH':
    #stays at 1 position
    print(pos_p)

pos_lists = POS_WEIGHT_LISTS.get(pos_p[0])

position_opts = pos_lists[0]
weights = pos_lists[1]


if pos_p[0] == 'P': can_play = np.random.choice([0,1], 1, False, pos_lists[2])
else: can_play = np.random.choice([1,2,0], 1, False, pos_lists[2])

num = can_play[0]
print(num)

if can_play[0] > 0:
        num = can_play[0]
        sel = np.random.choice(position_opts, num, False, weights)
        for x in range(0,num):
                     pos_p.append(sel.tolist()[x])
                    

print(pos_p)
      
