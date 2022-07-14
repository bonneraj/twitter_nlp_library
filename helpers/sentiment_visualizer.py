from helpers.json_utils import list_from_json
import seaborn as sns
import matplotlib.pyplot as plt
from helpers.dataframe_utils import get_df_from_json

class SentimentVisualizer:

    def plot_standalone_bar_graph(self, sentiment_output_path, keyword):
        # read cleaned tweets json
        sentiment_output_df = get_df_from_json(sentiment_output_path)
        # plot bar plot
        ax = sns.barplot(x='metric', y='mean', data=sentiment_output_df, palette="Blues_d")
        ax.bar_label(ax.containers[0])
        ax.set(title=f'Tweet Keyword: {keyword}')
        plt.plot()
        
        # save figure as pdf for future reference
        plt.savefig(sentiment_output_path.replace(".json", ".png"))
        plt.show()
        return plt

    def _customize_plot_settings(self):
        sns.set_theme(style="whitegrid")       
