import requests
import csv
import sys
import time


class RestCountriesParser:
    def __init__(self, input_file="countries.txt", output_file="countries_data.csv"):
        self.input_file = input_file
        self.output_file = output_file
        self.base_url = "https://restcountries.com/v3.1/"

    def get_country_info(self, country_name):
        """Получение информации о стране через REST API"""
        try:
            # Используем точный поиск по названию
            response = requests.get(f"{self.base_url}name/{country_name}?fullText=true")

            # Если точный поиск не дал результатов, пробуем обычный
            if response.status_code == 404:
                response = requests.get(f"{self.base_url}name/{country_name}")

            response.raise_for_status()

            data = response.json()

            # Берем первую страну из результатов
            country_data = data[0]

            capital = country_data.get('capital', ['N/A'])[0] if country_data.get('capital') else 'N/A'
            area = str(country_data.get('area', 'N/A'))
            population = str(country_data.get('population', 'N/A'))

            return {
                "capital": capital,
                "area": area,
                "population": population
            }

        except Exception as e:
            print(f"Ошибка при получении данных для {country_name}: {e}")
            return {"capital": "N/A", "area": "N/A", "population": "N/A"}

    def process_countries(self):
        """Основной метод для обработки всех стран"""
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                countries = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Файл {self.input_file} не найден!")
            return

        with open(self.output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['country', 'capital', 'area', 'population']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for i, country in enumerate(countries, 1):
                print(f"Обрабатывается {country} ({i}/{len(countries)})...")

                country_info = self.get_country_info(country)

                writer.writerow({
                    'country': country,
                    'capital': country_info['capital'],
                    'area': country_info['area'],
                    'population': country_info['population']
                })

                print(f"  Столица: {country_info['capital']}")
                print(f"  Площадь: {country_info['area']} км²")
                print(f"  Население: {country_info['population']}")

                if i < len(countries):
                    time.sleep(0.5)  # Меньшая пауза для API

        print(f"\nДанные сохранены в {self.output_file}")


def main():
    input_file = "countries.txt"
    output_file = "countries_data.csv"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    parser = RestCountriesParser(input_file, output_file)
    parser.process_countries()


if __name__ == "__main__":
    main()