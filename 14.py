
# ------------------------------------------------------------------------------------------------------
#  Initialize dictionary with default values.
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
#initialize the keys with the same values.
employees_with_defaults = dict(zip(employees,defaults.values()))
print(employees_with_defaults)