import sys

output_file = sys.argv[1]
start_year = int(sys.argv[2]) #year corresponding to issue_num_start
issue_num_start = int(sys.argv[3]) #first available 
issue_num_end = int(sys.argv[4]) #last available 
journal = sys.argv[5]

academics = {}

for i in range(issue_num_start, issue_num_end+1):
    filename = journal + '.' + str(i) + '.extracted.txt'
    filepath = './../data/extracted_names/' + journal + '/' + filename
    year = start_year - issue_num_start + i
    with open(filepath, 'r') as input:
        for line in input:
            line = line.rstrip()
            if line in academics and year == academics[line][-1][1] + 1:
                academics[line][-1][1] += 1
            elif line not in academics:
                academics[line] = [[year, year]]
            else: #there was an interval
                academics[line].append([year, year])

result = open(output_file, 'w')
for key in academics.keys():
    this_res = key + ',' + ','.join([str(year) for interval in academics[key] for year in interval]) + '\n'
    result.write(this_res)
            
result.close()