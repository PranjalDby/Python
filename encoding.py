# converting a dict type to json called serialisation

import json
person = {"names":"john","Age":30,"city":"California","HasChildrebn":False}
persnjson =json.dumps(person,indent=4,sort_keys=True)
print(persnjson)

with open('person.json','w') as file:
    json.dump(person,file,indent=4)

topy = json.loads(persnjson)
print(topy)