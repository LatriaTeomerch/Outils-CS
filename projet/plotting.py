import matplotlib.pyplot as plt


class WeatherDataVisualizer:
    def __init__(self):
        """
        Initializes the data visualizer.
        """
        pass

    def plot_data(self, data_array, title="Weather Data", cmap="viridis"):
        """
        Plots the given data array.
        :param data_array: xarray.DataArray to be plotted.
        :param title: Title of the plot.
        :param cmap: Colormap for the plot.
        """
        plt.figure(figsize=(10, 6))
        data_array.plot(cmap=cmap)
        plt.title(title)
        plt.show()

    def plot_anomaly(self, anomaly, title="Temperature Anomaly", cmap="coolwarm"):
        """
        Plots the temperature anomaly.
        :param anomaly: xarray.DataArray representing the temperature anomaly.
        :param title: Title of the plot.
        :param cmap: Colormap for the plot.
        """
        plt.figure(figsize=(10, 6))
        anomaly.plot(cmap=cmap)
        plt.title(title)
        plt.show()

    def plot_timeseries(self, time_data, variable, title="Timeseries Data"):
        """
        Plots a timeseries for a particular variable.
        :param time_data: xarray.DataArray or pandas Series for the time series.
        :param variable: Name of the variable to plot.
        :param title: Title of the plot.
        """
        plt.figure(figsize=(10, 6))
        time_data[variable].plot()
        plt.title(title)
        plt.xlabel("Time")
        plt.ylabel(variable)
        plt.show()
