def convertTemperature(celsius):
    ans=[]
    Kelvin = celsius + 273.15
    Fahrenheit = celsius * 1.80 + 32.00
    ans.append(Kelvin)
    ans.append(Fahrenheit)
    return ans

celsius=36.50
print(convertTemperature(celsius))