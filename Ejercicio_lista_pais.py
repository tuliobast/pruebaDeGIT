input_countries = input("Ingrese una lista de países separados por comas: ")
country_list = list(set(input_countries.split(",")))
country_list.sort()
print(", ".join(country_list))

