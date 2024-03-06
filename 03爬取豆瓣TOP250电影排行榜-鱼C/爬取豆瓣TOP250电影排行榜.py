import requests
from bs4 import BeautifulSoup

def get_movie_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    movie_list = soup.find('ol', class_='grid_view').find_all('li')

    for movie in movie_list:
        name = movie.find('span', class_='title').text
        rating = movie.find('span', class_='rating_num').text
        comment_num = movie.find('div', class_='star').find_all('span')[-1].text[:-3]
        info = movie.find('div', class_='bd').p.text.strip()

        print(f'电影名称：{name}')
        print(f'评分：{rating}')
        print(f'评论数：{comment_num}')
        print(f'电影信息：{info}')
        print('-' * 50)

if __name__ == '__main__':
    base_url = 'https://movie.douban.com/top250?start={}&filter='
    total_pages = 10

    for page in range(total_pages):
        url = base_url.format(page * 25)
        get_movie_info(url)
