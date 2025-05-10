
names = {
    "Marlon": "Meier",
    "Adam": "Nash",
    "Lamine": "Jamal",
    "Adam": "Obi"
}

print(names) 

print(names["Adam"])

names["Adamo"] = "Vicent"

del names["Adam"] 

names["Hannes"] = "Newman"

print(names)

for name in names:
    last_name = names[name]
    print(last_name) 






