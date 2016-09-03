# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import numpy as np
import csv
f = open('football.csv')
csv_f = csv.reader(f)

team = []
g_scored = []
g_allowed = []
gs_no_header = []
ga_no_header = []
diff = []
diff_abs = []

for i in csv_f:
    team.append(i[0])
    g_scored.append(i[5])
    g_allowed.append(i[6])

g_scored_nh = g_scored[1:]
g_allowed_nh = g_allowed[1:]

for j in range(len(g_scored_nh)):
    gs_no_header.append(int(g_scored_nh[j]))

for k in range(len(g_allowed_nh)):
    ga_no_header.append(int(g_allowed_nh[k]))

for h in range(len(gs_no_header)):
    diff.append(gs_no_header[h] - ga_no_header[h])

diff_abs = [abs(i) for i in diff]

min_ind = np.argmin(diff_abs)+1 # +1 is needed to account for the header

print "%s has the smallest absolute difference in 'for' and 'against' goals" %team[min_ind]
