"""
udalmap.utils

This module implements convenient classes to get info from udalmap API.
"""

from .base import UdalMap
import pandas as pd
import matplotlib.pyplot as plt

class UdmDf(UdalMap):
    """Gets Udalmap API info into Pandas dataframes.
    
    """

    def __init__(self):
        UdalMap.__init__(self, timeout=5)

    def find(self):
        """Provides all indicators in a Pandas dataframe.

        Args:
        
        Returns:
            A Pandas dataframe.
        """
        groups = self.groups()
        
        group_ls, subgroup_ls, indicator_ls = [], [], []
        for group in groups:
            for subgroup in group["subgroups"]:
                for indicator in subgroup["indicators"]:
                    indicator_ls.append(f"{indicator["id"]}: {indicator["name"]}")
                    subgroup_ls.append(f"{subgroup["id"]}: {subgroup["name"]}")
                    group_ls.append(f"{group["id"]}: {group["name"]}")

        return pd.DataFrame({"group": group_ls,
                             "subgroup": subgroup_ls,
                             "indicator": indicator_ls})

    def get(self, indicatorId, body):
        """Provides an indicator data in a Pandas dataframe.

        Args:
            indicatorId (str, required): The id of indicator
            body (str, required): "entities", "regions", "municipalities"
        
        Returns:
            A Pandas dataframe.
        """
        data = self.indicator_data(indicatorId)

        names, years = [], []
        for item in data[body]:
            names.append(item["name"])
            years.append(item["years"][0])
        
        return pd.DataFrame(years, index=names)

    def plot(self, indicatorId, body, filters=None):
        """Plots an indicator data for a body.

        Args:
            indicatorId (str, required): The id of indicator
            body (str, required): "entities", "regions", "municipalities"
            filters (list[str], optional): filters items to plot
        
        Returns:
            A Matplotlib plot.
        """
        df = self.get(indicatorId, body)
        if filters is not None:
            df = df.loc[filters, :]

        lookup_name = {item["id"]: item["name"] for item in self.indicators()}
        
        fig, ax = plt.subplots()
        df.transpose().plot(ax=ax)
        ax.set_title(f"{indicatorId}: {lookup_name[indicatorId]}")
        plt.show()