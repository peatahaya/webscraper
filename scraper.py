from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://it.pracuj.pl/praca?et=1%2C17%2C4&ws=1%2C2&wm=full-office%2Chybrid%2Chome-office&its=backend%2Cfullstack%2Cfrontend&itth=33%2C34%2C36%2C37%2C76%2C73%2C42').text
soup = BeautifulSoup(html_text, 'lxml')

# tiles_ojyuczp core_n194fgoq

# <h5 class="tiles_r1rl4c7t size-caption core_t1rst47b"
# data-test="text-region">Kraków, Podgórze</h5>

# <p class="tiles_b10050bf core_pk4iags size-caption core_t1rst47b"
# data-test="text-added">Opublikowana: 10 lutego 2024</p>

companies_name_roles = soup.find_all('a', class_ = 'tiles_ojyuczp core_n194fgoq')
cities = soup.find('h5', class_='tiles_r1rl4c7t size-caption core_t1rst47b').text
for company_name_role in companies_name_roles:
    print(company_name_role.text)

