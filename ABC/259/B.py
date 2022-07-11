a, b, d = map(int, input().split())
import math
X = a* math.cos(math.radians(d)) - b*math.sin(math.radians(d))
Y = a* math.sin(math.radians(d)) + b*math.cos(math.radians(d))

print(X, Y)