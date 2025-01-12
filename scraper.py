import requests, time, csv, random
from bs4 import BeautifulSoup

def get_soup(url):

    try:
        req = requests.get(url)
        req.raise_for_status()
        print("\nStatus: ", req)
        if req:
            soup = BeautifulSoup(req.text, "html.parser")
            return soup
        else: None
    except requests.HTTPError as err:
        print("Error: ", err)
        return None
    
with open("output.csv", "w", newline="", encoding="utf-8") as file:
    file = csv.writer(file)
    file.writerow(["Book Title", "Img URL", "Price", "Rating", "Availability", "Product Page URL"])

    url = "https://books.toscrape.com/catalogue/page-1.html"
    img_base_url = "https://books.toscrape.com/"
    page_base_url = "https://books.toscrape.com/catalogue/"


    while url:
        soup = get_soup(url)
        conts = soup.find_all(class_="product_pod") if soup else None

        for cont in conts:

            img_cont = cont.find(class_="image_container") if cont else None

            page_url = f"{page_base_url}{img_cont.a.get('href')}" if img_cont.a else "N/A"
            img_url = f"{img_base_url}{img_cont.a.img.get('src')}" if img_cont.a.img else "N/A"

            p_rating = cont.find(class_="star-rating")
            rating = p_rating.get("class")[1] if p_rating else "N/A"

            title = cont.h3.a.get("title").strip() if cont.h3.a else "N/A"

            price = cont.find(class_="price_color").text.strip() if cont.find(class_="price_color") else "N/A"

            availability = cont.find(class_="instock availability").text.strip() if cont.find(class_="instock availability") else "N/A"


            data = f"Book Title: {title} \nImg URL: {img_url} \nPrice: {price} \nRating: {rating} \nAvailability: {availability} \nProduct Page URl: {page_url}"

            print("="*50)
            print(data.center(50))
            print("="*50)

            file.writerow([title, img_url, price, rating, availability, page_url])
        
        next_page = soup.find(class_="next")

        if next_page:
            time.sleep(random.uniform(1, 3))
            url = f"{page_base_url}{next_page.a.get("href")}"
            print("\n\nNext_Page: ", url)
        else:
            url = None




    