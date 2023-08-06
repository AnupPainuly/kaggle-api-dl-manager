#!/home/darkstar/lang/python/venv/bin/python3

from kaggle_dataset_downloader import KaggleDatasetDownloader
def main():
    dataset_dir = "/home/darkstar/Documents/code_humour/kaggle/datasets/"
    api_command = input("enter the API command: ")
    downloader = KaggleDatasetDownloader(api_command, dataset_dir)

    for i in downloader.dataset:
        print(i)
    downloader.close()

if __name__ == "__main__":
    main()

