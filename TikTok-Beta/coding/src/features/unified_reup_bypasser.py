import os
import subprocess


class UnifiedReupBypasser:
    def __init__(self, input_path: str):
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Không tìm thấy file video: {input_path}")

        self.input_path = input_path
        self.video_filters = []
        self.audio_filters = []
        self.speed_changed = False

    def apply_remove_logo(self, x: int, y: int, w: int, h: int):
        self.video_filters.append(f"delogo=x={x}:y={y}:w={w}:h={h}")
        return self

    def apply_mirror(self):
        self.video_filters.append("hflip")
        return self

    def apply_zoom(self, zoom_percentage: float = 3.0):
        # Đã sửa lỗi: Phóng to trước, cắt khung hình sau để giữ nguyên độ phân giải gốc
        zoom_factor = 1 + (zoom_percentage / 100.0)
        filter_str = f"scale=iw*{zoom_factor}:ih*{zoom_factor},crop=iw/{zoom_factor}:ih/{zoom_factor}"
        self.video_filters.append(filter_str)
        return self

    def apply_color_grading(
        self, brightness: float = 0.0, contrast: float = 1.0, saturation: float = 1.0
    ):
        # FFmpeg brightness: [-1.0, 1.0], contrast: [-1000, 1000], saturation: [0, 3]
        self.video_filters.append(
            f"eq=brightness={brightness}:contrast={contrast}:saturation={saturation}"
        )
        return self

    def apply_speed(self, speed_factor: float = 1.05):
        if speed_factor != 1.0:
            if speed_factor < 0.5 or speed_factor > 100.0:
                raise ValueError(
                    "Hệ số tốc độ âm thanh (atempo) chỉ hỗ trợ từ 0.5 đến 100.0"
                )
            self.speed_changed = True
            self.video_filters.append(f"setpts={1.0/speed_factor}*PTS")
            self.audio_filters.append(f"atempo={speed_factor}")
        return self

    def export(
        self,
        output_path: str,
        preset: str = "faster",
        crf: int = 23,
        use_gpu: bool = False,
    ):
        print("Đang khởi tạo luồng xử lý FFmpeg...")

        command = ["ffmpeg", "-y", "-hwaccel", "auto", "-i", self.input_path]

        if self.video_filters:
            vf_string = ",".join(self.video_filters)
            command.extend(["-vf", vf_string])

        if self.audio_filters:
            af_string = ",".join(self.audio_filters)
            command.extend(["-af", af_string])
            command.extend(["-c:a", "aac"])
        else:
            command.extend(["-c:a", "copy"])

        # Tùy chọn sử dụng GPU NVIDIA nếu có
        video_codec = "h264_nvenc" if use_gpu else "libx264"
        command.extend(["-c:v", video_codec, "-preset", preset])

        # NVENC không hỗ trợ cờ -crf một cách trực tiếp như libx264, cần điều chỉnh nếu dùng GPU
        if not use_gpu:
            command.extend(["-crf", str(crf)])
        else:
            command.extend(
                ["-cq", str(crf), "-b:v", "0"]
            )  # Cách cấu hình chất lượng cho NVENC

        command.append(output_path)

        try:
            # Tham số text=True yêu cầu Python 3.7+
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            print("-" * 50)
            print(f"Xử lý thành công! File lưu tại: {output_path}")
            print("-" * 50)
        except subprocess.CalledProcessError as e:
            print("Lỗi FFmpeg trong quá trình xuất file:")
            print(e.stderr)
