import pandas

change=pandas.DataFrame({
    '2011':[3205, 48077],
    '2012':[3609, 61093]},
    index = ['Netflix','Amazon']
)
print(change.pct_change()) 