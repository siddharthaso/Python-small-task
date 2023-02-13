class Y: print("Y")
class Z:print("Z")
class X:print("X")
class W:print("W")
class A(X,Y):pass
class B(Y,Z):pass
class M(B,W,A,Z):pass


print(M.mro())
print(M.__mro__)