import sys
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from ..functions.pokedex_functions import find_details_move

class MoveSelectionDialog(QDialog):
    def __init__(self, mainpokemon_attacks):
        super().__init__()

        # Dialog settings
        self.setWindowTitle("选择招数")
        self.resize(300, 200)
        self.selected_move = None
        self.mainpokemon_attacks = mainpokemon_attacks

        # Create and set layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Add a title label
        title_label = QLabel("请选择你的招数（按 1-4 或者直接点击选择）")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont("霞鹜文楷 GB 屏幕阅读版", 14, QFont.Weight.Bold))
        layout.addWidget(title_label)

        # Add labels for each move
        self.move_labels = []
        for index, move in enumerate(mainpokemon_attacks):
            move_detail = find_details_move(move)
            move_label = QLabel(f"{index + 1}.{move_detail['name_zh']}({move_detail['basePower']}): {move_detail['shortDesc']}")
            move_label.setToolTip(f"{move_detail['desc']}")
            move_label.setFont(QFont("微软雅黑", 12))
            move_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            move_label.setStyleSheet("border: 1px solid #ccc; border-radius: 0px;")  # Removed padding, reduced border-radius
            move_label.mousePressEvent = self.create_mouse_press_handler(index)
            move_label.setFixedHeight(20)  # Example fixed height for thinner labels
            layout.addWidget(move_label)
            self.move_labels.append(move_label)


    def create_mouse_press_handler(self, index):
        def handle_mouse_press(event):
            self.select_move(index)
        return handle_mouse_press

    def select_move(self, index):
        """Handle move selection and close the dialog."""
        self.selected_move = self.mainpokemon_attacks[index]
        self.accept()

    def keyPressEvent(self, event):
        """Handle keyboard shortcuts for move selection."""
        key = event.key()
        if Qt.Key.Key_1 <= key <= Qt.Key.Key_9:
            move_index = key - Qt.Key.Key_1  # Convert key to list index
            if 0 <= move_index < len(self.mainpokemon_attacks):
                self.select_move(move_index)
