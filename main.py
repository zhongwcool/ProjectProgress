import os
import sys
import time

# Unicode 块字符
BLOCK_CHARS = ['█', '▉', '▊', '▋', '▌', '▍', '▎', '▏']


def countdown_progress_bar_decreasing_smooth2(total_duration, bar_length=40, direction='left_to_right'):
    def _print_progress_bar(remaining):
        # 计算剩余时间比例
        progress_ratio = remaining / total_duration
        # 全块进度块的个数
        full_blocks = int(progress_ratio * bar_length)
        # 确定进度条中剩余部分所用的Unicode字符的索引
        partial_block_index = int((progress_ratio * bar_length - full_blocks) * len(BLOCK_CHARS))
        # 初始化进度条为空字符串
        bar = ''
        # 根据方向构建进度条
        if direction == 'left_to_right':
            # 进度从右往左消失
            bar += BLOCK_CHARS[0] * full_blocks
            if full_blocks < bar_length:
                bar += BLOCK_CHARS[partial_block_index]
            bar += ' ' * (bar_length - full_blocks - 1)
        elif direction == 'right_to_left':
            # 顺滑消失在右侧的效果
            bar = ' ' * (bar_length - full_blocks - 1)
            if full_blocks < bar_length:
                bar = BLOCK_CHARS[7 - partial_block_index] + bar
            bar = BLOCK_CHARS[0] * full_blocks + bar
        # 剩余时间的秒数
        time_str = f'{int(remaining):02d}s'
        sys.stdout.write(f'\r[{bar}] {time_str} remaining')
        sys.stdout.flush()

    start_time = time.time()
    _print_progress_bar(total_duration)
    # 一直倒计时直到时间为0
    while True:
        elapsed_time = time.time() - start_time
        remaining_time = total_duration - elapsed_time
        if remaining_time <= 0:
            break
        _print_progress_bar(remaining_time)
        time.sleep(0.1)  # Update at a rate of ten times per second.

    # 倒计时结束时确保进度条是空的，并打印信息
    _print_progress_bar(0)
    sys.stdout.write('\rDone!\n')


def countdown_progress_bar(total_time):
    bar_length = 40  # Modify this to change the length of the progress bar
    block = '█'  # block character
    sys.stdout.write('\n')  # Start on a new line

    for i in range(total_time, 0, -1):
        filled_length = int(bar_length * i // total_time)
        bar = ' ' * (bar_length - filled_length) + block * filled_length
        sys.stdout.write('\r[{0}] {1}s'.format(bar, i))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write('\rTime is up!          \n')  # Clear the progress bar


def print_hi(file_path):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {file_path}')  # Press Ctrl+F8 to toggle the breakpoint.

    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        total_duration = 20  # 10 seconds duration for the progress bar
        countdown_progress_bar(total_duration)
        print("\nright_to_left:")
        countdown_progress_bar_decreasing_smooth2(total_duration, direction='right_to_left')
    else:
        # 获取版本号
        total_duration = 20  # 10 seconds duration for the progress bar
        print("\nleft_to_right:")
        countdown_progress_bar_decreasing_smooth2(total_duration, direction='left_to_right')
        print("\nDone.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('hello.exe')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
