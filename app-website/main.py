import json, requests, simplejson
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    uri = "http://localhost:8081"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    '''
    ['event_id', 'event_timestamp', 'event_type', 'page_url',
       'page_url_path', 'referer_url', 'referer_url_scheme',
       'referer_url_port', 'referer_medium', 'utm_medium', 'utm_source',
       'utm_content', 'utm_campaign', 'click_id', 'geo_latitude',
       'geo_longitude', 'geo_country', 'geo_timezone', 'geo_region_name',
       'ip_address', 'browser_name', 'browser_user_agent', 'browser_language',
       'os', 'os_name', 'os_timezone', 'device_type', 'device_is_mobile',
       'user_custom_id', 'user_domain_id']
    '''

    # displayName = data['items'][0]['display_name']# <-- The display name
    # reputation = data['items'][0]['reputation']# <-- The reputation

    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)