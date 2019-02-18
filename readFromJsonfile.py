import json

with open(r'C:\Users\1024994\Desktop\student.json', mode = 'r') as gg:
          data = json.load(gg)
          for item in data['data']:
              print("{} {}".format(item['name'],item['marks']))
