import requests

def get_posts():
    # Define the API endpoint URL
    # url = 'https://jsonplaceholder.typicode.com/posts'
    # url = 'https://api.nettoolkit.com/v1/account/test-api-keys'
    url = 'http://127.0.0.1:5000/examples'
    # headers = {'Accept': 'application/json'}
    # auth = HTTPBasicAuth('apikey', 'test_pIObiKV98uZdLLdenY7pwjTdPmjkzanUXn7HHd3G')

    try:
        # Make a GET request to the API endpoint using requests.get()
        # response = requests.get(url,headers=headers,auth=auth)
        response = requests.get(url)
        # response = requests.post(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None

    except requests.exceptions.RequestException as e:
      
        # Handle any network-related errors or exceptions
        print('Error:', e)
        return "Some error ocurred"

def main():
    posts = get_posts()

    if posts:
        # print('First Post Title:', posts[0]['title'])
        # print('First Post Body:', posts[0]['body'])
        # print('Complete API response: ', posts['results'][0]['created'])
        print('Complete API response: ', posts)
    else:
        print('Failed to fetch posts from API.')

if __name__ == '__main__':
    main()