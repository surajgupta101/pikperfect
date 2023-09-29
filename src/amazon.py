

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import threading
import concurrent.futures
#from dataframeout import *
# Function to extract Product Title
def get_title(soup):
    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'})
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

# Function to extract Product Price
def get_price(soup):

    try:
        price = soup.find("span", attrs={'class':"a-price-whole"}).string.strip()
    
    
    except AttributeError:
        print("L")
        try:
            # If there is some deal price
            price = soup.find("span", attrs={'class':"a-offscreen"}).string.strip()
            
        except:
            price = ""

    return price

'''def get_image(soup):

    try:
        image = soup.find("span", attrs={'class':"imgTagWrapper"}).string.strip()
    
    
    except AttributeError:
            image = ""
    print(image)
    return image'''


# Function to extract Product Rating
def get_rating(soup):

    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = "" 

    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count = "" 

    return review_count

#url shorten
def shorten_url(url):
    '''try:
        # TinyURL API endpoint
        api_url = "https://tinyurl.com/api-create.php"

        # POST request to create a short URL
        response = requests.post(api_url, data={"url": url})

        # Check if the request was successful
        if response.status_code == 200:
            return response.text
    except:
        pass'''

    # Return the original URL if something goes wrong
    return url

# Function to extract product details from a link
def extract_product_details(link, d, HEADERS):
    long_url = "https://www.amazon.in" + link
    short_url = shorten_url(long_url)
    new_webpage = requests.get("https://www.amazon.in" + link, headers=HEADERS)

    new_soup = BeautifulSoup(new_webpage.content, "html.parser")

    # Function calls to display all necessary product information
    get_image(new_soup)
    d['title'].append(get_title(new_soup))
    d['price'].append(get_price(new_soup))
    d['rating'].append(get_rating(new_soup))
    d['reviews'].append(get_review_count(new_soup))
    d['link'].append(short_url)

# Function to extract product details from multiple links using multithreading
def extract_product_details_multithreaded(links_list, HEADERS):
    d = {"title":[], "price":[], "rating":[], "reviews":[],"link":[]}
    threads = []

    for link in links_list:
        t = threading.Thread(target=extract_product_details, args=(link, d, HEADERS))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    return d

def flipkart_get(product_name):
  


  # Flipkart URL
   
  flipkart_url = "https://www.flipkart.com/search?q=" + product_name.replace(' ', '%20')

  # Make request to Flipkart URL
    
  flipkart_response = requests.get(flipkart_url)
  flipkart_soup = BeautifulSoup(flipkart_response.content, 'html.parser')

  # Get product details
  try:
    


    product_name = flipkart_soup.find('div', {'class': '_4rR01T'}).text
    product_rating = flipkart_soup.find('div', {'class': '_3LWZlK'}).text
    product_price = flipkart_soup.find('div', {'class': '_30jeq3 _1_WHN1'}).text.replace('₹', '').replace(',', '').strip()
    product_num_reviews = flipkart_soup.find('span', {'class': '_2_R_DZ'}).text.split()[0]
    product_url = flipkart_soup.find('a', {'class': '_1fQZEK'}).get('href')
    product_url = 'https://www.flipkart.com' + product_url
  except (AttributeError, TypeError):
    print("Product details not found!")
    return {"" :[""]}

  d1 = {"title":[product_name], "price":[product_price], "rating":[product_rating], "reviews":[product_num_reviews],"link":[product_url]}
  return d1 
  # Print product details
  '''print("Product Name:", product_name)
  print("Rating:", product_rating)
  print("Price (in INR):", product_price)
  print("Number of Reviews:", product_num_reviews)
  print("URL:", product_url)'''




