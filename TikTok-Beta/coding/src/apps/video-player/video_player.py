from time import sleep
import sys
import os
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QMainWindow,
    QScrollArea,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QSlider,
    QLabel,
    QSizePolicy,
)
from PySide6.QtCore import QUrl, Qt, QTimer
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget


# ===========================================================
# Dialog: Danh sách phím tắt
# ===========================================================
SHORTCUTS_DATA = [
    (
        "PHÁT VIDEO",
        [
            ("Space", "Phát / Tạm dừng"),
            ("Ctrl + Space", "Reset về đầu"),
            ("← (Arrow Left)", "Tua lùi 5 giây"),
            ("→ (Arrow Right)", "Tua tới 5 giây"),
        ],
    ),
    (
        "ÂM LƯỢNG",
        [
            ("↑ (Arrow Up)", "Tăng âm lượng (+2)"),
            ("↓ (Arrow Down)", "Giảm âm lượng (-2)"),
        ],
    ),
    (
        "NGUỒN AUDIO",
        [
            ("Ctrl + ,", "Option 1: chỉ nghe audio video Trái"),
            ("Ctrl + .", "Option 2: chỉ nghe audio video Phải"),
            ("Ctrl + M", "Option 3: toggle Mute / Unmute cả 2 video"),
        ],
    ),
    (
        "MỞ FILE",
        [
            ("Ctrl + [", "Chọn video bên Trái"),
            ("Ctrl + ]", "Chọn video bên Phải"),
        ],
    ),
    (
        "CỬA SỔ",
        [
            ("Ctrl + +  /  Ctrl + =", "Bật / Tắt toàn màn hình"),
            ("Ctrl + K", "Mở bảng phím tắt này"),
            ("Ctrl + Q", "Thoát ứng dụng"),
        ],
    ),
    (
        "BẢNG PHÍM TẮT",
        [
            ("Ctrl + Q", "Đóng bảng phím tắt này"),
        ],
    ),
]


