import json

data = {}  
data['people'] = []  
data['people'].append({  
    'name': 'Scikkk',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({  
    'name': 'Larry',
    'website': 'google.com',
    'from': 'murali krishna'
})
data['people'].append({  
    'name': 'Tim',
    'website': 'facebook.com',
    'from': 'Alabama'
})

maps = {"maps": [
        {
            "id": "blabla",
            "iscategorical": "0"
        },
        {
            "id": "blabla",
            "iscategorical": "0"
        }
    ],
    "masks": {
        "id": "valore"
    },
    "om_points": "value",
    "parameters": {
        "id": "valore"
    }}
with open (r"C:\Users\1024994\writejson.json",mode = 'w') as outfile:  
    json.dump(data, outfile,indent=4)
    
print("Done with dumping 1")


with open (r"C:\Users\1024994\writejson.json",mode = 'w') as outtfile:  
    json.dump(maps, outtfile,indent=4)
    outfile.close()
print("Done with dumping 2")
