import os
import zipfile
import pandas as pd
import tempfile
import subprocess
import shutil

class KaggleDatasetDownloader:
    def __init__(self, api_command, dataset_dir):
        self.api_command = api_command
        self.temp_dir = None
        self.dataset_dir = dataset_dir
        self.dataset = []
        self.filenames = []
        self._setup()

    def _setup(self):
        try:
            self.temp_dir = tempfile.mkdtemp()
            print(f"Temp directory created: {self.temp_dir}")
            self._execute_api_command()
            print("API command executed")
            self._extract_files()
            print("Files extracted")
            self._read_csv_files()
            print("CSV files read")
        except Exception as e:
            self._cleanup_temp_dir()
            raise e

    def _execute_api_command(self):
        os.chdir(self.temp_dir)  # Change the current working directory to the temp directory
        subprocess.run(self.api_command, shell=True, check=True)

    def _extract_files(self):
        with zipfile.ZipFile(self._zip_filename(), "r") as zip_ref:
            zip_basename = os.path.splitext(os.path.basename(self._zip_filename()))[0]
            destination_folder = os.path.join(self.dataset_dir, zip_basename)
            try:
                os.makedirs(destination_folder)
                zip_ref.extractall(destination_folder)
            except FileExistsError:
                print(f"Warning: Folder '{zip_basename}' already exists in '{self.dataset_dir}'. Contents not extracted.")


    def _read_csv_files(self):
        filenames = os.listdir(self.dataset_dir)
        for filename in filenames:
            if filename.lower().endswith(".csv"):
                file_path = os.path.join(self.dataset_dir, filename)
                df = pd.read_csv(file_path)
                self.dataset.append(df)
                self.filenames.append(filename)

    def _zip_filename(self):
        return os.path.join(self.temp_dir, self.api_command.split('/')[-1] + ".zip")

    def _cleanup_temp_dir(self):
         if self.temp_dir:
            try:
                for filename in os.listdir(self.temp_dir):
                    file_path = os.path.join(self.temp_dir, filename)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                os.rmdir(self.temp_dir)
                print("Temporary directory cleaned up successfully.")
            except Exception as e:
                print(f"Error during cleanup: {e}")
    
    def close(self):
        self._cleanup_temp_dir()

