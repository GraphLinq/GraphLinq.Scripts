import json

with open('node_schema.json',) as data_file:
    data = json.load(data_file)
    for v in data:
        #print(v['NodeType'])
        #print(v['FriendlyName'])
        #print(v['NodeGroupName'])
        #print(v['NodeBlockType'])
        #print(v['NodeDescription'])
        #print()
        z = 0
        with open('node_schema.json',) as d:
            d = json.load(d)
            for x in d:
                if(v['NodeType'] == x['NodeType']):
                    z = z + 1
                    if (z > 1):
                        print("V")
                        print(v['NodeType'])
                        print(v['FriendlyName'])
                        print(v['NodeGroupName'])
                        print(v['NodeBlockType'])
                        print(v['NodeDescription'])
                        print("---")
                        print("X")
                        print(x['NodeType'])
                        print(x['FriendlyName'])
                        print(x['NodeGroupName'])
                        print(x['NodeBlockType'])
                        print(x['NodeDescription'])
                        print()
                        z = 1
            z = 0
