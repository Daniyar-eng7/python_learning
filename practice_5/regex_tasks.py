#1
import re
with open("raw.txt", "r") as f:
    raw=f.read()



result=re.match(r"ab*", raw)
print(result.group())


#2
import re

result = re.match(r"ab{2,3}", raw)
print(result.group())



#3
import re

print(re.findall(r"[a-z]+_[a-z]+", raw))

#4
import re

print(re.findall(r"[A-Z][a-z]+", raw))


#5
import re 
print(re.findall(r"a\\w+b", raw))


#6

print(re.sub(r"[ .,]",":", raw))


#7
def it (match):
  return match.group(1).upper()


print(re.sub(r"_([a-z])",it, raw))


#8
print(re.split(r"([A-Z])", raw))


#9
def it (match):
  return " "+match.group(0)


print(re.sub(r"[A-Z]",it, raw))



#10

def it (match):
  return "_" + match.group(1).lower()


print(re.sub(r"([A-Z])",it, raw))