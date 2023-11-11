import numpy as np; np.random.seed(sum(map(ord, 'calmap')))
import pandas as pd
import calmap
import calplot
from plotly_calplot import calplot
import matplotlib.pyplot as plt
from datetime import datetime

from drinker_thinker.src.io.query_runner import QueryRunner

class ContextManager(object):

    def __init__(self, configs):
        self.config = configs
        self.query_runner = QueryRunner(configs)
        self.query_runner.create_all_tables()

    def record_drinks(self, num_drinks, comment, date):
        self.query_runner.record_drinks(num_drinks, comment, date)

    def get_drinks(self):
        return self.query_runner.read_drinks()


    def heat_graph(self):

        drinks = self.query_runner.read_drinks()
        all_drinks = []

        ## TODO : get from the data probably
        start_date = '2023-11-01'
        end_date = '2023-12-31'

        all_dates = pd.date_range(start_date, end_date)

        mapping = {}

        for drink in drinks:
            mapping[drink[2]] = drink[0]

        for date in all_dates:
            date_str = date.strftime("%Y-%m-%d")
            if date_str in mapping:
                all_drinks.append(mapping[date_str])
            else:
                all_drinks.append(0)

        df = pd.DataFrame({
            "ds": all_dates,
            "values": all_drinks
        })
        fig = calplot(df, x="ds", y="values")
        fig.show()
