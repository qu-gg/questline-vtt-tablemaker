import random
import string
import sys
import json
import copy

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QGroupBox, QGridLayout,
                             QLineEdit, QFileDialog, QPushButton, QComboBox)


TEMPLATE = [
  {
    "displayName": "A Random Table - ",
    "effects": [
      {
        "hide": False,
        "tableBaseRoll": "",
        "baseRoll": "",
        "type": "table",
        "advantageType": "none",
        "encounterRoll": False,
        "bonus": 0,
        "selectedDie": "",
        "quantity": 1,
        "name": "Item",
        "tableName": "Items"
      }
    ],
    "type": "roll tables",
    "details": [
      {
        "value": {
          "table": {
            "name": "Items",
            "rows": [],
            "baseRoll": ""
          }
        },
        "visibility": "resultsOnly",
        "type": "table"
      }
    ],
    "privacy": {
      "level": "public",
      "users": []
    },
    "image": {
      "tokenCrop": {
        "y": 0,
        "x": 0,
        "width": 100,
        "height": 100,
        "aspect": 1,
        "unit": "%"
      },
      "url": "https://firebasestorage.googleapis.com/v0/b/rpg-pbp.appspot.com/o/games%2Fn9qXCE2Ylwj8dBmy4lpo%2Fimages%2FR63C00NUgwM5aWxFDbQg.png?alt=media&token=c5326c3b-ecaa-47fe-9cd5-29af8924f5db"
    },
    "id": "vvSU9QmslWCmNreOUYD5"
  }
]


class Window(QMainWindow):
    def __init__(self, basedir):
        super(Window, self).__init__()

        # Load classes
        self.basedir = basedir

        # Window Title
        self.setWindowTitle("QuestlineVTT Table Maker")

        # Base Groupbox to hold the lines
        base_stats_group = QGroupBox("")
        base_stats_layout = QGridLayout()
        base_stats_layout.setAlignment(Qt.AlignTop)

        # Filepath display for table data
        self.table_path = QLineEdit("")

        # Buttons and file dialog associated with selecting local files
        gridlayout = QGridLayout()
        self.table_filedialog = QFileDialog()
        self.table_select = QPushButton("Open")
        self.table_select.clicked.connect(self.open_file)
        gridlayout.addWidget(self.table_path, 0, 1)
        gridlayout.addWidget(self.table_select, 0, 2)

        base_stats_layout.addWidget(QLabel("Table Data Path:"), 0, 0)
        base_stats_layout.addLayout(gridlayout, 0, 1)

        # Dice
        dice = ["d100", "d20", "d10", "d8", "d6", "d4", "d2"]
        base_stats_layout.addWidget(QLabel("Die Size: "), 1, 0)
        self.die_box = QComboBox()
        for item in dice:
            self.die_box.addItem(item)
        base_stats_layout.addWidget(self.die_box, 1, 1)

        # Make the execute button
        self.button = QPushButton("Execute")
        self.button.clicked.connect(lambda: self.create_table())
        base_stats_layout.addWidget(self.button, 4, 0, 1, -1)

        # Grid layout
        base_stats_group.setFixedWidth(500)
        base_stats_group.setFixedHeight(100)
        base_stats_group.setLayout(base_stats_layout)
        self.setCentralWidget(base_stats_group)

    def open_file(self):
        """ Handles opening a file for the art path images; if an invalid image then show a message to the statusbar """
        self.pdf_path = self.table_filedialog.getOpenFileName(self, 'Load File', self.basedir + '/')[0]
        self.table_path.setText(self.pdf_path)

    def create_table(self):
        # Load in an Action template
        data = copy.deepcopy(TEMPLATE)
        data[0]["details"][0]["value"]["table"]["rows"] = list()

        # Set a random ID
        data[0]["id"] = ''.join(random.choices(string.ascii_letters + string.digits, k=20))

        # Set a random display name
        displayName = data[0]["displayName"] + ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        data[0]["displayName"] = displayName

        # Get and set the dice size
        dice_size = int(self.die_box.currentText().replace('d', ''))
        data[0]["effects"][0]["baseRoll"] = f"1d{dice_size}"
        data[0]["effects"][0]["tableBaseRoll"] = f"1d{dice_size}"
        data[0]["effects"][0]["selectedDie"] = f"d{dice_size}"
        data[0]["details"][0]["value"]["table"]["baseRoll"] = f"1d{dice_size}"

        # Insert item results into JSON
        items = open(self.table_path.text(), 'r', encoding='utf-8', errors='replace').readlines()
        for item_num in range(dice_size):
            # Get the item
            if item_num < len(items):
                item_result = items[item_num].replace('\n', '')
            else:
                item_result = "TO-FILL"

            # Add the item
            data[0]["details"][0]["value"]["table"]["rows"].append(
                {
                    'showDescription': False,
                    'result': item_result,
                    'range': {'start': item_num, 'end': item_num}
                }
            )

        # Output to JSON
        json.dump(data, open(f"{displayName}.actions", 'w'))


if __name__ == '__main__':
    # Specify whether this is local development or application compilation
    basedir = ""
    application = True

    # If application compilation, get the folder from which the executable is being executed
    if application:
        # First split depending on OS to get the current application name (in case users have modified it)
        if '/' in sys.executable:
            current_app_name = sys.executable.split('/')[-1]
        elif '\\' in sys.executable:
            current_app_name = sys.executable.split('\\')[-1]
        else:
            raise NotADirectoryError("Pathing not found for {}. Please move to another path!".format(sys.executable))

        # Then replace the application name with nothing to get the path
        basedir = sys.executable.replace(current_app_name, '')

    # Define the application
    app = QApplication(sys.argv)
    window = Window(basedir)

    # Different checking needed depending on local build or executable run
    window.show()
    sys.exit(app.exec_())
