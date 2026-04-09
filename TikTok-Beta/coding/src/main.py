import sys
from features.unified_reup_bypasser import UnifiedReupBypasser
from utils.helpers import load_configs, resolve_path

# Fix UnicodeEncodeError khi print tiếng Việt trên Windows Console (đặc biệt là PowerShell/CMD)
if sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore


def bypass_videos_for_reup():
    configs = load_configs()
    videos = configs.get("videos", [])

    if not videos:
        print("Không có cấu hình video nào để xử lý.")
        return

    for idx, video in enumerate(videos, 1):
        print(f"\n[{idx}/{len(videos)}] Bắt đầu xử lý video...")

        # Đọc đường dẫn và chuyển đổi sang dạng đường dẫn tuyệt đối
        input_video = resolve_path(video.get("input_path"))
        output_video = resolve_path(video.get("output_path"))

        # Đọc thông số watermark
        logo_info = video.get("logo", {})
        x = logo_info.get("x")
        y = logo_info.get("y")
        w = logo_info.get("w")
        h = logo_info.get("h")

        try:
            editor = UnifiedReupBypasser(input_path=str(input_video))

            if x is not None and y is not None and w is not None and h is not None:
                editor.apply_remove_logo(x=x, y=y, w=w, h=h)

            # Áp dụng các kỹ thuật "Tác động trực tiếp vào khung hình (Visual Editing)" để né quét re-up
            editor.apply_mirror()
            editor.apply_zoom(zoom_percentage=10.0)  # Phóng to khoảng 3%
            editor.apply_speed(speed_factor=1.05)  # Thay đổi tốc độ một chút (1.05x)
            editor.apply_color_grading(
                brightness=0.02, contrast=1.02, saturation=1.05
            )  # Điều chỉnh màu sắc một chút

            # Đảm bảo thư mục đầu ra tồn tại
            output_video.parent.mkdir(parents=True, exist_ok=True)

            editor.export(output_path=str(output_video))
        except Exception as e:
            print(f"Lỗi khi xử lý video {input_video.name}: {e}")

    print(f"Đã xử lý xong {len(videos)} video")


if __name__ == "__main__":
    try:
        bypass_videos_for_reup()
    except Exception as ex:
        print(f"Chương trình bị gián đoạn, lỗi: {ex}")
