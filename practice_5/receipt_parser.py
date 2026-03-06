import re

with open("raw.txt", "r")as f:
    sss=f.read()

#1    
cost=re.findall(r"Стоимость\n(\d+,\d+)", sss)
print(cost)


#2
name= re.findall(r"\d[.]\n\w+", sss)
print(name)


#3
total = re.findall(r"ИТОГО:\\n(\\d[\\d\\s]*,\\d+)", sss)[0]
print(total)


#4
date=re.findall(r"Время: (\\d{2}\\.\\d{2}\\.\\d{4} \\d{2}:\\d{2}:\\d{2})", sss)
print(date)

#5
payment=re.findall(r"Банковская карта:\n\d+\s\d+,\d+", sss)
print(payment)

#6
data = {
    "дата": date,
    "товары": [{"название": n, "стоимость": c} for n, c in zip(name, cost)],
    "оплата": {"метод": "Банковская карта", "сумма": payment},
    "итого": total
}
