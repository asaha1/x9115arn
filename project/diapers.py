# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas

# <markdowncell>

# The system dynamics of diapers with weekly pickup/delivery::
# 
#       q  +-----+  r  +-----+  s
#     ---->|  C  |---->|  D  |---->
#      ^^  +-----+     +-++--+
#      ||                ||
#      ++= = = = = = = = ++
# 
# $C$ = stock of clean diapers
# 
# $D$ = stock of dirty diapers
# 
# $q$ = in-flow of clean diapers
# 
# $r$ = flow of clean diapers to dirty diapers
# 
# $s$ = out-flow of dirty diapers
# 
# To make this totally precise we need a system of equations relating the stocks and flows.  In this case, a system of difference equations with a timestep of one day works fine:
# 
# $C(t+1) = C(t) + q(t) - r(t)$
# 
# $D(t+1) = D(t) + r(t) - s(t)$
# 
# So far this seems like an example from intro applied math, and 100 other subjects.  But what makes it truely a system dyamics modeling example is the dashed arrow from compartment $D$ to flow $q$.  This signifies feedback, a core feature of SDM.  It is actually what makes me _want_ this simulation, because it makes things complicated (especially since I am a new parent, and therefore I am not sleeping much!)  The in-flow of clean diapers happens weekly (on Fridays... don't forget to take the dirty ones out on Thursday!), and the number of diapers that flow in is a function of the number of diapers that flow out... a week ago.  In equations,
# $$q(t) = s(t-7) + A(t) - C(t-7).$$
# 
# I've added something new here, $A(t)$ which is the stock of diapers I ask for.  It started out at 70, but I was worried about running out, so I raised
# it to 100.
# 
# So what is left to specify?  $r(t)$ is up to little Sidney, mostly, and $s(t)$ is equal to $D(t)$ on Thursdays and zero every other day.
# 
# Code that up and we have a system dynamics model.

# <codecell>

# what would make this code really cool is if I could use the "with" syntax on a pandas.DataFrame

# that requires a context manager

from contextlib import contextmanager
from numpy.core.numeric import arange

@contextmanager
def columns_in(df):
    col_names = df.columns
    col_list = [df[col] for col in col_names]
    try:
        yield tuple(col_list)
    finally:
        for i, col in enumerate(col_names):
            df[col] = col_list[i]

# <codecell>

T = 50
state = pandas.DataFrame(index=range(-7,T), columns=['C', 'D', 'q', 'r', 's'])

state.ix[-7:0, ['C']] = 70
state.ix[-7:0, ['D', 'q', 'r', 's']] = 0


# simulate
with columns_in(state) as (C,D,q,r,s):
    for t in range(T-1):
        C[t+1] = C[t] + q[t] - r[t]
        if C[t+1] < 0:
            C[t+1] = 0

        D[t+1] = D[t] + r[t] - s[t]
        
        q[t+1] = s[t+1-7] if t % 7 == 6 else 0
        # special case, first pickup, need to deliver something
        if t == 6:
            q[t+1] = 70.
        
        r[t+1] = 8.
        s[t+1] = D[t] if t % 7 == 6 else 0

t = state.filter(['C','D'])
t.columns = ['Clean', 'Dirty']
print state

# t.plot(linewidth=2, alpha=.9, figsize=(11.5, 4.5))
# plot(arange(-7,T)[::7], state.ix[::7,'C'], ':o', mec='k', ms=7, color='k', linewidth=2, alpha=.7, label='Weekly minimum')

# axis([-5,60,-10,120])
# grid()
# legend()
# xlabel('Time (Days)')
# ylabel('Diapers')

# <markdowncell>

# Now I can simulate my nightmare scenario, forgetting to take the dirty diapers out one week

# <codecell>

T = 50
state = pandas.DataFrame(index=range(-7,T), columns=['C', 'D', 'q', 'r', 's'])

state.ix[-7:0, 'C'] = 70
state.ix[-7:0, ['D', 'q', 'r', 's']] = 0


# simulate
with columns_in(state) as (C,D,q,r,s):
    for t in range(T-1):
        C[t+1] = C[t] + q[t] - r[t]
        if C[t+1] < 0:
            C[t+1] = 0

        D[t+1] = D[t] + r[t] - s[t]
        
        q[t+1] = s[t+1-7] if t % 7 == 6 else 0
        # special case, first pickup, need to deliver something
        if t == 6:
            q[t+1] = 70.
        
        r[t+1] = 8.
        s[t+1] = D[t] if t % 7 == 6 else 0
        
        # special case, forget to take the diapers out
        if t == 34:
            s[t+1] = 0

t = state.filter(['C','D'])
t.columns = ['Clean', 'Dirty']
print state
# t.plot(linewidth=2, alpha=.9, figsize=(11.5, 4.5))
# plot(arange(-7,T)[::7], state.ix[::7,'C'], ':o', mec='k', ms=7, color='k', linewidth=2, alpha=.7, label='Weekly minimum')
# 
# axis([-5,100,-10,130])
# grid()
# legend()
# xlabel('Time (Days)')
# ylabel('Diapers')

# <codecell>
