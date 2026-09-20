import time
import streamlit as st

# Cấu hình giao diện Streamlit
st.set_page_config(page_title="Karaoke Lyrics", page_icon="🎵", layout="centered")

st.title("2AM")
st.title("JustaTee ft. BigDaddy")
# Bảng mã màu HTML
MAU = {
    "xanh_ngoc": "#00FFFF",
    "vang": "#FFD700",
    "xanh_la": "#00FF7F",
    "do": "#FF4500",
    "hong": "#FF69B4",
    "tim": "#BA55D3",
    "xanh_duong": "#1E90FF",
}

# Danh sách bài hát giữ nguyên 100% chữ, thời gian và màu sắc
lyrics = [
    ("ANH TRONG THEO ĐÓ", 1, "xanh_ngoc"),
    ("ĐÂY", 0.7, "vang"),
    ("NHƯNG SAO CHẲNG", 1.3, "xanh_la"),
    ("THẤY", 0.7, "do"),
    ("NHỮNG DẤU SON CÒN TƯƠI", 1.7, "hong"),
    ("TRÊN MÔI HỒNG EM,TỪ NGÀY EM ĐI", 1.8, "tim"),
    ("KHI BAO NHIÊU KHÓ", 1.2, "xanh_duong"),
    ("KHĂN", 0.4, "do"),
    ("BÊN ANH NHIỀU", 0.9, "vang"),
    ("LẮM", 0.8, "hong"),
    ("EM NÓI EM SẼ VỀ ĐÂY KHI", 2, "xanh_ngoc"),
    ("MÙA ĐÔNG TÀN", 0.8, "xanh_la"),
]

# Nút Bắt đầu phát lời
if st.button(" Bắt đầu chạy lời", type="primary"):
    for text, total_time, color in lyrics:
        line_placeholder = st.empty()
        color_code = MAU.get(color, "#FFFFFF")
        speed = total_time / len(text)

        current_text = ""
        for char in text:
            current_text += char
            # Hiển thị chữ nổi bật với phông to chuẩn Karaoke
            line_placeholder.markdown(
                f'<p style="color: {color_code}; font-size: 28px; font-weight: bold; margin: 6px 0;">{current_text}</p>',
                unsafe_allow_html=True,
            )
            time.sleep(speed)