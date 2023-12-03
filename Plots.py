import plotly.express as px
import plotly.graph_objects as go


class DataAnalysis:
    def __init__(self, df):
        """
        Initialize the DataPlotter class.

        Parameters:
        - df (pd.DataFrame): The DataFrame containing the data.
        """
        self.df = df
        self.custom_palette = px.colors.qualitative.Plotly

    def plot_uni_variate_numerical(self, feature):
        """
        Generate a histogram to visualize the distribution of a numerical variable in a DataFrame.

        Parameters:
        - feature (str): The name of the numerical column in the DataFrame.

        Returns:
        - go.Figure: Plotly Figure object representing the histogram.
        """
        column = feature.replace(' ', '_').lower()
        fig = px.histogram(self.df, x=column, title=f'{feature} Distribution', labels={column: feature})
        return fig

    def plot_bi_variate_categorical_vs_numerical(self, num_feature, cat_feature):
        """
        Generate a grouped histogram to compare the mean of a numerical variable across categories in a DataFrame.

        Parameters:
        - num_feature (str): The name of the numerical column in the DataFrame.
        - cat_feature (str): The name of the categorical column in the DataFrame.

        Returns:
        - go.Figure: Plotly Figure object representing the grouped histogram.
        """
        num_col = num_feature.replace(' ', '_').lower()
        cat_col = cat_feature.replace(' ', '_').lower()
        group = self.df.groupby(cat_col)[[num_col]].mean().sort_values(by=num_col, ascending=False).reset_index()

        fig = px.histogram(group, x=cat_col, barmode='group', labels={cat_col: cat_feature, num_col: num_feature},
                           title=f'{cat_feature} vs {num_feature}', y=num_col, histfunc='avg', text_auto='.2f')

        return fig

    def scatterplot_bi_variate_numerical_vs_numerical(self, x_feature, y_feature):
        """
        Generate a scatter plot to visualize the relationship between two numerical variables in a DataFrame.

        Parameters:
        - x_feature (str): The name of the x-axis numerical column in the DataFrame.
        - y_feature (str): The name of the y-axis numerical column in the DataFrame.

        Returns:
        - go.Figure: Plotly Figure object representing the scatter plot.
        """
        x_col = x_feature.replace(' ', '_').lower()
        y_col = y_feature.replace(' ', '_').lower()
        fig = go.Figure(data=[go.Scatter(x=self.df[x_col], y=self.df[y_col], mode='markers')])
        fig.update_layout(xaxis_title=x_feature, yaxis_title=y_feature, title=f'{y_feature} by {x_feature}')
        return fig

    def multivariate_analysis(self, x_feature, y_feature, z_feature):
        """
        Generate a grouped histogram for multivariate analysis.

        Parameters:
        - x_feature (str): The variable for the x-axis.
        - y_feature (str): The variable for the y-axis.
        - z_feature (str): The grouping variable for color.

        Returns:
        - go.Figure: Plotly Figure object representing the grouped histogram.

        Example:
        #>>> DataPlotter(df).multivariate_analysis('age', 'income', 'gender')
        # Generates a grouped histogram of 'age' vs 'income' colored by 'gender'.
        """
        x = x_feature.replace(' ', '_').lower()
        y = y_feature.replace(' ', '_').lower()
        z = z_feature.replace(' ', '_').lower()
        fig = px.histogram(self.df, x=x, color=z, barmode='group',
                           labels={z: z_feature, y: y_feature, x: x_feature}, text_auto='.2f',
                           title=f'{x_feature} vs {y_feature} by {z_feature}', y=y, histfunc='avg')
        return fig

    def plot_uni_variate_categorical(self, feature):
        """
        Generate a pie chart to visualize the distribution of a categorical variable in a DataFrame.

        Parameters:
        - feature (str): The name of the categorical column in the DataFrame.

        Returns:
        - go.Figure: Plotly Figure object representing the pie chart.

        Example:
        #>>> DataPlotter(df).plot_uni_variate_categorical('category_column')
        """
        column = feature.replace(' ', '_').lower()

        fig = go.Figure(data=[go.Pie(labels=self.df[column], hole=0.3,
                                     textinfo='percent+label', marker=dict(colors=self.custom_palette))])

        fig.update_traces(textposition='inside')
        fig.update_layout(
            title=f'{feature} Contribution',
            legend=dict(title=column.replace('_', ' ').title()),
            margin=dict(l=0, r=0, b=0, t=50)
        )
        return fig

    def generate_correlation_heatmap(self, num_cols):
        """
        Generate a correlation heatmap for numerical columns in a DataFrame.

        Parameters:
        - num_cols (list): List of numerical column names for which to generate the heatmap.

        Returns:
        - go.Figure: Plotly Figure object representing the correlation heatmap.

        Example:
        #>>> correlation_heatmap = generate_correlation_heatmap(['num1', 'num2', 'num3'])
        #>>> correlation_heatmap.show()
        """
        correlation_matrix = self.df[num_cols].corr()

        fig = go.Figure(data=go.Heatmap(
            z=correlation_matrix.values,
            x=num_cols,
            y=num_cols,
            colorscale='YlGnBu',
            colorbar=dict(title='Correlation'),
            text=correlation_matrix.round(2),
            hoverinfo='text'))

        fig.update_layout(
            title='Correlation Heatmap',
            xaxis_title='Columns',
            yaxis_title='Columns',
            annotations=[dict(x=x, y=y, text=str(correlation_matrix.loc[y, x].round(4)),
                              showarrow=False, font=dict(size=12))
                         for x in num_cols for y in num_cols])

        return fig
