from ProspectClass import Prospect
from PlayerClass import Player
from CreationClass import ClassGen
from ScoutClass import Scout
from ScoutReport import ScoutReport
import sqlite3


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

lists = POS_WEIGHT_LISTS.get('P')
print(lists[0][0])


"""x= Prospect('West')
print(x)"""

#c = ClassGen(2024)


