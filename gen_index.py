import os

def list_markdown_files(directory):
    files_list = []
    for root, dirs, files in os.walk(directory):
        # 过滤出当前目录的 Markdown 文件
        markdown_files = [f for f in files if f.endswith('.md')]
        if markdown_files:
            # 添加目录名
            directory_name = os.path.relpath(root, directory)
            files_list.append(f"- {directory_name}:")
            # 添加文件列表
            for file in markdown_files:
                files_list.append(f"    - {file.split('.')[0]}：{file}")

    return files_list

def main():
    # 指定你的目录路径
    directory_path = '/home/laodu/notes/github.notes/docs/'
    
    # 获取 Markdown 文件列表
    files_list = list_markdown_files(directory_path)
    
    # 打印结果
    for line in files_list:
        if line.startswith(directory_path):
            print(line)
        else:
            print(line)

if __name__ == "__main__":
    main()
