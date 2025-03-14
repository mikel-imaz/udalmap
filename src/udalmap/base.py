import requests


class UdalMap:

    REQUESTS_OK = 200
    
    def __init__(self):
        from . import REQUESTS_TIMEOUT
        self.base_uri = "https://api.euskadi.eus/udalmap"
        self.timeout = REQUESTS_TIMEOUT

    def _get_complete_url(self, path):
        return f"{self.base_uri}/{path}"

    def _request(self, path, params=None):
        url = self._get_complete_url(path)
        response = requests.get(url,
                                params=params,
                                timeout=self.timeout
                               )
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.json()

    def groups(self, **kwargs):
        """
        Find all groups.

        Args:
            lang: (optional) "SPANISH" (default), "BASQUE"
            summarized: (optional) "false" (default), "true"
        
        Returns:
            A dict respresentation of the JSON returned from the API.
        """
        path = "groups"
        return self._request(path, kwargs)

    def group(self, groupId, **kwargs):
        """
        Get a group.

        Args:
            groupId: (required)
            lang: (optional) "SPANISH" (default), "BASQUE"
            summarized: (optional) "false" (default), "true"
        
        Returns:
            A dict respresentation of the JSON returned from the API.
        """
        path = f"groups/{groupId}"
        return self._request(path, kwargs)

    def indicator_municipality(self, indicatorId, municipalityId, **kwargs):
        """
        Get a group.

        Args:
            indicatorId: (required)
            municipalityId: (required)
            lang: (optional) "SPANISH" (default), "BASQUE"
        
        Returns:
            A dict respresentation of the JSON returned from the API.
        """
        path = f"indicators/{indicatorId}/municipalities/{municipalityId}"
        return self._request(path, kwargs)