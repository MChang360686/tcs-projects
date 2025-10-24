l = [1, 2, 3, 4, 5]
l.append(2)
print(l)

d = {"a": 1, "b": 2}
d["c"] = 3
print(d)

s = {1, '1'}
print(s)

t = ("Ross", "Bob")
print(t[1])


class Person:
    def __init__(self, f_name, l_name, age, phone_num):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.phone_num = phone_num

    def get_f_name(self):
        return self.f_name
    
    def get_l_name(self):
        return self.l_name
    
chris = Person('chris', 'jones', 32, '123-098-4765')

d = {('jones', 'chris'): chris}
print(d[('jones', 'chris')].get_f_name())