def listofproduct(nameofproduct):

    # Add a user agent to the headers
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

    
    fname = nameofproduct
    pname = fname.replace(' ', '+')
    # The webpage URL
    URL = "https://www.amazon.in/s?k=" + pname

    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Fetch links as List of Tag Objects

    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})
    
    # Store the links
    links_list = []
    choice = [] #title mapped to reviews
    # Loop for extracting links from Tag Objects
    ind1=1
    products =[]
    for link in links:
            dict12 = {}
            sstrg = link.get('href')
            sstrg2 = link.get('href')
            
            sstrg1 = sstrg.split("/")
            
            if sstrg1[1]!="sspa":
              print(str(ind1) + " ", end="")
              ind1 +=1
              long1 = "https://www.amazon.in" + sstrg2
              dict12["image_link"] = long1
              dict12["name"] = sstrg1[1].replace("-"," ")
              dict12["price"] = get_price(soup)
              print(dict12["name"])
              products.append(dict12)
              choice.append(sstrg)
            #links_list.append(link.get('href'))
            #web1 = requests.get("https://www.amazon.in" + link.get('href'), headers=HEADERS)

            #firt_soup = BeautifulSoup(web1.content, "html.parser")
            #choice[get_title(firt_soup)]= get_rating(firt_soup)
    return products
    #choiceselected(products[0]['image_link'])       
    #print(choice)  




#if __name__ == '__main__':
def choiceselected(chosenlink):
    # Add a user agent to the headers
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

    
    '''fname = input('enter the product name: ')
    pname = fname.replace(' ', '+')
    # The webpage URL
    URL = "https://www.amazon.in/s?k=" + pname

    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Fetch links as List of Tag Objects

    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})
    
    # Store the links
    links_list = []
    choice = [] #title mapped to reviews
    # Loop for extracting links from Tag Objects
    ind1=1
    products =[]
    for link in links:
            dict12 = {}
            sstrg = link.get('href')
            sstrg2 = link.get('href')
            
            sstrg1 = sstrg.split("/")
            
            if sstrg1[1]!="sspa":
              print(str(ind1) + " ", end="")
              ind1 +=1
              long1 = "https://www.amazon.in" + sstrg2
              dict12["image_link"] = long1
              dict12["name"] = sstrg1[1].replace("-"," ")
              print(dict12["name"])
              products.append(dict12)
              choice.append(sstrg)
            #links_list.append(link.get('href'))
            #web1 = requests.get("https://www.amazon.in" + link.get('href'), headers=HEADERS)

            #firt_soup = BeautifulSoup(web1.content, "html.parser")
            #choice[get_title(firt_soup)]= get_rating(firt_soup)
    print(products)       
    #print(choice)  
    val = int(input("enter your choice"+" "))''' 
    #links_list.append(choice[val-1])
    links_list = []
    links_list.append(chosenlink[21:])

    d = {"title":[], "price":[], "rating":[], "reviews":[],"link":[]}
    
    # Threadpool for making parallel requests
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Loop for extracting product details from each link 
        results = []
        for link in links_list:
            long_url = "https://www.amazon.in" + link
            
            # Submit a request to shorten the URL in a separate thread
            short_url = executor.submit(shorten_url, long_url)
            new_webpage = requests.get("https://www.amazon.in" + link, headers=HEADERS)

            new_soup = BeautifulSoup(new_webpage.content, "html.parser")

            # Function calls to display all necessary product information
          
            d['title'].append(get_title(new_soup))
            d['price'].append(get_price(new_soup))
            d['rating'].append(get_rating(new_soup))
            d['reviews'].append(get_review_count(new_soup))
            # Retrieve the shortened URL from the thread when it's done
            d['link'].append(short_url.result())

    print(" ")
    amazon_df = pd.DataFrame.from_dict(d)
    amazon_df['title'].replace('', np.nan, inplace=True)
    amazon_df = amazon_df.dropna(subset=['title'])
    amazon_df.to_csv("amazon_data.csv", header=True, index=False)
    print(amazon_df.to_string(index=False,justify='left'))
    links_list[0] = links_list[0].split("/")
    links_list[0][1] = links_list[0][1].replace("-"," ")
    print(" ")
    d1 = flipkart_get(str(links_list[0][1]))
    #print(d1)
    flip_df = pd.DataFrame.from_dict(d1)
    flip_df['title'].replace('', np.nan, inplace=True)
    flip_df = flip_df.dropna(subset=['title'])
    flip_df.to_csv("flip_data.csv", header=True, index=False)
    print(flip_df.to_string(index=False,justify='left'))
    #wind2 = MainWindow2()
    #wind2.show()