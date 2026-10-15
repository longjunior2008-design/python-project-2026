import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# #1. Tạo frame (Dữ liệu của bạn)
data = {
    'Họ và tên': [
        'An',
        'Bình',
        'Chi',
        'Dung',
        'Hà',
        'Lan',
        'Minh',
        'Nam',
        'Phúc',
        'Trang',
    ],
    'Chuyên cần': [8.5, 9.0, 7.5, 8.0, 9.0, 6.5, 8.0, 7.0, 8.5, 9.5],
    'Giữa kỳ': [7.0, 8.0, 6.5, 7.5, 8.5, 5.5, 7.0, 6.0, 7.5, 8.0],
    'Cuối kỳ': [8.0, 8.5, 7.0, 8.0, 9.0, 6.0, 7.5, 6.5, 8.0, 9.0],
}

df = pd.DataFrame(data)

# #2. Tính điểm tổng kết
df['Tổng kết'] = (
    df['Chuyên cần'] * 0.2 + df['Giữa kỳ'] * 0.3 + df['Cuối kỳ'] * 0.5
)
df['Tổng kết'] = df['Tổng kết'].round(2)


# #3. Xếp loại
def xep_loai(diem):
  if diem >= 8.5:
    return 'Giỏi'
  elif diem >= 7.0:
    return 'Khá'
  elif diem >= 5.0:
    return 'Trung bình'
  else:
    return 'Yếu'


df['Xếp loại'] = df['Tổng kết'].apply(xep_loai)


# ================= GIAO DIỆN STREAMLIT =================
st.title('QUẢN LÝ ĐIỂM SINH VIÊN')  #[span_1](start_span)[span_1](end_span)

# Hiển thị bảng điểm
st.subheader('Bảng điểm 10 sinh viên')  #[span_2](start_span)[span_2](end_span)
st.dataframe(df)

# Thống kê kết quả học tập
st.subheader('Thống kê kết quả học tập')
dtb_lop = df['Tổng kết'].mean()
st.write(f'- *Điểm tổng kết trung bình của lớp:* {dtb_lop:.2f}')  #[span_3](start_span)[span_3](end_span)

max_sv = df.loc[df['Tổng kết'].idxmax()]
st.write(
    f"- *Sinh viên có điểm tổng kết cao nhất:* {max_sv['Họ và tên']} (Điểm:"
    f" {max_sv['Tổng kết']})"
)  #[span_4](start_span)[span_4](end_span)

min_sv = df.loc[df['Tổng kết'].idxmin()]
st.write(
    f"- *Sinh viên có điểm tổng kết thấp nhất:* {min_sv['Họ và tên']} (Điểm:"
    f" {min_sv['Tổng kết']})"
)  #[span_5](start_span)[span_5](end_span)

so_sv_dat = (df['Tổng kết'] >= 5.0).sum()
st.write(
    f'- *Số sinh viên đạt (điểm tổng kết >= 5.0):* {so_sv_dat} / {len(df)}'
)  #[span_6](start_span)[span_6](end_span)

# Danh sách xổ xuống chọn sinh viên
st.subheader('Tra cứu chi tiết sinh viên')
selected_name = st.selectbox(
    'Chọn tên sinh viên cần xem:', df['Họ và tên']
)  #[span_7](start_span)[span_7](end_span)
sv_info = df[df['Họ và tên'] == selected_name].iloc[0]

st.markdown(f"""
* *Họ và tên:* {sv_info['Họ và tên']}
* *Chuyên cần:* {sv_info['Chuyên cần']}
* *Giữa kỳ:* {sv_info['Giữa kỳ']}
* *Cuối kỳ:* {sv_info['Cuối kỳ']}
* *Điểm tổng kết:* {sv_info['Tổng kết']}
* *Xếp loại:* {sv_info['Xếp loại']}
""")  #[span_8](start_span)[span_8](end_span)

# Trực quan hóa biểu đồ Matplotlib
st.subheader('Biểu đồ cột điểm tổng kết của 10 sinh viên')  #[span_9](start_span)[span_9](end_span)
short_names = df['Họ và tên'].apply(lambda x: x.split()[-1])
scores = df['Tổng kết']

fig, ax = plt.subplots(figsize=(9, 5))
ax.barh(short_names, scores, color='#5B92E5')
ax.set_xlabel('Điểm tổng kết', fontsize=11)
ax.set_ylabel('Sinh viên', fontsize=11)
ax.set_title(
    'Biểu đồ cột thể hiện điểm tổng kết của 10 sinh viên',
    fontsize=12,
    fontweight='bold',
)
ax.invert_yaxis()
ax.grid(axis='x', linestyle='--', alpha=0.5)
st.pyplot(fig)

# Họ tên và MSSV ở cuối trang với kích thước chữ nhỏ
st.markdown(
    '<hr><p style="text-align: center; font-size: small; color: gray;">Người'
    ' tạo: Trần Văn Hoàng Long - MSSV: [Điền_MSSV_Của_Bạn]</p>',
    unsafe_allow_html=True,
)  #[span_10](start_span)[span_10](end_span)
