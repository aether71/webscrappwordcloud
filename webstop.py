#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs 
import re 
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os
import requests   
from nltk.corpus import stopwords


# In[2]:


macbook_reviews=[]

mac=[]  
url="https://www.flipkart.com/apple-macbook-air-core-i5-5th-gen-8-gb-128-gb-ssd-mac-os-sierra-mqd32hn-a-a1466/product-reviews/itmevcpqqhf6azn3?pid=COMEVCPQBXBDFJ8C&page="
response = requests.get(url)
soup = bs(response.content,"html.parser") 
reviews = soup.findAll("div",class_="qwjRop")
for i in range(len(reviews)):
    mac.append(reviews[i].text)  
macbook_reviews=macbook_reviews+mac 

with open("macbo.txt","w",encoding='utf8') as output:
    output.write(str(macbook_reviews))


# In[3]:


mac_rev_string = " ".join(macbook_reviews) 

mac_rev_string = re.sub("[^A-Za-z" "]+"," ",mac_rev_string).lower()

mac_reviews_words = mac_rev_string.split(" ")


# In[5]:


stopworrd=stopwords.words('english')


# In[6]:


mac_reviews_words = [w for w in mac_reviews_words if not w in stopworrd]
mac_rev_string = " ".join(mac_reviews_words)

wordcloud_mac = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(mac_rev_string)
plt.imshow(wordcloud_mac)


# In[8]:


soup


# In[9]:


reviews


# In[ ]:


for w in mac_reviews_words:
    if not w in stopworrd:
        mac_reviewswords.append(w)

