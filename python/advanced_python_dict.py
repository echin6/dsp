import csv
f = open('faculty.csv')
csv_f = csv.reader(f)

faculty_dict = {}

for row in csv_f:
    key = row[0]
    if key in faculty_dict:
        pass
    faculty_dict[key] = row[1:]

split_dict = {tuple(map(str, key.split())): value for key, value in faculty_dict.items()}

last_dict = {key[len(key)-1]: value for key, value in split_dict.items()}

last_first3 = {k: last_dict[k] for k in sorted(last_dict.keys())[:3]}

split_first3 = {k: split_dict[k] for k in sorted(split_dict.keys())[:3]}

#last_dict_sorted = {k: last_dict[k] for k in sorted(last_dict.keys())}

print last_first3

print split_first3

for k in sorted(last_dict.keys()):
	value = last_dict[k]
	print {k: value}
	
#print last_dict_sorted
