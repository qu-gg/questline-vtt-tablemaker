<h2 align='center'>Questline VTT Table Maker</h2>


## About this Repository
Questline Table Maker is a Python-based PyQt5 application that allows users to generate tables from simple text files, which can then be imported into Questline VTT (Virtual Tabletop) software. This tool simplifies the process of creating game elements by automating the conversion of text data into structured tables that are compatible with Questline VTT.

Currently it only supports building rollable tables/Actions, but I hope to expand this into a general tool that can be used for items and characters even.
Help on that would be greatly welcome!

## Local Installation
```bash
# Clone the repository
git clone https://github.com/qu-gg/questline-vtt-tablemaker

# Navigate to the project directory
cd questlineTableMaker

# Install dependencies
pip install PyQt5

# Run the program
python questlineTableMaker.py
```

## Usage
To use Questline Table Maker, prepare a text file with your items listed, and then run the application. Follow the GUI prompts to import your text file and generate the table.

The text file should be just a bunch of lines where each line is its own item:

<img src="https://github.com/qu-gg/questline-vtt-tablemaker/assets/32918812/99de92da-eff1-44bf-bd71-811a60a4dea6" width="75%">

And the imported action should look something like this in Questline:

<img src="https://github.com/qu-gg/questline-vtt-tablemaker/assets/32918812/a115975d-6463-428d-a1f0-40896bd90d54" width="25%">

## Note on Anti-Virus Catching
It is a common occurrence that anti-viruses mistakenly flag Python executable programs that were compiled with PyInstaller as malicious software.<br> More information on this can be found <a href="https://github.com/hankhank10/false-positive-malware-reporting">here</a>.

## Issues and Contributions
Please feel free to put up any issues that are found or enhancements that would improve this work. <br>As well, please feel welcome to put up PRs for any improvements that you can do!
