# ISEN 302 engineering economics
# Xiaochen Yan UIN: 327002462

# compound interest
def FP(P, i, n):
	F = P * (1+i)**n
	return F
def PF(F, i, n):
	P = F / (1+i)**n
	return P

# uniforn series factors
def PA(A, i, n):
	r = (1+i)**n
	P = A * ((r-1)/(r*i))
	return P
def FA(A, i, n):
	r = (1+i)**n
	F = A * ((r-1)/i)
	return F
def AP(P, i, n):
	r = (1+i)**n
	A = P / ((r-1)/(r*i))
	return A
def AF(F, i, n):
	r = (1+i)**n
	A = F / ((r-1)/i)
	return A

# arthmetic gradient
def PG(G, i, n):
	r = (1+i)**n
	P = G * (r-(i*n)-1)/((i**2)*r)
	return P
def AG(G, i, n):
	r = (1+i)**n
	A = (1/i) - (n/(r-1))
	return A

# geometric gradient
def Pg(A, g, i, n):
	r1 = (1+i)**(-n)
	r2 = (1+g)**n
	P = A*(1-r1*r2)/(1-g)
	return P

# when n = infinite:
# P = A/i, A = P*i

# calculator
print(FP(10000, 0.11, 30))
