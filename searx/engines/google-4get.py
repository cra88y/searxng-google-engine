from fourget_hijacker_client import FourgetHijackerClient
import logging

logger = logging.getLogger(__name__)

categories = ['general']
paging = True

def request(query, params):
    client = FourgetHijackerClient()
    filters = client.get_engine_filters('google')
    params['url'] = 'http://4get-hijacked:80/harness.php'
    params['method'] = 'POST'
    params['json'] = {
        'engine': 'google',
        'params': FourgetHijackerClient.get_4get_params(query, params, filters)
    }
    return params

def response(resp):
    try:
        response_data = resp.json()
        logger.debug(f'4get google response data: {response_data}')
        results = FourgetHijackerClient.normalize_results(response_data)
        logger.debug(f'google-4get results: {len(results)}')
        return results
    except Exception as e:
        logger.error(f'4get google response error: {e}')
        return []