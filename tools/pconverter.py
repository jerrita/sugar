import os

# phigros 练习速度生成

name = 'pre.mp4'

so = f'ffmpeg -i {name} origin.mp4'
s5 = f'ffmpeg -i {name} -filter_complex "[0:v]setpts=2*PTS[v];[0:a]atempo=0.5[a]" -map "[v]" -map "[a]" 0-5.mp4'
s75 = f'ffmpeg -i {name} -filter_complex "[0:v]setpts=1.3333*PTS[v];[0:a]atempo=0.75[a]" -map "[v]" -map "[a]" 0-75.mp4'

for i in [so, s5, s75]:
    os.system(i)
