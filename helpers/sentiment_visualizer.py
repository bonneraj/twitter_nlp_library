from helpers.json_utils import list_from_json
from tabulate import tabulate
import seaborn as sns
import matplotlib.pyplot as plt
from helpers.dataframe_utils import get_df_from_json, print_dataframe

class SentimentVisualizer:

    def plot_bar_graph(self, sentiment_output_path):
        # read cleaned tweets json
        sentiment_output_df = get_df_from_json(sentiment_output_path)
        print(tabulate(sentiment_output_df, headers='keys', tablefmt='fancy_grid'))        
        # plot
        ax = sns.barplot(x='metric', y='mean', data=sentiment_output_df, palette="Blues_d")
        ax.bar_label(ax.containers[0])
        plt.show()

    def _customize_plot_settings(self):
        sns.set_theme(style="whitegrid")
       
