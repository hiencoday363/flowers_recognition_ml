 
import os
import shutil

# os.rename("./total_flowers", "./daisy")
# print(len(os.listdir("./daisy")))
# os.rename("./rose", "./total_flowers")
# shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

# li_folder = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

# for namefolder in li_folder:
# 	for item in os.listdir("./" + namefolder):
# 		base_path = './' + namefolder + '/' + item

# 		destination_path = './total_flowers' 
# 		# move to total_flowers
# 		try:
# 			shutil.move(base_path, destination_path)
# 		except Exception as e:
# 			print(e)
# 			continue
			
# 	print('done: '+namefolder)



# destination_path = './total_flowers' 

# shutil.move('./tulip/100930342_92e8746431_n.jpg', destination_path)

'''
check match
'''
count = 0
for total in os.listdir("./total_flowers"):
	filename, file_extension = os.path.splitext('./total_flowers/' + total)
	if file_extension != ".jpg":
		count += 1

print(f'count: {count}')

