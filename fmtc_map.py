import geopandas as gpd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = 'NanumGothic' # 한글 폰트
plt.rcParams["figure.figsize"] = (10, 10)

# 파일 읽기(read file)
fmtc_file = "C:/github/fmtc_hdmap/A1_LANE.shp"
fmtc = gpd.read_file(fmtc_file)
fmtc

ax = fmtc.convex_hull.plot(color = 'purple', edgecolor = 'w')
ax.set_title("FMTC")
ax.set_axis_off() # 축제거
plt.show()