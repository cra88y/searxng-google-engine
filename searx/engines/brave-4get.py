from fourget_hijacker_client import FourgetHijackerClient
categories = ['general']; paging = True
def request(query, params):
    params['results'] = FourgetHijackerClient().fetch('brave', {'s': query})
    params['url'] = 'http://localhost/brave'
    return params
def response(params):
    return FourgetHijackerClient.normalize_results(params.get('results'))