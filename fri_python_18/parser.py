import requests
import bs4
import webbrowser

#webbrowser.open('https://hi-news.ru/', new=2)

def link_random_cats():
	'''Парсит ссылки c гифками котов'''
	# Подключается к сайту 
	res = requests.get('https://tenor.com/search/fat-cat-gifs')
	# Проверяет подключение 404 - ошибка, 200 - ОК
	res.raise_for_status()
	# Иcследуем наш сайт
	soup = bs4.BeautifulSoup(res.text)

	# Находим теги с ссылками и сохраняем ссылки в список
    gifElem = soup.select('img[src]')
    gif_list = []
    
    # Заполняет список ссылками
    for i in gifElem:
        gifUrl = i.get('src')
        gif_list.append(gifUrl)

	return gif_list


print(link_random_cats())
    
