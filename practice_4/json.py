import json

with open('sample-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


interfaces = data['imdata']


print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print(f"{'-'*50} {'-'*20} {'-'*8} {'-'*6}")

# 4. Обработка каждого интерфейса
for item in interfaces:
    attrs = item['l1PhysIf']['attributes']  
    dn = attrs.get('dn', '')
    desc = attrs.get('descr', '')           
    speed = attrs.get('speed', '')
    mtu = attrs.get('mtu', '')


    print(f"{dn:<50} {desc:<20} {speed:<8} {mtu:<6}")