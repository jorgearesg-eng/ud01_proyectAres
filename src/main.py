"""
EUR/USD converter
Author : Ares Jorge
Date 19/10/2026
Version: 1.0
"""

CONVERSION_RATE = 1.8
celsius = float(input("Enter temp in ºC: "))

farenheit = (celsius * CONVERSION_RATE) + 32
print(f"{celsius:.2f} ºC = {farenheit:.2f} ºF")