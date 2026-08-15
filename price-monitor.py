import requests
from bs4 import BeautifulSoup
import re
from plyer import notification
import time

# الجزء 1: جلب بيانات الصفحة
def get_page_html(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        return response.text
    raise Exception(f"فشل جلب الصفحة، رمز الاستجابة: {response.status_code}")

# الجزء 2: استخراج السعر والعنوان
def parse_product_info(html_content: str) -> dict:
    soup = BeautifulSoup(html_content, "html.parser")
    title_element = soup.find("h1") or soup.find("span", {"id": "productTitle"})
    price_element = soup.find("span", {"class": "price"}) or soup.find("span", {"class": "a-price-whole"})
    
    title = title_element.get_text(strip=True) if title_element else "منتج غير معروف"
    price = 0.0
    
    if price_element:
        raw_price = price_element.get_text(strip=True)
        clean_price = re.sub(r"[^\d.]", "", raw_price)
        price = float(clean_price) if clean_price else 0.0
        
    return {"title": title, "price": price}

# الجزء 3: منطق المقارنة والتنبيه
def is_price_good(current_price: float, target_price: float) -> bool:
    return 0 < current_price <= target_price

def send_desktop_alert(title: str, price: float):
    notification.notify(
        title="تنبيه هبوط السعر!",
        message=f"وصل سعر {title[:25]}... إلى ${price}",
        app_name="Price Monitor",
        timeout=10
    )

# الجزء 4: المحرك الرئيسي
def main():
    target_url = "https://httpbin.org/html"
    target_price = 150.0
    
    print("جاري فحص السعر...")
    try:
        html = get_page_html(target_url)
        product = parse_product_info(html)
        print(f"اسم المنتج: {product['title']}")
        print(f"السعر الحالي: ${product['price']}")
        
        if is_price_good(product['price'], target_price):
            send_desktop_alert(product['title'], product['price'])
            print("تم إرسال التنبيه بنجاح!")
        else:
            print("السعر أعلى من السعر المستهدف.")
    except Exception as e:
        print(f"حدث خطأ أثناء التشغيل: {e}")

if __name__ == "__main__":
    main()
