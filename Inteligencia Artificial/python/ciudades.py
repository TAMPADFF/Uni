def ciudades_grandes(ciudades):
    ciudades_filtradas = {ciudad: poblacion for ciudad, poblacion in ciudades.items() if poblacion > 100000}

    return sorted(ciudades_filtradas.items(), key=lambda x: x[1], reverse=True)

ciudades = {
    "Ciudad de México": 9209944,
    "São Paulo": 12106920,
    "Buenos Aires": 3075646,
    "Lima": 9674755,
    "Bogotá": 7968095,
    "Santiago": 5615000,
    "Ciudad de Guatemala": 995393,
    "Caracas": 1943901,
    "Quito": 1628700,
    "La Paz": 816044,
    "San Salvador": 316090,
    "Montevideo": 1381000,
    "Asunción": 521559,
    "San José": 340000,
    "Tegucigalpa": 1170000,
    "Managua": 1077028
}

resultado = ciudades_grandes(ciudades)

print("\n\nCiudades con más de 100,000 habitantes:\n")
for i, (ciudad, poblacion) in enumerate(resultado, start=1):
    print(f"{i}. {ciudad}: {poblacion} habitantes")
