from prettytable import PrettyTable

table=PrettyTable()

table.field_names=["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Sydney", 2058, 4336374, 1214.8])
print(table)

