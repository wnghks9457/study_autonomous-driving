import geopandas as gpd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = 'NanumGothic' # 한글 폰트
plt.rcParams["figure.figsize"] = (10, 10)

# 파일 읽기(read file)
korea_file = "C:\github\hdmap_korea\ctp_rvn.shp"
korea = gpd.read_file(korea_file)
korea

ax = korea.convex_hull.plot(color = 'purple', edgecolor = 'w')
ax.set_title("대한민국")
ax.set_axis_off() # 축제거
plt.show()