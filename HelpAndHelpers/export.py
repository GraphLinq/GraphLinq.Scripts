import json
import csv

with open('nodes.csv', 'w', newline='') as csvfile:
    w = csv.writer(csvfile, delimiter=',', quotechar='"')
    w.writerow(['NodeType', 'FriendlyName', 'NodeGroupName', 'NodeBlockType', 'NodeDescription'])
    with open('node_schema.json',) as data_file:
        data = json.load(data_file)
        for v in data:
            #print(v['NodeType'].strip())
            #print(v['FriendlyName'].strip())
            #print(v['NodeGroupName'].strip())
            #print(v['NodeBlockType'].strip())
            #print(v['NodeDescription'].strip())
            #print()
            w.writerow([v['NodeType'].strip(), v['FriendlyName'].strip(), v['NodeGroupName'].strip(), v['NodeBlockType'].strip(), v['NodeDescription'].strip()])

print("done")
print()
