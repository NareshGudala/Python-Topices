''''
import requests
from bs4 import BeautifulSoup
import csv

# url = "https://www.flipkart.com/tyy/4io/~cs-k0hb29i4y2/pr?sid=tyy%2C4io&collection-tab-name=iphone+15&pageCriteria=default&param=27989&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJKdXN0IOKCuTY0LDk5OSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sInRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbImlQaG9uZSAxNSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PQkdUQUdQVEIzVlMyNFciLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19fX19"
url = "https://www.bikewale.com/royalenfield-bikes/hunter-350/"
page=requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
'''

'''
# images

image1=[]
image=soup.findAll('div',class_="o-bfyaNx o-brXWGL o-bqHweY o-dgboEW  PhYMAu")
# print(image)

for i in image:
    j=i.img['src']
    image1.append(j)
    # print(j)
print(image1)

'''




'''
links = []
link = soup.findAll('div',class_='bikeDescWrapper')
for i in link:
    j = i.a['href']
    links.append(j)
print(links)    

'''


# df = pandas.DataFrame()
# data={'Names': name.pandas.Series(),
#       "Prices": price,
#       "Rating": rate,
#       'Features': features,
#       'Reviews': review,
#       "Images": image,
#       "Links": link
#       }

# df = pandas.DataFrame(data)
# print(df)


# import requests
# from bs4 import BeautifulSoup
# import csv

# url = "https://www.bikewale.com/royalenfield-bikes/hunter-350/"
# page = requests.get(url)

# print(page.status_code)
# # print(page.content)

# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.text) 


# # ->images
# image = soup.findAll('div',class_="o-bfyaNx o-brXWGL o-bqHweY o-dgboEW  PhYMAu")
# print(image)






import requests
from bs4 import BeautifulSoup

# Send a GET request to the Amazon product page
url = "https://www.amazon.com/dp/B076MX9VG9"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all customer review elements on the page
reviews = soup.find_all('div', {'class': 'a-section review'})

# Extract the review text and rating from each element
for review in reviews:
    text = review.find('span', {'class': 'a-size-base review-text'}).text.strip()
    rating = review.find('span', {'class': 'a-icon-alt'}).text.strip()
    print(f"Review: {text}, Rating: {rating}")