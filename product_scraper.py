import csv
import requests

input_query = 'airpods'

def remove_duplicates(your_list:list):
    new_list = []
    for member in your_list:
        if member not in new_list:
            new_list.append(member)
    return new_list

full_data = []
count = 0
last_product = []
while True:
    ssize = 48
    ffrom = 0+(count*48)
    url = f"https://search.basalam.com/ai-engine/api/v2.0/product/search?productAds=true&adsImpressionDisable=false&q={input_query}&literal=false&from={ffrom}&size={ssize}&facets=namedTags,categories,prices,essences,provinces&filters.hasDiscount=false&filters.isReady=false&filters.isExists=true&filters.hasDelivery=false&filters.vendorScore=false&filters.hasVideo=false&filters.queryNamedTags=false"
    response = requests.get(url)
    res_json = response.json()
    products = res_json['products']
    for product in products:
        if product['status']['id'] == 2976:
            full_data.append([product['name'],product['price'],f'https://basalam.com/{product["vendor"]["identifier"]}/product/{product["id"]}'])

    print(len(full_data))
    if full_data[-1] == last_product:
        break
    else:
        last_product = full_data[-1]
    count+=1

print(len(full_data))
new_full_data = remove_duplicates(full_data)
print(len(new_full_data))
with open(f"{input_query}.csv" , "w+" , encoding="UTF-8" , newline="") as file:
	writer = csv.writer(file)
	writer.writerow(["title" , "price", "url"])
	writer.writerows(new_full_data)
