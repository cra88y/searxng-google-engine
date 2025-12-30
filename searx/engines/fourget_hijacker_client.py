import requests
from typing import Dict, Any

class FourgetHijackerClient:
    def __init__(self, base_url: str = "http://4get-hijacked:80"):
        self.base_url = base_url

    def fetch(self, engine: str, params: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base_url}/harness.php"
        payload = {
            "engine": engine,
            "params": params
        }
        try:
            # SearXNG threads are synchronous; use requests.
            response = requests.post(url, json=payload, timeout=15)
            if response.status_code == 200:
                return response.json()
            return {"status": "error", "message": f"HTTP {response.status_code}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    @staticmethod
    def normalize_results(response_data: Any):
        results = []
        # If response_data is a list (direct results) or a dict with a list
        data = response_data.get("web") if isinstance(response_data, dict) else response_data
        
        if not isinstance(data, list):
            return results

        for item in data:
            results.append({
                "url": item.get("url"),
                "title": item.get("title"),
                "content": item.get("description") or item.get("snippet") or "",
            })
        return results