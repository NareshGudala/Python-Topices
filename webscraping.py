"""
WEBSCRAPING

--> it ia computer software technique of extracting information from website.
--> It is transfromation of unstructure data into structure data

import section

cmd:
==> pip install requests
==> pip insatll pandas
==> pip install bs4
==> pip list ( showing the pip installed lists )python

"""
import requests
import pandas
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/tyy/4io/~cs-k0hb29i4y2/pr?sid=tyy%2C4io&collection-tab-name=iphone+15&pageCriteria=default&param=27989&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJKdXN0IOKCuTY0LDk5OSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sInRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbImlQaG9uZSAxNSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PQkdUQUdQVEIzVlMyNFciLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19fX19")
# print(response)

soup=BeautifulSoup(response.content,'html.parser')

# print(soup)

names=soup.find_all('div',class_='KzDlHZ')
name=[]
for i in name[0:12]:
    d=i.get_text()
    name.append(d)
# print(name)    

prices = soup.find_all('div',class_="Nx9bqj _4b5DiR")
price=[]
for i in prices[0:12]:
    d=i.get_text()
    price.append(d)
# print(price)
    

ratings = soup.find_all('div',class_="XQDdHH")
rate=[]
for i in ratings[0:12]:
    d=i.get_text()
    rate.append(d)
# print(rate)
    
reviews=soup.find_all('span',class_="hG7V+4")  
review=[]
for i in reviews[0:12]:
    d=i.get_text()
    review.append(d)
# print(review)

features=soup.find_all('li',class_="_6NESgJ")  
feature=[]
for i in features[0:12]:
    d=i.get_text()
    feature.append(d)
# print(feature)

links=soup.find_all('a',class_="_1fQZEK")
link=[]
for i in links[0:12]:
    d="https://www.flipkart.com"+i['href']
    link.append(d)
# print(link)

images=soup.find_all('image',class_="_1fQZEK")
image=[]
for i in images[0:12]:
    d=i.div.image['src']
    image.append(d)
# print(image)

# print(df)
data={'Names':name,
      "prices":price,
      "ratings":rate,
      "features":feature,
      "reviews":review,
      }

# print(data)
df = pandas.DataFrame(data)
# print(df)
df.to_csv("mobiles_data.csv")

