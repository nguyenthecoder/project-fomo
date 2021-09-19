from newsplease import NewsPlease

url1 = 'https://www.cnn.com/2021/09/18/weather/extreme-urban-heat-environmental-racism-climate/index.html'

article = NewsPlease.from_url(url1)

print(article.authors)
print(article.maintext)





