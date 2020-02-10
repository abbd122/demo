import os

from moviepy.editor import VideoFileClip

target_dir = r'/home/wangzheng/视频/Python分布式爬虫打造搜索引擎 Scrapy精讲/1/第3章 爬虫基础知识回顾'

movie_ext_list = ['.mp4', '.avi']


def task_run(dir_name, file):
    os.chdir(dir_name)
    clip = VideoFileClip(file)
    minutes = int(clip.duration // 60)
    path = os.path.join(dir_name, file)
    return path, minutes


def start():
    total_minutes = 0
    for root, dirs, files in os.walk(target_dir):
        if files:
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in movie_ext_list:
                    dir_name = root
                    path, minutes = task_run(dir_name, file)
                    print('{}:{}分钟'.format(path, minutes))
                    total_minutes += minutes
    total_hours = total_minutes // 60
    extra_minutes = total_minutes % 60
    print('共计{}小时{}分钟'.format(total_hours, extra_minutes))


if __name__ == '__main__':
    start()
