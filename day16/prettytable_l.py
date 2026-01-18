import prettytable

table = prettytable.PrettyTable()

table.add_column("Name 1 2 3", ["Name"])
table.add_column("John", ["21"])

print(table)