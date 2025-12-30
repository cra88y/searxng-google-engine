from fourget_hijacker_client import FourgetHijackerClient  
  
categories = ['general']  
paging = True  
  
def request(query, params):  
    params['url'] = 'http://4get-hijacked:80/harness.php'  
    params['method'] = 'POST'  
    params['json'] = {  
        "engine": "duckduckgo",   
        "params": {"s": query}  
    }  
    return params  
  
def response(resp):  
    try:  
        response_data = resp.json()  
        return FourgetHijackerClient.normalize_results(response_data)  
    except Exception as e:  
        return []