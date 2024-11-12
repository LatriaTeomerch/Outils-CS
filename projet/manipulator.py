import xarray as xr


class WeatherDataManipulator:
    def __init__(self, dataset):
        """
        Initializes the data manipulator with a dataset.
        :param dataset: xarray.Dataset object.
        """
        self.dataset = dataset

    def filter_by_time(self, start_time, end_time):
        """
        Filters the dataset by a specified time range.
        :param start_time: Start time for filtering.
        :param end_time: End time for filtering.
        :return: Filtered xarray.Dataset.
        """
        if "time" in self.dataset.coords:
            filtered_data = self.dataset.sel(time=slice(start_time, end_time))
            print(f"Filtered data from {start_time} to {end_time}")
            return filtered_data
        else:
            print("Error: Time coordinate not found in the dataset.")
            return self.dataset

    def calculate_mean_temperature(self):
        """
        Calculates the mean temperature over time.
        :return: xarray.DataArray representing the mean temperature.
        """
        if "temperature" in self.dataset.data_vars:
            mean_temp = self.dataset["temperature"].mean(dim="time")
            print("Calculated mean temperature.")
            return mean_temp
        else:
            raise KeyError("Dataset does not contain 'temperature' data variable.")

    def calculate_temperature_anomaly(
        self, reference_period=("2000-01-01", "2010-12-31")
    ):
        """
        Calculates temperature anomaly by comparing with a reference period.
        :param reference_period: Tuple with the start and end of the reference period.
        :return: xarray.DataArray representing the temperature anomaly.
        """
        start_ref, end_ref = reference_period
        ref_data = self.filter_by_time(start_ref, end_ref)
        mean_ref_temp = ref_data["temperature"].mean(dim="time")
        anomaly = self.dataset["temperature"] - mean_ref_temp
        print(
            f"Calculated temperature anomaly using reference period: {reference_period}"
        )
        return anomaly
