import requests
from bs4 import BeautifulSoup
import time
import random
import json


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

def wine_url():
    wine_urls = []
    count = 1
    urls_count = 177
    for url in range(1, 3):
        page = requests.get(url=f"https://simplewine.ru/catalog/vino/page{url}", headers=headers)
        soup = BeautifulSoup(page.text, "lxml")
        items_divs = soup.find_all("div", class_="product-snippet__right")
        for item in items_divs:
            item_url = item.find("a").get("href")
            wine_urls.append('https://simplewine.ru' + item_url)

        print(f"[+] Процесс: {count}/{urls_count}")

        count += 1

        with open(r"\wine_parser\url_wine.txt", "w") as file:
            for element in wine_urls:
                file.write(element)
                file.write("\n")

def get_data_wine():
    with open(r"\wine_parser\url_wine.txt") as file:
        urls_list = [url.strip() for url in file.readlines()]

    result_list = []
    urls_count = len(urls_list)
    count = 1
    for url in urls_list:
        try:
            response = requests.get(url=url, headers=headers)
        except:
            pass
        soup = BeautifulSoup(response.text, "lxml")

        try:
            item_name = soup.find("h1", class_="product-page__header").text.strip()
        except Exception as _ex:
            item_name = None
        try:
            item_price = soup.find("div", class_="product-buy__price-wrapper").text.strip().replace("₽", "")
        except Exception as _ex:
            item_price = None
        try:
            item_country = soup.find("dl", class_="product-brief").text
            try:
                item_country = item_country.replace("\nС", 'С')
            except:
                pass
            try:
                item_country = item_country.replace("\nВ", "В")
            except:
                pass
            try:
                item_country = item_country.replace("\nП", 'П')
            except:
                pass
            try:
                item_country = item_country.replace("\nК", "К")
            except:
                pass
            try:
                item_country = item_country.replace("\nО", "О")
            except:
                pass
            item_country = item_country.replace("\n\n", "").split("\n")

            prefix = "Страна, регион:"

            for i in item_country:
                if i.startswith(prefix):
                    item_country = i.removeprefix(prefix)
                    break
            else:
                item_country = None
        except Exception as _ex:
            item_country = None
        try:
            item_grape = soup.find("dl", class_="product-brief").text
            try:
                item_grape = item_grape.replace("\nС", 'С')
            except:
                pass
            try:
                item_grape = item_grape.replace("\nВ", "В")
            except:
                pass
            try:
                item_grape = item_grape.replace("\nП", 'П')
            except:
                pass
            try:
                item_grape = item_grape.replace("\nК", "К")
            except:
                pass
            try:
                item_grape = item_grape.replace("\nО", "О")
            except:
                pass
            item_grape = item_grape.replace("\n\n", "").split("\n")

            prefix = "Виноград:"

            for i in item_grape:
                if i.startswith(prefix):
                    item_grape = i.removeprefix(prefix)
                    break
            else:
                item_grape = None
        except Exception as _ex:
            item_grape = None
        try:
            item_suggar = soup.find("dl", class_="product-brief").text
            try:
                item_suggar = item_suggar.replace("\nС", 'С')
            except:
                pass
            try:
                item_suggar = item_suggar.replace("\nВ", "В")
            except:
                pass
            try:
                item_suggar = item_suggar.replace("\nП", 'П')
            except:
                pass
            try:
                item_suggar = item_suggar.replace("\nК", "К")
            except:
                pass
            try:
                item_suggar = item_suggar.replace("\nО", "О")
            except:
                pass
            item_suggar = item_suggar.replace("\n\n", "").split("\n")

            prefix = "Сахар:"

            for i in item_suggar:
                if i.startswith(prefix):
                    item_suggar = i.removeprefix(prefix)
                    break
            else:
                item_suggar = None
        except Exception as _ex:
            item_suggar = None
        try:
            item_strength = soup.find("dl", class_="product-brief").text
            try:
                item_strength = item_strength.replace("\nС", 'С')
            except:
                pass
            try:
                item_strength = item_strength.replace("\nВ", "В")
            except:
                pass
            try:
                item_strength = item_strength.replace("\nП", 'П')
            except:
                pass
            try:
                item_strength = item_strength.replace("\nК", "К")
            except:
                pass
            try:
                item_strength = item_strength.replace("\nО", "О")
            except:
                pass
            item_strength = item_strength.replace("\n\n", "").split("\n")

            prefix = "Крепость:"

            for i in item_strength:
                if i.startswith(prefix):
                    item_strength = i.removeprefix(prefix)
                    break
            else:
                item_strength = None
        except Exception as _ex:
            item_strength = None
        try:
            item_producer = soup.find("dl", class_="product-brief").text
            try:
                item_producer = item_producer.replace("\nС", 'С')
            except:
                pass
            try:
                item_producer = item_producer.replace("\nВ", "В")
            except:
                pass
            try:
                item_producer = item_producer.replace("\nП", 'П')
            except:
                pass
            try:
                item_producer = item_producer.replace("\nК", "К")
            except:
                pass
            try:
                item_producer = item_producer.replace("\nО", "О")
            except:
                pass
            item_producer = item_producer.replace("\n\n", "").split("\n")

            prefix = "Производитель:"

            for i in item_producer:
                if i.startswith(prefix):
                    item_producer = i.removeprefix(prefix)
                    break
            else:
                item_producer = None
        except Exception as _ex:
            item_producer = None
        try:
            item_year = (
                soup.find("dl", class_="characteristics-params__list")
                .text
                .replace("                ", "")
                .replace("            ", "")
                .replace("\n\n\n", "")
                .replace("\n\n", "")
                .split("\n")
            )

            prefix = "Год:"

            for i in item_year:
                if i.startswith(prefix):
                    item_year = i.removeprefix(prefix)
                    break
            else:
                item_year = None
        except Exception as _ex:
            item_year = None
        try:
            item_decantation = (
                soup.find("dl", class_="characteristics-params__list")
                .text
                .replace("                ", "")
                .replace("            ", "")
                .replace("\n\n\n", "")
                .replace("\n\n", "")
                .split("\n")
            )

            prefix = "Декантация:"

            for i in item_decantation:
                if i.startswith(prefix):
                    item_decantation = i.removeprefix(prefix)
                    break
            else:
                item_decantation = None
        except Exception as _ex:
            item_decantation = None
        try:
            item_temperature = soup.find("dd", class_="serving__temperature-value").text.strip()
        except Exception as _ex:
            item_temperature = None
        try:
            item_rating_sw = soup.find("p", class_="rating-stars__value").text.strip()
        except Exception as _ex:
            item_rating_sw = None
        try:
            item_rating_vivino = soup.find("ul", class_="product-ratings__list").text.strip().replace(" ", "").split('\n\n\n\n\n')

            for i in item_rating_vivino:
                if i.startswith("VIVINO"):
                    key = item_rating_vivino.index(i)
                    item_rating_vivino = item_rating_vivino[key][6:]
                    break
            else:
                item_rating_vivino = None
        except Exception as _ex:
            item_rating_vivino = None
        try:
            item_rating_js = soup.find("ul", class_="product-ratings__list").text.strip().replace(" ", "").split('\n\n\n\n\n')

            for i in item_rating_js:
                if i.startswith("JS"):
                    key = item_rating_js.index(i)
                    item_rating_js = item_rating_js[key][2:]
                    break
            else:
                item_rating_js = None
        except Exception as _ex:
            item_rating_js = None
        try:
            item_rating_ws = soup.find("ul", class_="product-ratings__list").text.strip().replace(" ", "").split('\n\n\n\n\n')

            for i in item_rating_ws:
                if i.startswith("WS"):
                    key = item_rating_ws.index(i)
                    item_rating_ws = item_rating_ws[key][2:]
                    break
            else:
                item_rating_ws = None
        except Exception as _ex:
            item_rating_ws = None
        try:
            item_rating_rp = soup.find("ul", class_="product-ratings__list").text.strip().replace(" ", "").split('\n\n\n\n\n')

            for i in item_rating_rp:
                if i.startswith("RP"):
                    key = item_rating_rp.index(i)
                    item_rating_rp = item_rating_rp[key][2:]
                    break
            else:
                item_rating_rp = None
        except Exception as _ex:
            item_rating_rp = None
        try:
            item_description = soup.find("ul", class_= "characteristics-description__list").text.strip().split("\n\n")[4]
        except Exception as _ex:
            item_description = None

        result_list.append(
            {
                "name": item_name,
                "country": item_country,
                "year": item_year,
                "grape": item_grape,
                "suggar": item_suggar,
                "strength": item_strength,
                "producer": item_producer,
                "temperature_suplly": item_temperature,
                "decantation": item_decantation,
                "price": item_price,
                "simplewine_rating": item_rating_sw,
                "vivino_rating": item_rating_vivino,
                "ws_rating": item_rating_ws,
                "rp_rating": item_rating_rp,
                "js_rating": item_rating_js,
                "description": item_description

            }
        )

        time.sleep(random.randrange(2, 5))

        if count % 10 == 0:
            time.sleep(random.randrange(5, 9))

        print(f"[+] Процесс: {count}/{urls_count}")

        count += 1

    with open(r"\wine_parser\result.json", "w") as file:
        json.dump(result_list, file, indent=4, ensure_ascii=False)

    return "[INFO] Данные успешно собраны!"

def main():
    # сбор ссылок на вино
    #wine_url()
    # сбор данных
    #get_data_wine()

if __name__ == "__main__":
    main()