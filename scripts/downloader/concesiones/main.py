import json
import time
from datetime import date

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from joblib import Parallel, delayed

requests.urllib3.disable_warnings()
s = requests.Session()
ua = UserAgent()


def get_random_header():
    return {
        'User-Agent': str(ua.random)
    }


def get_csrf(headers):
    page = s.get("https://www.infosubvenciones.es/bdnstrans/GE/es/concesiones", headers=headers,
                 verify=False)
    soup = BeautifulSoup(page.text, 'html.parser')
    csrf = soup.find('input', attrs={'name': '_csrf'})
    return csrf['value']


def post_csrf(csrf, headers, date=""):
    data = {
        "_csrf": csrf,
        "_ministerios": 1,
        "_organos": 1,
        "_cAutonomas": 1,
        "_departamentos": 1,
        "_locales": 1,
        "_localesOculto": 1,
        "beneficiarioFilter": "DNI",
        "beneficiarioNombre": "",
        "beneficiarioDNI": "",
        "beneficiario": "",
        "fecDesde": date,
        "fecHasta": date,
        "tipoBusqPalab": 1,
        "titulo": "",
        "_regiones": 1,
        "_actividadesNACE": 1,
        "_instrumentos": 1
    }
    s.post("https://www.infosubvenciones.es/bdnstrans/GE/es/concesiones", data=data, headers=headers,
           verify=False)


def get_data(headers, page_number):
    requests.urllib3.disable_warnings()
    page = s.get(
        f"https://www.infosubvenciones.es/bdnstrans/busqueda?type=concs&_search=false&nd={int(time.time())}&rows=200&page={page_number}&sidx=8&sord=desc",
        headers=headers, verify=False)
    data = page.json()
    return data


def num_entries(date, headers):
    requests.urllib3.disable_warnings()
    csrf = get_csrf(headers)
    post_csrf(csrf, headers, date)
    initial_data = get_data(headers, 1)
    print(f"{date} tiene {initial_data['records']} entradas en {initial_data['total']} páginas")

    initial_rows = initial_data['rows']
    data = Parallel(n_jobs=5)(delayed(get_data)(headers, i) for i in range(2, initial_data['total'] + 1))
    for d in data:
        initial_rows += d['rows']

    print(len(initial_rows))

    file_name = f"results-{date.replace('/', '-')}.json"
    print(f"Saving to {file_name}")

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(initial_rows, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # num_entries("04/01/2022", get_random_header())

    start_date = date(2022, 1, 1)
    end_date = date(2022, 1, 7)
    dates = [date.fromordinal(i) for i in range(start_date.toordinal(), end_date.toordinal())]
    dates_str = [d.strftime("%d/%m/%Y") for d in dates]

    for d in dates_str:
        num_entries(d, get_random_header())
