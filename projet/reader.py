import xarray as xr


import xarray as xr
import requests
from io import BytesIO
import os


class WeatherDataLoader:
    def __init__(self, file_path, remote=False):
        """
        Initializes the data loader and loads the dataset.
        Can load from a local file or a remote URL.
        :param file_path: Path to the dataset file or URL.
        :param remote: Boolean flag indicating if the file is remote.
        """
        self.file_path = file_path
        self.remote = remote
        self.dataset = None
        self.load_dataset()

    def load_dataset(self):
        """
        Loads the dataset from a local or remote file.
        If remote, fetches the data via HTTP.
        """
        try:
            if self.remote:
                print(f"Downloading dataset from {self.file_path}...")
                response = requests.get(self.file_path)
                if response.status_code == 200:
                    # Load the dataset from the response content
                    data = BytesIO(response.content)
                    self.dataset = xr.open_dataset(data)
                    print(f"Remote NetCDF dataset loaded from {self.file_path}")
                else:
                    print(
                        f"Error: Failed to download dataset. Status code {response.status_code}"
                    )
            else:
                # Local file loading (NetCDF)
                if self.file_path.endswith(".nc") or self.file_path.endswith(".nc4"):
                    self.dataset = xr.open_dataset(self.file_path)
                    print(f"NetCDF dataset loaded from {self.file_path}")
                elif self.file_path.endswith(".csv"):
                    df = pd.read_csv(self.file_path)
                    self.dataset = xr.Dataset.from_dataframe(df)
                    print(f"CSV dataset loaded from {self.file_path}")
                else:
                    raise ValueError(
                        "Unsupported file format. Please use .nc, .nc4, or .csv."
                    )
        except requests.exceptions.RequestException as e:
            print(f"Error fetching remote dataset: {e}")
        except FileNotFoundError:
            print(f"Error: The file at {self.file_path} was not found.")
        except Exception as e:
            print(f"An error occurred while loading the dataset: {e}")

    def preprocess_data(self, variables=None, fill_missing="linear"):
        """
        Applies basic preprocessing such as selecting specific variables and filling missing values.
        :param variables: List of variable names to keep in the dataset (optional).
        :param fill_missing: Method to fill missing values ('linear', 'nearest', 'ffill', 'bfill', or None).
        """
        if self.dataset is None:
            print("No dataset loaded.")
            return

        if variables:
            self.dataset = self.dataset[variables]
            print(f"Selected variables: {variables}")

        if fill_missing:
            self.dataset = self.dataset.interpolate_na(method=fill_missing, dim="time")
            print(f"Missing values filled using '{fill_missing}' method.")

    def get_dataset(self):
        """
        Returns the processed dataset.
        :return: xarray.Dataset object.
        """
        return self.dataset


# Example usage with a remote dataset
if __name__ == "__main__":
    # Example URL for a remote NetCDF file (this is a placeholder URL)
    remote_url = "https://example.com/weather_data.nc"

    # Load and preprocess remote dataset
    loader = WeatherDataLoader(remote_url, remote=True)
    loader.preprocess_data(variables=["temperature", "humidity"], fill_missing="linear")
    dataset = loader.get_dataset()

    if dataset is not None:
        print("Remote dataset is ready for further analysis.")


# ds = xr.open_dataset(
#     "/home/newton/ienm2021/chabotv/COURS_CS/arome_forecast_2024100900.nc"
# )

# print(ds["t2m"])

# t2m_toulouse = ds["t2m"].sel(latitude=43.6, longitude=1.43, method="nearest")
# t2m_by_index = ds["t2m"].isel(latitude=198, longitude=705)
# t2m_area = ds["t2m"].sel(latitude=slice(44, 42), longitude=slice(0, 2))
# t2m_area = ds["t2m"].sel(latitude=slice(42, 44), longitude=slice(0, 2))

# # Moyenne temporelle pour toutes les variables du dataset
# ds_temporal_mean = ds.mean(dim="time")
# # Variation spatiale
# ds_std = ds.std(dim=["latitude", "longitude"])

# def conditional_mean(ds, lats, lons, altitude):
#     """
#     Fonction permettant de faire la moyenne sur une zone donnée
#     pour les points supérieur à une altitude donnée (altitude).
#     """
#     mask = ds["altitude"] > altitude
#     mean_da = ds["t2m"].sel(latitude=lats, longitude=lons).where(mask).mean()
#     print(f"{mean_da.long_name} mean is {str(mean_da.values.round(2))} {mean_da.units}")


# lats = slice(46, 44)
# lons = slice(-2, 2)
# altitude = 500
# conditional_mean(ds, lats, lons, altitude)
