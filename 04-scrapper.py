import requests
from bs4 import BeautifulSoup

# URL de la página web
sitio = "https://stackoverflow.com"
url = "/questions"
page = 0

# while url:
while page < 3:
    res = requests.get(sitio + url, verify=False)
    text = res.text

    # Parsear el contenido HTML
    soup = BeautifulSoup(text, 'html.parser')
    # Seleccionar todas las preguntas
    questions = soup.select('.s-post-summary')

    for question in questions:
        title = question.select_one(".s-link").get_text()
        user = question.select_one(".s-user-card--link").get_text()
        # vote_count = question.select_one(".s-post-summary--stats-item-number").get_text()
        print(f"{user} - Titulo: \n{title.strip()}")

    next_page = None
    pagination = soup.select(".s-pagination--item")

    for pag in pagination:
        if pag.get_text().strip() == "Next":
            next_page = pag.get("href")
            break

    if next_page:
        url = next_page
        print(f"Pasando a la siguiente página: {url}")
    else:
        print("No hay más páginas disponibles.")
        break
    print("=============================================")
    page += 1
