# 复制目标目录下所有指定的文件到存储目录

import re
import os
import shutil

target_dir = "G:/Programming/VS/C++/C++ Primer Plus/"  # 目标目录
filename_extension = ".cpp"  # 文件扩展名
save_dir = target_dir + "src/"  # 存储目录

# 判断目标目录是否存在
if not os.path.isdir(target_dir):
	print("目标目录不存在！！")
else:
	# 清理存储目录并重新创建存储目录
	if not os.path.isdir(save_dir):
		# 创建存储目录
		print("存储目录不存在，正在创建...")
		os.mkdir(save_dir)
		print("创建完成！")
		print("-----------------------------------------------")
	else:
		# 清理存储目录
		print("正在清理存储目录..")
		shutil.rmtree(save_dir)
		print("清理完成！")
		print("-----------------------------------------------")

		# 创建存储目录
		print("正在创建...")
		os.mkdir(save_dir)
		print("创建完成！")
		print("-----------------------------------------------")
	
	# 复制目标目录下的指定的所有文件到存储目录
	for parent, dirnames, filenames in os.walk(target_dir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
		for filename in filenames:  # 输出文件信息
			# print("parent is:" + parent)
			if re.search(filename_extension + "$", filename):
				print("发现指定文件：")
				print(os.path.join(parent, filename))  # 输出文件路径信息

				# 判断文件是否已经存在存储目录下
				if not os.path.isfile(os.path.join(save_dir, filename)):
					print("正在复制 " + filename + " 到 " + save_dir + "...")
					shutil.copy(os.path.join(parent,filename),os.path.join(save_dir,filename))
					print("复制完成！")
					print("-----------------------------------------------")