class vehicle:
	def __init__(self) -> None:
		self.a = 5
		self.b = 1
		self.c =self.a+self.b
		
class s(vehicle):
	b=2
	def __init__(self) -> None:
		super().__init__()
		self.c = 4

v = s()
print(v.c)
print(v.b)
print(s.b)

def f():
	try:
		for i in range(10):
			yield i
	except StopIteration:
		print("sd")

sdd = f()
print(next(sdd))
print(next(sdd))
print(next(sdd))
print(next(sdd))
print(next(sdd))
print(next(sdd))
print(next(sdd))
print(next(sdd))
print(next(sdd))
print(next(sdd))
print(next(sdd))