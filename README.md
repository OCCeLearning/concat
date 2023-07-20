# Simple Script that Combines Excel Files

This script was put together to allow the user to quickly put all excel files that should be "merged" into one directory/folder, execute the script, and receive one file with the all of the rows from all of the files.

**Notes**

1. This script expects the data to be on a sheet named "RawData." (Adjust the script as needed)

## How to Use this Script

1. Download/Clone the repository.
2. Install the packages

```
python3 -m pip install pandas openpyxl
```

3. Move your excel files into the input directory.
4. Execute the command

```
python3 -m main
```
