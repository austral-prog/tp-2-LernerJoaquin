def earth():
    country1 = "Bangladesh"
    country2 = "Barbados"

    # Comparaciones lexicográficas
    first_comparison = country1 < country2
    second_comparison = country2 < country1

    # Resultados
    print(f"The result of {country1} comes first in the dictionary than {country2} is {first_comparison}.")
    print(f"The result of {country2} comes first in the dictionary than {country1} is {second_comparison}.")
