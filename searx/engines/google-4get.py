from fourget_hijacker_client import FourgetHijackerClient

categories = ['general']
paging = True

def request(query, params):
    client = FourgetHijackerClient()
    fourget_params = {
        's': query,
        'country': params.get('searxng_locale', 'US').split('-')[-1].lower(),
        'lang': params.get('searxng_locale', 'en').split('-')[0],
    }
    # Perform the hijack call to the sidecar
    params['results'] = client.fetch('google', fourget_params)
    
    # Dummy URL to satisfy SearXNG core
    params['url'] = 'http://localhost/proxied-to-4get'
    return params

def response(params):
    response_data = params.get('results')
    client = FourgetHijackerClient()
    return client.normalize_results(response_data)