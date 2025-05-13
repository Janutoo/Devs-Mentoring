# Zad 9.
# W załączeniu znajduje się plik data.json. Przechowuje on informacje o różnych pakietach informacji.
#  Twoim zadaniem jest napisanie skryptu, który będzie odczytywał taki pliku i drukował poniższy 
# komunikat zawierający informacje o każdym z pakietów:


# Interface Status
# ================================================================================
# DN                                                 Description           Speed    MTU  
# -------------------------------------------------- --------------------  ------  ------
# topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
# topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
# topology/pod-1/node-201/sys/phys-[eth1/35]                          

import json

with open("E:\github\Devs-Mentoring\T6\data.json","r") as file:
    data = json.load(file)

print("Interface Status")
print("="*80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<5}")
print("-"*80)

for item in data["imdata"]:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes['dn']
    if dn in ["topology/pod-1/node-201/sys/phys-[eth1/33]", "topology/pod-1/node-201/sys/phys-[eth1/34]", "topology/pod-1/node-201/sys/phys-[eth1/35]"]:
        description = attributes["descr"]
        speed = attributes['speed']
        mtu = attributes["mtu"]
        print(f"{dn:<50} {description:<20} {speed:<8} {mtu:<5}")


