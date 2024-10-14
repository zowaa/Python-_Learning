import math

def calculateSinCosTan(x):
	sin = math.sin(x)
	cos = math.cos(x)
	tan = math.tan(x)

	return [sin, cos, tan]

[sin, cos, tan] = calculateSinCosTan(3)
print(sin)
print(cos)
print(tan)