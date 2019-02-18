import json

with open(r"C:\Users\1024994\Desktop\student.json",mode = 'r') as json_file:  
    data = json.load(json_file)
    for it in data["data"]:
        print(it['name'])
        print(it['marks'])
    '''
    try:
        for p in data['people']:
             print('Name: ' + p['name'])
             print('Website: ' + p['website'])
             print('From: ' + p['from'])
             print('')
    except:
        print("exception\n")
        print(data["maps"])

  '''  
