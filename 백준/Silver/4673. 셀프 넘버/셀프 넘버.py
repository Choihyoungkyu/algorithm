def self(n):
    hap = 0
    for i in range(len(str(n))):
        hap += int(str(n)[i])
    return n + hap
num_list = list(range(10000))
for i in range(10000):
    if self(i) in num_list:
        num_list.remove(self(i))
for i in num_list:
    print(i)