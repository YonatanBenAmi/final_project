from division_data import DivisionData

division = DivisionData()

all_data = division.get_list_data()
print(division.get_metadata_parts(all_data))