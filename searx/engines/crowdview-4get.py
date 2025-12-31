from fourget_hijacker_client import FourgetHijackerClient
import logging

logger = logging.getLogger(__name__)

categories = ['general']
paging = True

def request(query, params):
    client = FourgetHijackerClient()
    filters = client.get_engine_filters('crowdview')
    params['url'] = 'http://4get-hijacked:80/harness.php'
    params['method'] = 'POST'
    params['json'] = {
        'engine': 'crowdview',
        'params': FourgetHijackerClient.get_4get_params(query, params, filters)
    }
    return params

def response(resp):
    try:
        response_data = resp.json()
        logger.debug(f'4get crowdview response data: {response_data}')
        results = FourgetHijackerClient.normalize_results(response_data)
        logger.debug(f'crowdview-4get results: {len(results)}')
        return results
    except Exception as e:
        logger.error(f'4get crowdview response error: {e}')
        return []
