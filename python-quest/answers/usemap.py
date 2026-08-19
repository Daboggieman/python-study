celcius_temp = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0]

def to_kelvin(predicate) :
    kelvin = predicate + 273.15
    return kelvin

convert = list(map(to_kelvin, celcius_temp))

print(convert)