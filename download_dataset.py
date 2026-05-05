import os
import zipfile

def download_dataset():
    # Create data folder
    os.makedirs("data", exist_ok=True)

    print("Downloading dataset from Kaggle...")

    # Download dataset
    os.system(
        "kaggle datasets download -d clmentbisaillon/fake-and-real-news-dataset -p data/"
    )

    # Unzip dataset
    zip_path = "data/fake-and-real-news-dataset.zip"

    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall("data/")
        print("Dataset extracted successfully!")
    else:
        print("Download failed!")

if __name__ == "__main__":
    download_dataset()
