import os
import argparse

# 创建 ArgumentParser 对象
parser = argparse.ArgumentParser(description='Process some arguments.')

# 添加命令行参数
parser.add_argument('pure_name', type=str, help='无后缀文件名')

# 解析命令行参数
args = parser.parse_args()

# 访问参数值
pure_name = args.pure_name

def wav_to_pcm(wav_filename, pcm_filename):
    # WAV文件的头部信息通常占用44个字节
    header_size = 44

    try:
        # 以二进制读模式打开WAV文件
        with open(wav_filename, 'rb') as wav_file:
            # 跳过头部信息
            wav_file.seek(header_size)
            # 读取剩余的音频数据
            audio_data = wav_file.read()
            if os.path.exists(pcm_filename):
                os.remove(pcm_filename)
                print(f"已删除文件: {pcm_filename}")
            # 以二进制写模式创建PCM文件
            with open(pcm_filename, 'wb') as pcm_file:
                pcm_file.write(audio_data)
                
        print(f"转换完成，PCM文件已保存到：{pcm_filename}")
    except IOError as e:
        print(f"文件操作错误：{e}")

if __name__ == '__main__':
    # 使用函数，指定源WAV文件和目标PCM文件的路径
    wav_to_pcm(f'ffmpeg_8000_16{pure_name}.wav', f'ffmpeg_8000_16{pure_name}.pcm')