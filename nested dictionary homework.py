computers={
    "computer1": {
        "name": "mackbook",
        "model":"air",
        "year":2019
    } ,
    "computer2":{
        "name":"samsung",
        "model":"galaxy book",
        "year":2023
    },
    "computer3": {
        "name":"microsoft",
        "model":"edge",
        "year":2025
    }
    
}

print(computers)
print(computers["computer1"])
print(computers["computer2"])

for keys in computers:
    print(keys)

computers.clear()
print(computers)

del computers
#delted the nested dictionary 


