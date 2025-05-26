from metaflow import FlowSpec, step, card

import pandas as pd
import numpy as np

class Assignment6(FlowSpec):
    """Generate random dataset and visualize using html cards"""

    @step
    def start(self):
        # create random dataset
        self.df = pd.DataFrame({
            'Category': np.random.choice(['A', 'B', 'C', 'D'], size = 50),
            'Value': np.random.rand(50) * 100
        })

        self.next(self.visualize)


    @card(type="html")
    @step
    def visualize(self):
        import seaborn as sns
        import matplotlib.pyplot as plt

        # plot and save the chart
        plot_path = 'plot.png'
        sns.histplot(self.df['Value'], kde=True)
        plt.title("Distribution of Random Values")
        plt.savefig(plot_path)
        plt.close()

        # convert data to html table
        table_html = self.df.to_html()

        # compose the html card
        self.html = f"""
        <h2> Random DataSet Analysis </h2>
        <p> This card shows a plot of the generated values </p>
        <img src="../plot.png" alt="plot" width="600" />
        <h3> Data Table </h3>
        {table_html}
        """

        self.next(self.end)


    @step
    def end(self):
        print("Ended")


if __name__ == "__main__":
    Assignment6()