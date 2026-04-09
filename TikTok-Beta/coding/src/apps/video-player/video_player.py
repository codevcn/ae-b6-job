from time import sleep
import sys
import os
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
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
from PySide6.QtGui import QShortcut, QKeySequence  # Thêm thư viện xử lý phím tắt
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget


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
        self.btn_audio_left = QPushButton("🔊 Audio Trái")
        self.btn_audio_right = QPushButton("🔇 Audio Phải")

        controls_layout.addWidget(self.btn_reset)
        controls_layout.addWidget(self.btn_prev)
        controls_layout.addWidget(self.btn_play_pause)
        controls_layout.addWidget(self.btn_next)
        controls_layout.addWidget(self.btn_audio_left)
        controls_layout.addWidget(self.btn_audio_right)


        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.volume_slider.setFixedWidth(120)
        controls_layout.addWidget(self.volume_slider)

        main_layout.addLayout(controls_layout)

        self.change_volume(50)
        self.switch_audio("left")  # Bật audio bên trái làm mặc định

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

        self.btn_audio_left.clicked.connect(lambda: self.switch_audio("left"))
        self.btn_audio_right.clicked.connect(lambda: self.switch_audio("right"))

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

        # Đảo nguồn âm thanh giữa Trái và Phải khi dùng phím tắt Ctrl+M
        QShortcut(QKeySequence("Ctrl+M"), self).activated.connect(self.toggle_audio_source)
        QShortcut(QKeySequence("Ctrl+,"), self).activated.connect(
            lambda: self.switch_audio("left")
        )
        QShortcut(QKeySequence("Ctrl+."), self).activated.connect(
            lambda: self.switch_audio("right")
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

        QShortcut(QKeySequence("Ctrl+Q"), self).activated.connect(self.close)

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

    def switch_audio(self, side: str):
        active_style = """
            QPushButton {
                background-color: #38bdf8;
                color: black;
                border: 1px solid #0284c7;
            }
            QPushButton:hover {
                background-color: #7dd3fc;
            }
        """
        normal_style = ""

        if side == "left":
            self.audio_left.setMuted(False)
            self.audio_right.setMuted(True)
            self.btn_audio_left.setText("🔊 Audio Trái")
            self.btn_audio_right.setText("🔇 Audio Phải")
            
            self.btn_audio_left.setStyleSheet(active_style)
            self.btn_audio_right.setStyleSheet(normal_style)
        elif side == "right":
            self.audio_left.setMuted(True)
            self.audio_right.setMuted(False)
            self.btn_audio_left.setText("🔇 Audio Trái")
            self.btn_audio_right.setText("🔊 Audio Phải")
            
            self.btn_audio_left.setStyleSheet(normal_style)
            self.btn_audio_right.setStyleSheet(active_style)

    def toggle_audio_source(self):
        # Đảo nguồn âm thanh hiện tại
        if not self.audio_left.isMuted():
            self.switch_audio("right")
        else:
            self.switch_audio("left")

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
