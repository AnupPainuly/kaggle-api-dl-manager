# Kaggle Dataset Downloader

The `KaggleDatasetDownloader` is a Python class that simplifies the process of downloading and working with Kaggle datasets. This class automates the download, extraction, and reading of CSV files from Kaggle datasets, making it easier to integrate Kaggle datasets into your data analysis workflow.

## Features

- Automates downloading and extracting Kaggle datasets
- Reads extracted CSV files into Pandas DataFrames
- Provides a clean interface for dataset management

## Installation

Clone or download this repository to include the `kaggle_dataset_downloader.py` file in your project.

## Usage

1. Import the `KaggleDatasetDownloader` class:

    ```python
    from kaggle_dataset_downloader import KaggleDatasetDownloader
    ```

2. Create an instance of the `KaggleDatasetDownloader` class:

    ```python
    api_command = "your/kaggle/api/command"
    dataset_dir = "/path/to/your/dataset/folder"
    downloader = KaggleDatasetDownloader(api_command, dataset_dir)
    ```

3. Download and work with the dataset:

    ```python
    downloader.download_and_extract()
    # ... Perform data analysis or processing using downloader.dataset ...
    downloader.close()  # Clean up temporary files
    ```

4. Make sure to replace `"your/kaggle/api/command"` and `"/path/to/your/dataset/folder"` with the actual Kaggle API command and the desired directory to extract the dataset.

