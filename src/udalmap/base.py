"""
udalmap.base

This module implements the base class of udalmap.
"""

import requests
from requests.exceptions import ConnectionError, HTTPError

class UdalMap:
    """Implements all available GET queries in Udalmap API.

    Attributes:
        timeout (float): for requests, in seconds
        
    """
    BASE_URI = "https://api.euskadi.eus/udalmap"
    HEADERS = {"accept": "application/json"}

    def __init__(self, timeout=5):
        self.timeout = timeout

    def _get_complete_url(self, path):
        return f"{UdalMap.BASE_URI}/{path}"

    def _request(self, path, params=None):
        url = self._get_complete_url(path)
        try:
            response = requests.get(url,
                                    params=params,
                                    headers=UdalMap.HEADERS,
                                    timeout=self.timeout
                                   )
            response.raise_for_status()
            response.encoding = "utf-8"
            return response.json()
            
        except ConnectionError as conn_err:
            print(f"Connection Error! {conn_err}.")
            
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")

    def groups(self, **kwargs):
        """Find all groups.
        /groups

        Args:
            lang (str, optional): "SPANISH" (default), "BASQUE"
            summarized (str, optional): "false" (default), "true"
        
        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = f"groups"
        return self._request(path, kwargs)

    def group(self, groupId, **kwargs):
        """Get a group.
        /groups/{groupId}

        Args:
            groupId (str, required): The id of group
            lang (str, optional): "SPANISH" (default), "BASQUE"
            summarized (str, optional): "false" (default), "true"
        
        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = f"groups/{groupId}"
        return self._request(path, kwargs)

    def subgroups(self, **kwargs):
        """Find subgroups of all groups.
        /subgroups

        Args:
            lang (str, optional): "SPANISH" (default), "BASQUE"
            summarized (str, optional): "false" (default), "true"
        
        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = f"subgroups"
        return self._request(path, kwargs)

    def subgroup(self, subgroupId, **kwargs):
        """Get a subgroup.
        /subgroups/{subgroupId}

        Args:
            subgroupId (str, required): The id of subgroup
            lang (str, optional): "SPANISH" (default), "BASQUE"
            summarized (str, optional): "false" (default), "true"
        
        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = f"subgroups/{subgroupId}"
        return self._request(path, kwargs)

    def group_subgroups(self, groupId, **kwargs):
        """Find all subgroups of a group.
        /groups/{groupId}/subgroups

        Args:
            groupId (str, required): The id of group
            lang (str, optional): "SPANISH" (default), "BASQUE"
            summarized (str, optional): "false" (default), "true"
        
        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = f"groups/{groupId}/subgroups"
        return self._request(path, kwargs)

    def indicators(self, **kwargs):
        """Find all indicators.
        /indicators

        Args:
            lang (str, optional): "SPANISH" (default), "BASQUE"
        
        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = f"indicators"
        return self._request(path, kwargs)

    def subgroup_indicators(self, subgroupId, **kwargs):
        """Find all indicators of a subgroup.
        /subgroups/{subgroupId}/indicators

        Args:
            subgroupId (str, required): The id of subgroup
            lang (str, optional): "SPANISH" (default), "BASQUE"
            summarized (str, optional): "false" (default), "true"
        
        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = f"subgroups/{subgroupId}/indicators"
        return self._request(path, kwargs)

    def municipality_indicators(self, municipalityId, **kwargs):
        """Find indicators by municipality.
        /indicators/municipalities/{municipalityId}

        Args:
            municipalityId (str, required): The id of municipality
            lang (str, optional): "SPANISH" (default), "BASQUE"
        
        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = f"indicators/municipalities/{municipalityId}"
        return self._request(path, kwargs)

    def indicator_data(self, indicatorId, **kwargs):
        """Get an indicator data.
        /indicators/{indicatorId}

        Args:
            indicatorId (str, required): The id of indicator
            lang (str, optional): "SPANISH" (default), "BASQUE"
        
        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = f"indicators/{indicatorId}"
        return self._request(path, kwargs)

    def indicator_entities_data(self, indicatorId, **kwargs):
        """Get all entities data of an indicator.
        /indicators/{indicatorId}/entities

        Args:
            indicatorId (str, required): The id of indicator
            lang (str, optional): "SPANISH" (default), "BASQUE"
        
        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = f"indicators/{indicatorId}/entities"
        return self._request(path, kwargs)

    def indicator_entity_data(self, indicatorId, entityId, **kwargs):
        """Get entity data of an indicator.
        /indicators/{indicatorId}/entities/{entityId}

        Args:
            indicatorId (str, required): The id of indicator
            entityId (str, required): The id of entity
            lang (str, optional): "SPANISH" (default), "BASQUE"
        
        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = f"indicators/{indicatorId}/entities/{entityId}"
        return self._request(path, kwargs)

    def indicator_regions_data(self, indicatorId, **kwargs):
        """Get all regions data of an indicator.
        /indicators/{indicatorId}/regions

        Args:
            indicatorId (str, required): The id of indicator
            lang (str, optional): "SPANISH" (default), "BASQUE"
        
        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = f"indicators/{indicatorId}/regions"
        return self._request(path, kwargs)

    def indicator_region_data(self, indicatorId, regionId, **kwargs):
        """Get regions data of an indicator.
        /indicators/{indicatorId}/regions/{regionId}

        Args:
            indicatorId (str, required): The id of indicator
            regionId (str, required): The id of region
            lang (str, optional): "SPANISH" (default), "BASQUE"
        
        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = f"indicators/{indicatorId}/regions/{regionId}"
        return self._request(path, kwargs)

    def indicator_municipalities_data(self, indicatorId, **kwargs):
        """Get all municipalities of an indicator.
        /indicators/{indicatorId}/municipalities

        Args:
            indicatorId (str, required): The id of indicator
            lang (str, optional): "SPANISH" (default), "BASQUE"
        
        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = f"indicators/{indicatorId}/municipalities"
        return self._request(path, kwargs)

    def indicator_municipality_data(self, indicatorId, municipalityId, **kwargs):
        """Get indicators data of a municipality.
        /udalmap/indicators/{indicatorId}/municipalities/{municipalityId}

        Args:
            indicatorId (str, required): The id of indicator
            municipalityId (str, required): The id of municipality
            lang (str, optional): "SPANISH" (default), "BASQUE"
        
        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = f"indicators/{indicatorId}/municipalities/{municipalityId}"
        return self._request(path, kwargs)