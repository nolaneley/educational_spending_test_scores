import pandas as pd
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

df = pd.read_csv('school_spending_outcome.csv')

xy_chart = pygal.XY(stroke=False, show_legend=False)
for state, spend, m_score in zip(df.states_abbrev.values,df.spending.values,df.math.values):
    xy_chart.add(state, [(spend, m_score), {'color': 'blue'}])

xy_chart.render_to_file('hist.svg')