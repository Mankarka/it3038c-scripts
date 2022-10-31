from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = ('https://www.booking.com/searchresults.en-us.html?ss=Cincinnati%2C+Ohio%2C+United+States&label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4AQfIAQzYAQHoAQH4AQKIAgGoAgO4AvTIm_IFwAIB&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=20097593&dest_type=city&ac_position=1&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=97bd9db292ce0232&ac_meta=GhA5N2JkOWRiMjkyY2UwMjMyIAEoATICZW46A2NpbkAASgBQAA%3D%3D&checkin=2022-10-30&checkout=2022-10-31&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure')
response=requests.get(url,headers=headers)

soup=BeautifulSoup(response.content,'lxml')

for item in soup.select('.sr_property_block'):
	try:
		print('----------------------------------------')
		print(item.select('.sr-hotel__name')[0].get_text().strip())
		print(item.select('.hotel_name_link')[0]['href'])
		print(item.select('.bui-review-score__badge')[0].get_text().strip())
		print(item.select('.bui-review-score__text')[0].get_text().strip())
		print(item.select('.bui-review-score__title')[0].get_text().strip())
		print(item.select('.hotel_image')[0]['data-highres'])
		print(item.select('.bui-price-display__value')[0].get_text().strip())

		print('----------------------------------------')
	except Exception as e:

		print('')
