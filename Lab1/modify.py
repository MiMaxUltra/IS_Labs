import os

def flip_bit_in_file(file_path, position, bit_position):
    # 打开文件读取二进制内容
    with open(file_path, 'rb') as f:
        content = bytearray(f.read())

    # 获取要修改的字节
    byte_value = content[position]

    # 计算比特掩码
    mask = 1 << (7 - bit_position)

    # 反转目标比特位
    new_byte_value = byte_value ^ mask

    # 更新字节数组
    content[position] = new_byte_value

    # 构建新的文件名
    base_name = os.path.splitext(file_path)[0]
    new_file_path = f"{base_name}_modified{os.path.splitext(file_path)[1]}"

    # 写回文件
    with open(new_file_path, 'wb') as f:
        f.write(content)

# 文件路径，假设文件名分别为 'plain_1000bytes-ecb.bin', 'plain_1000bytes-cbc.bin', 'plain_1000bytes-cfb.bin', 'plain_1000bytes-ofb.bin' 并位于根目录下
files = [
    'plain_1000bytes-ecb.bin',
    'plain_1000bytes-cbc.bin',
    'plain_1000bytes-cfb.bin',
    'plain_1000bytes-ofb.bin'
]

# 修改的位置和比特位
position = 54  # 索引从0开始，因此第55个字节是位置54
bit_position = 0  # 第1个比特位是从0开始计数的

# 对每个文件进行修改
for file_path in files:
    print(f"Modifying {file_path}...")
    flip_bit_in_file(file_path, position, bit_position)
    print(f"Modified file saved as {file_path}_modified")