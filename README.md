# Google Sheets Address Checker

This Python script checks a list of wallet addresses against a Google Sheet and saves the matching addresses to a results file.


## Installation

1.  Clone the repository to your local machine:
```sh
   git clone https://github.com/your-username/google-sheets-address-checker.git
   cd google-sheets-address-checker ```
   
1. Create a virtual environment (optional but recommended):
```sh
python3 -m venv venv
source venv/bin/activate```

3. Install the required packages:
```sh
pip install -r requirements.txt```


## Getting Google Service Account
To use this script, you'll need a Google Service Account with the necessary permissions. Here's how to set it up:

- Go to the Google Cloud Console.

- Create a new project or select an existing one.

- In the left menu, navigate to "IAM & Admin" > "Service accounts".

- Create a new service account and download the JSON key file.

- Rename the JSON key file to **serviceaccount.json** and place it in the same directory as the script.

## Usage
- Place the addresses you want to check in the **addresses.txt** file, with each address on a separate line.

- Make sure you have the s**erviceaccount.json key** file in the same directory.

- Run the script ``` You know how ```
- The script will analyze the addresses and save the matching ones in the **results.txt** file.

- You can monitor the progress using the tqdm progress bar displayed in the terminal.

- After completion, the results will be available in the **results.txt** file.