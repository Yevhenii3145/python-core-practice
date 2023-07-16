from script_1 import get_length as get_length_by_diameter, math

def get_length(r):
    length = 2 * math.pi * r
    print(f"Radius = {r} Length = {length}")

get_length(90) # 565.4866776461628
print(math.pi) # 3.141592653589793
get_length_by_diameter(180) # 565.4866776461628
