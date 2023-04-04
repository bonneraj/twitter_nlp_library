import seaborn as sns
import matplotlib.pyplot as plt

class WordCloudVisualizer:

    def plot_standalone_bar_graph(self, word_cloud_object, world_cloud_file_path) -> plt:
        '''Plots word cloud for given query'''
        # plot word cloud
        plt.figure(figsize=(15,8))
        plt.imshow(word_cloud_object)
        plt.axis("off")
        
        # save figure as png for future reference
        plt.savefig(world_cloud_file_path + ".png", bbox_inches='tight')
        return plt

