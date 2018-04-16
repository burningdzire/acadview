import requests

response = requests.get('').json()
APP_ACCESS_TOKEN = response['access_token']
BASE_URL='https://api.instagram.com/v1/'

def self_info():
	request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
	print('GET request url : %s' % (request_url))
	user_info = requests.get(request_url).json()
	
	if user_info['meta']['code'] == 200:
		print(user_info['data']['id'])
		print(user_info['data']['username'])
	else:
		print('Status code other than 200 received!')

self_info()
