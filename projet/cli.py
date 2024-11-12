import argparse
import yaml
import xarray as xr
from weather_data_loader import WeatherDataLoader
from weather_data_manipulator import WeatherDataManipulator
from weather_data_visualizer import WeatherDataVisualizer


def load_config(config_file):
    """
    Load the configuration from a YAML file.
    :param config_file: Path to the YAML configuration file.
    :return: Configuration as a dictionary.
    """
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    return config


def main(config_file):
    # Load configuration
    config = load_config(config_file)

    # Load the dataset
    loader = WeatherDataLoader(
        config["dataset"]["file_path"], remote=config["dataset"]["remote"]
    )
    loader.preprocess_data(
        variables=config["dataset"]["variables"],
        fill_missing=config["dataset"]["fill_missing"],
    )
    dataset = loader.get_dataset()

    # Data Manipulation
    manipulator = WeatherDataManipulator(dataset)
    filtered_dataset = manipulator.filter_by_time(
        config["processing"]["start_time"], config["processing"]["end_time"]
    )

    # Visualize based on configuration
    visualizer = WeatherDataVisualizer()
    plot_type = config["visualization"]["plot_type"]

    if plot_type == "mean_temperature":
        mean_temp = manipulator.calculate_mean_temperature()
        visualizer.plot_data(
            mean_temp,
            title=config["visualization"]["title"],
            cmap=config["visualization"]["cmap"],
        )

    elif plot_type == "anomaly":
        anomaly = manipulator.calculate_temperature_anomaly(
            reference_period=config["processing"]["reference_period"]
        )
        visualizer.plot_anomaly(
            anomaly,
            title=config["visualization"]["title"],
            cmap=config["visualization"]["cmap"],
        )

    elif plot_type == "timeseries":
        # If the user wants a timeseries plot
        visualizer.plot_timeseries(
            filtered_dataset,
            variable=config["visualization"]["plot_timeseries_variable"],
            title=config["visualization"]["title"],
        )

    else:
        print("Error: Invalid plot type specified in the configuration.")


if __name__ == "__main__":
    # Define the command-line argument for the config file
    parser = argparse.ArgumentParser(description="Weather Data Processing CLI")
    parser.add_argument(
        "--config", type=str, required=True, help="Path to the YAML configuration file"
    )
    args = parser.parse_args()

    # Run the main function
    main(args.config)
