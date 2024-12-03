#!/usr/bin/env python3
from countryinfo import CountryInfo
 
country_list = ["england", "spain"]
city=["london", "madrid"]
 
country_input = str(input("Which country would you like to know?"))
 
if country_input in country_list:
    position = country_list.index(country_input)
    print (city[position])
 
else:
    country = CountryInfo(country_input)
    city.append(country.capital())
    country_list.append(country_input)
    print (city)
    print (country_list)