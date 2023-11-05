from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                             QWidget,QPushButton,QLabel,QLineEdit,QTextEdit,QListWidget,
                             QVBoxLayout,QHBoxLayout)
import json
app = QApplication([])

notes = {
    "Ласкаво просимо!" : {
        "текст" : "Це найкращий додаток для заміток у світі!",
        "теги" : ["добро", "інструкція"]
    }
}

with open("f.json","w") as file:
    json.dump(notes,file)







notes_win = QWidget()
notes_win.setWindowTitle("Smart Notes")
notes_win.resize(900,600)


list_notes = QListWidget()
list_notes_label = QLabel("Notes list")

btn_note_create = QPushButton("Create note")
btn_note_save = QPushButton("Save")
btn_note_delete = QPushButton("Delete")

field_tag = QLineEdit("")
field_tag.setPlaceholderText("Set tag name")

field_text=QTextEdit()

btn_tag_add = QPushButton("Add tag to note")
btn_tag_delete = QPushButton("Delete note's tag")
btn_tag_search = QPushButton("Look for notes by tag")

list_tags = QListWidget()
list_tags_label = QLabel("List of tags")

#Widged placement

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col1.addWidget(field_text)

col2 = QVBoxLayout()
col2.addWidget(list_notes_label)
col2.addWidget(list_notes)

row1 = QHBoxLayout()
row1.addWidget(btn_note_create)
row1.addWidget(btn_note_delete)

row2 = QHBoxLayout()
row2.addWidget(btn_note_save)

col2.addLayout(row2)
col2.addLayout(row1)


col2.addWidget(list_tags_label)
col2.addWidget(list_tags)
col2.addWidget(field_tag)
row3 = QHBoxLayout()
row3.addWidget(btn_tag_add)
row3.addWidget(btn_tag_delete)
col2.addLayout(row3)
row4 = QHBoxLayout()
row4.addWidget(btn_tag_search)
col2.addLayout(row4)

layout_notes.addLayout(col1)
layout_notes.addLayout(col2)
notes_win.setLayout(layout_notes)

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["теги"])

list_notes.itemClicked.connect(show_note)
list_notes.addItems(notes)

notes_win.show()
app.exec_()