class ShortcutsDialog(QDialog):
    """Popup hiển thị danh sách toàn bộ phím tắt của ứng dụng."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("⌨  Phím tắt")
        self.setFixedWidth(520)
        self.setModal(False)  # Không chặn cửa sổ chính
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, False)

        self.setStyleSheet(
            """
            QDialog {
                background-color: #1a1a24;
                border: 1px solid #2a2a3a;
            }
            QLabel#title {
                font-size: 18px;
                font-weight: bold;
                color: #25f4ee;
                padding-bottom: 4px;
            }
            QLabel#hint {
                font-size: 12px;
                color: #666;
                padding-bottom: 10px;
            }
            QLabel#group {
                font-size: 11px;
                font-weight: bold;
                letter-spacing: 1px;
                color: #fe2c55;
                padding-top: 12px;
                padding-bottom: 4px;
            }
            QLabel#key {
                font-size: 13px;
                font-family: Consolas, monospace;
                background-color: #2a2a3a;
                color: #f0eee8;
                border: 1px solid #3a3a4a;
                border-radius: 4px;
                padding: 7px 10px;
                min-width: 160px;
                min-height: 30px;
            }
            QLabel#desc {
                font-size: 13px;
                color: #cccccc;
                padding: 7px 0px 7px 12px;
                min-height: 30px;
            }
            QPushButton#close_btn {
                background-color: #2a2a3a;
                border: 1px solid #3a3a4a;
                border-radius: 6px;
                padding: 8px 24px;
                font-size: 13px;
                font-weight: bold;
                color: #f0eee8;
                margin-top: 12px;
            }
            QPushButton#close_btn:hover {
                background-color: #fe2c55;
                border-color: #fe2c55;
                color: white;
            }
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                background: #1a1a24;
                width: 6px;
                border-radius: 3px;
            }
            QScrollBar::handle:vertical {
                background: #3a3a4a;
                border-radius: 3px;
            }
        """
        )

        outer = QVBoxLayout(self)
        outer.setContentsMargins(20, 18, 20, 18)
        outer.setSpacing(0)

        # --- Tiêu đề ---
        title = QLabel("⌨  Phím tắt")
        title.setObjectName("title")
        outer.addWidget(title)

        hint = QLabel("Nhấn  Q  để đóng  •  Nhấn  Ctrl+K  để mở lại")
        hint.setObjectName("hint")
        outer.addWidget(hint)

        # --- Scrollable content ---
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        content_widget = QWidget()
        content_widget.setStyleSheet("background-color: transparent;")
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 4, 10, 8)
        content_layout.setSpacing(0)

        for idx, (group_name, shortcuts) in enumerate(SHORTCUTS_DATA):
            # Khoảng cách trước mỗi nhóm (trừ nhóm đầu tiên)
            if idx > 0:
                content_layout.addSpacing(14)

            group_label = QLabel(group_name)
            group_label.setObjectName("group")
            content_layout.addWidget(group_label)
            content_layout.addSpacing(4)

            for key, description in shortcuts:
                row = QHBoxLayout()
                row.setContentsMargins(0, 0, 0, 0)
                row.setSpacing(0)

                key_label = QLabel(key)
                key_label.setObjectName("key")
                key_label.setFixedWidth(200)
                key_label.setAlignment(
                    Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
                )

                desc_label = QLabel(description)
                desc_label.setObjectName("desc")
                desc_label.setWordWrap(True)
                desc_label.setAlignment(
                    Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft
                )

                row.addWidget(key_label)
                row.addWidget(desc_label, 1)
                content_layout.addLayout(row)
                content_layout.addSpacing(4)

        content_layout.addStretch()
        scroll.setWidget(content_widget)
        outer.addWidget(scroll)

        # --- Nút đóng ---
        close_btn = QPushButton("Đóng  (Q)")
        close_btn.setObjectName("close_btn")
        close_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        close_btn.clicked.connect(self.hide)
        outer.addWidget(close_btn, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Phím tắt Q đóng dialog
        QShortcut(QKeySequence("Ctrl+Q"), self).activated.connect(self.hide)

        # Tự điều chỉnh chiều cao phù hợp
        self.adjustSize()
        max_h = 560
        if self.height() > max_h:
            self.setFixedHeight(max_h)


class DualVideoPlayerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trình phát Video Kép (Hỗ trợ Phím tắt)")
        self.resize(1200, 700)

        self.setStyleSheet(
            """
            QWidget {
                background-color: #121212;
                color: white;
            }
            QPushButton {
                background-color: #2a2a2a;
                border: 1px solid #444444;
                border-radius: 4px;
                padding: 8px 15px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3a3a3a;
            }
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 8px;
                background: #333333;
                margin: 2px 0;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: white;
                border: 1px solid #5c5c5c;
                width: 14px;
                margin: -4px 0;
                border-radius: 7px;
            }
        """
        )

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 15)

        # 1. Khu vực hiển thị 2 Video
        video_area_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        self.video_widget_left = QVideoWidget()
        self.video_widget_left.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        self.btn_load_left = QPushButton("Chọn Video Trái")
        left_layout.addWidget(self.video_widget_left)
        left_layout.addWidget(self.btn_load_left)
        video_area_layout.addLayout(left_layout)

        right_layout = QVBoxLayout()
        self.video_widget_right = QVideoWidget()
        self.video_widget_right.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        self.btn_load_right = QPushButton("Chọn Video Phải")
        right_layout.addWidget(self.video_widget_right)
        right_layout.addWidget(self.btn_load_right)
        video_area_layout.addLayout(right_layout)

        main_layout.addLayout(video_area_layout, 1)

        self.player_left = QMediaPlayer()
        self.audio_left = QAudioOutput()
        self.player_left.setVideoOutput(self.video_widget_left)
        self.player_left.setAudioOutput(self.audio_left)

        self.player_right = QMediaPlayer()
        self.audio_right = QAudioOutput()
        self.player_right.setVideoOutput(self.video_widget_right)
        self.player_right.setAudioOutput(self.audio_right)

        # 2. Thanh tiến trình
        self.progress_slider = QSlider(Qt.Orientation.Horizontal)
        self.progress_slider.setRange(0, 0)
        self.progress_slider.setStyleSheet("margin-top: 10px; margin-bottom: 10px;")
        main_layout.addWidget(self.progress_slider)

        # 3. Các nút điều khiển
        controls_layout = QHBoxLayout()
        controls_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btn_reset = QPushButton("⏮ Về ban đầu")
        self.btn_prev = QPushButton("⏪ -5s")
        self.btn_play_pause = QPushButton("▶ Phát")
        self.btn_next = QPushButton("+5s ⏩")
        self.btn_audio_left = QPushButton("◄ Audio Trái")
        self.btn_audio_right = QPushButton("Audio Phải ►")
        self.btn_mute_all = QPushButton("🔊 Cả 2")

        controls_layout.addWidget(self.btn_reset)
        controls_layout.addWidget(self.btn_prev)
        controls_layout.addWidget(self.btn_play_pause)
        controls_layout.addWidget(self.btn_next)
        controls_layout.addWidget(self.btn_audio_left)
        controls_layout.addWidget(self.btn_audio_right)
        controls_layout.addWidget(self.btn_mute_all)

        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.volume_slider.setFixedWidth(120)
        controls_layout.addWidget(self.volume_slider)

        main_layout.addLayout(controls_layout)

        self.change_volume(50)
        # Trạng thái audio: 1=Trái, 2=Phải, 3=Cả 2 (toggle mute)
        self._audio_option = 1
        self._both_muted = False
        self._apply_audio_state()  # Áp dụng trạng thái mặc định (Audio Trái)

        # 4. Ngăn chặn việc phím Space click vào các nút đang focus
        self.remove_focus_policy()

        # 5. Khởi tạo Phím tắt
        self.setup_shortcuts()

        # 6. Kết nối tín hiệu
        self.btn_load_left.clicked.connect(lambda: self.load_video(self.player_left))
        self.btn_load_right.clicked.connect(lambda: self.load_video(self.player_right))

        self.btn_play_pause.clicked.connect(self.toggle_play_pause)
        self.btn_reset.clicked.connect(self.reset_videos)
        self.btn_prev.clicked.connect(self.seek_backward)
        self.btn_next.clicked.connect(self.seek_forward)

        self.btn_audio_left.clicked.connect(lambda: self.select_audio_option(1))
        self.btn_audio_right.clicked.connect(lambda: self.select_audio_option(2))
        self.btn_mute_all.clicked.connect(lambda: self.select_audio_option(3))

        self.volume_slider.valueChanged.connect(self.change_volume)
        self.progress_slider.sliderMoved.connect(self.set_position)

        self.player_left.positionChanged.connect(self.update_slider_position)
        self.player_left.durationChanged.connect(self.update_slider_duration)
        self.player_right.positionChanged.connect(self.update_slider_position)
        self.player_right.durationChanged.connect(self.update_slider_duration)

        self.player_left.mediaStatusChanged.connect(
            lambda status: self.on_media_status_changed(self.player_left, status)
        )
        self.player_right.mediaStatusChanged.connect(
            lambda status: self.on_media_status_changed(self.player_right, status)
        )

        # 7. Tự động tìm và nạp video mặc định nếu có
        self.auto_load_default_videos()

        # 8. Tạo dialog phím tắt (dùng chung, không tạo lại mỗi lần)
        self._shortcuts_dialog = ShortcutsDialog(self)

        # 9. Hiển thị popup phím tắt ngay khi mở app
        QTimer.singleShot(200, self.show_shortcuts)

    def auto_load_default_videos(self):
        """Tự động tìm 2 file input và output cấu hình sẵn để load vào 2 bên"""
        input_path = os.path.abspath("src/data/media/input/input_video.mp4")
        output_path = os.path.abspath("src/data/media/output/output_video.mp4")

        if os.path.exists(input_path):
            self.player_left.setSource(QUrl.fromLocalFile(input_path))
            self.player_left.pause()

        if os.path.exists(output_path):
            self.player_right.setSource(QUrl.fromLocalFile(output_path))
            self.player_right.pause()

    def remove_focus_policy(self):
        """Xóa focus khỏi tất cả các widget có thể tương tác để tránh xung đột phím Space"""
        widgets = [
            self.btn_load_left,
            self.btn_load_right,
            self.btn_reset,
            self.btn_prev,
            self.btn_play_pause,
            self.btn_next,
            self.btn_audio_left,
            self.btn_audio_right,
            self.btn_mute_all,
            self.progress_slider,
            self.volume_slider,
        ]
        for widget in widgets:
            widget.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def setup_shortcuts(self):
        """Định nghĩa và kết nối các phím tắt"""
        QShortcut(QKeySequence("Ctrl+["), self).activated.connect(
            lambda: self.load_video(self.player_left)
        )
        QShortcut(QKeySequence("Ctrl+]"), self).activated.connect(
            lambda: self.load_video(self.player_right)
        )

        QShortcut(QKeySequence(Qt.Key.Key_Space), self).activated.connect(
            self.toggle_play_pause
        )
        QShortcut(QKeySequence(Qt.Key.Key_Left), self).activated.connect(
            self.seek_backward
        )
        QShortcut(QKeySequence(Qt.Key.Key_Right), self).activated.connect(
            self.seek_forward
        )

        QShortcut(QKeySequence("Ctrl+Space"), self).activated.connect(self.reset_videos)

        # Ctrl+M: toggle Option 3 (Mute/Unmute cả 2)
        QShortcut(QKeySequence("Ctrl+M"), self).activated.connect(
            lambda: self.select_audio_option(3)
        )
        QShortcut(QKeySequence("Ctrl+,"), self).activated.connect(
            lambda: self.select_audio_option(1)
        )
        QShortcut(QKeySequence("Ctrl+."), self).activated.connect(
            lambda: self.select_audio_option(2)
        )

        QShortcut(QKeySequence(Qt.Key.Key_Up), self).activated.connect(
            self.increase_volume
        )
        QShortcut(QKeySequence(Qt.Key.Key_Down), self).activated.connect(
            self.decrease_volume
        )
        QShortcut(QKeySequence("Ctrl++"), self).activated.connect(
            self.toggle_fullscreen
        )
        QShortcut(QKeySequence("Ctrl+="), self).activated.connect(
            self.toggle_fullscreen
        )

        # Mở bảng phím tắt
        QShortcut(QKeySequence("Ctrl+K"), self).activated.connect(self.show_shortcuts)

        QShortcut(QKeySequence("Ctrl+Q"), self).activated.connect(self.close)

    def show_shortcuts(self):
        """Hiển thị popup danh sách phím tắt."""
        self._shortcuts_dialog.show()
        self._shortcuts_dialog.raise_()
        self._shortcuts_dialog.activateWindow()
        # Căn giữa so với cửa sổ chính
        main_geo = self.geometry()
        dlg_geo = self._shortcuts_dialog.frameGeometry()
        cx = main_geo.left() + (main_geo.width() - dlg_geo.width()) // 2
        cy = main_geo.top() + (main_geo.height() - dlg_geo.height()) // 2
        self._shortcuts_dialog.move(cx, cy)

    def load_video(self, player):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Chọn tệp video")
        file_dialog.setNameFilter("Video Files (*.mp4 *.avi *.mkv *.mov)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                video_url = QUrl.fromLocalFile(selected_files[0])
                player.setSource(video_url)
                player.pause()

    def toggle_play_pause(self):
        state_left = self.player_left.playbackState()
        state_right = self.player_right.playbackState()

        if (
            state_left == QMediaPlayer.PlaybackState.PlayingState
            or state_right == QMediaPlayer.PlaybackState.PlayingState
        ):
            self.player_left.pause()
            self.player_right.pause()
            self.btn_play_pause.setText("▶ Phát")
        else:
            if self.player_left.mediaStatus() == QMediaPlayer.MediaStatus.EndOfMedia:
                self.player_left.setPosition(0)
            if self.player_right.mediaStatus() == QMediaPlayer.MediaStatus.EndOfMedia:
                self.player_right.setPosition(0)

            self.player_left.play()
            self.player_right.play()
            self.btn_play_pause.setText("⏸ Tạm dừng")

    def reset_videos(self):
        self.player_left.setPosition(0)
        self.player_right.setPosition(0)

    def seek_backward(self):
        for player in [self.player_left, self.player_right]:
            current_position = player.position()
            new_position = max(0, current_position - 5000)
            player.setPosition(new_position)

    def seek_forward(self):
        for player in [self.player_left, self.player_right]:
            current_position = player.position()
            duration = player.duration()
            new_position = min(duration, current_position + 5000)
            player.setPosition(new_position)

    # --- Audio styles ---
    _STYLE_AUDIO_ACTIVE = """
        QPushButton {
            background-color: #38bdf8;
            color: #0a0a0f;
            border: 1px solid #0284c7;
            font-weight: bold;
        }
        QPushButton:hover { background-color: #7dd3fc; }
    """
    _STYLE_BOTH_MUTED = """
        QPushButton {
            background-color: #fe2c55;
            color: white;
            border: 1px solid #c0143c;
            font-weight: bold;
        }
        QPushButton:hover { background-color: #ff6b9d; }
    """
    _STYLE_BOTH_UNMUTED = """
        QPushButton {
            background-color: #4ade80;
            color: #0a0a0f;
            border: 1px solid #16a34a;
            font-weight: bold;
        }
        QPushButton:hover { background-color: #86efac; }
    """

    def select_audio_option(self, option: int):
        """Chọn option audio:
        1 = chỉ nghe Trái
        2 = chỉ nghe Phải
        3 = toggle Mute/Unmute cả 2
        """
        if option == 3:
            if self._audio_option != 3:
                # Chuyển sang option 3 lần đầu: mặc định là Muted
                self._audio_option = 3
                self._both_muted = True
            else:
                # Đang ở option 3: toggle trạng thái
                self._both_muted = not self._both_muted
        else:
            self._audio_option = option
        self._apply_audio_state()

    def _apply_audio_state(self):
        """Cập nhật mute và style của cã 3 nút audio dựa theo _audio_option."""
        off = ""
        if self._audio_option == 1:
            self.audio_left.setMuted(False)
            self.audio_right.setMuted(True)
            self.btn_audio_left.setText("◄ Audio Trái")
            self.btn_audio_right.setText("Audio Phải ►")
            self.btn_mute_all.setText("🔊 Cả 2")
            self.btn_audio_left.setStyleSheet(self._STYLE_AUDIO_ACTIVE)
            self.btn_audio_right.setStyleSheet(off)
            self.btn_mute_all.setStyleSheet(off)
        elif self._audio_option == 2:
            self.audio_left.setMuted(True)
            self.audio_right.setMuted(False)
            self.btn_audio_left.setText("◄ Audio Trái")
            self.btn_audio_right.setText("Audio Phải ►")
            self.btn_mute_all.setText("🔊 Cả 2")
            self.btn_audio_left.setStyleSheet(off)
            self.btn_audio_right.setStyleSheet(self._STYLE_AUDIO_ACTIVE)
            self.btn_mute_all.setStyleSheet(off)
        elif self._audio_option == 3:
            self.audio_left.setMuted(self._both_muted)
            self.audio_right.setMuted(self._both_muted)
            self.btn_audio_left.setText("◄ Audio Trái")
            self.btn_audio_right.setText("Audio Phải ►")
            self.btn_audio_left.setStyleSheet(off)
            self.btn_audio_right.setStyleSheet(off)
            if self._both_muted:
                self.btn_mute_all.setText("🔇 Muted")
                self.btn_mute_all.setStyleSheet(self._STYLE_BOTH_MUTED)
            else:
                self.btn_mute_all.setText("🔊 Unmuted")
                self.btn_mute_all.setStyleSheet(self._STYLE_BOTH_UNMUTED)

    def change_volume(self, value):
        volume_level = value / 100.0
        self.audio_left.setVolume(volume_level)
        self.audio_right.setVolume(volume_level)

    def update_slider_duration(self):
        max_duration = max(self.player_left.duration(), self.player_right.duration())
        self.progress_slider.setRange(0, max_duration)

    def update_slider_position(self):
        current_pos = max(self.player_left.position(), self.player_right.position())
        self.progress_slider.blockSignals(True)
        self.progress_slider.setValue(current_pos)
        self.progress_slider.blockSignals(False)

    def set_position(self, position):
        self.player_left.setPosition(position)
        self.player_right.setPosition(position)

    def on_media_status_changed(self, player, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            player.setPosition(player.duration())
            player.pause()

            if (
                self.player_left.playbackState()
                != QMediaPlayer.PlaybackState.PlayingState
                and self.player_right.playbackState()
                != QMediaPlayer.PlaybackState.PlayingState
            ):
                self.btn_play_pause.setText("▶ Phát")

    def increase_volume(self):
        current_volume = self.volume_slider.value()
        new_volume = min(100, current_volume + 2)
        self.volume_slider.setValue(new_volume)

    def decrease_volume(self):
        current_volume = self.volume_slider.value()
        new_volume = max(0, current_volume - 2)
        self.volume_slider.setValue(new_volume)

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DualVideoPlayerWindow()
    window.show()
    sys.exit(app.exec())
