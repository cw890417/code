import enum

#枚举
Season = enum.Enum('aaa',('a','b','c'))
print(Season.a)
print(Season.a.name)
print(Season.a.value)

print(Season['a'])
print(Season(3))

#返回所有枚举
for name,member in Season.__members__.items():
	print(name,'=>',member,',',member.value)