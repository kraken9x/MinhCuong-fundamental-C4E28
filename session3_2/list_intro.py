#Vòng lặp While -> thực hiện chương trình khi không biết trước số lần lặp
#Sau while là 1 điều kiện

count = 0

# while True:
#     print("Running !!!!")

#-> in ra vô hạn lần
#Kiểm soát vòng lặp while bằng cách

# while count < 3:
#     print("Running")
# => chạy vô hạn vì count luôn đúng
# => sau mỗi lần print thì cho count tăng lên 1 => chương trình chỉ chạy 3 lần

# count += 1

#Cách kiểm soát vòng lặp số 2:
#Dùng biến trạng thái
loop = True #flag = True

# while loop and count < 5:
#     print("Running!!!")
#     count += 1

# while loop:
#     print("Running")
#     count += 1
#     if count == 5:
#         loop = False

# while loop:
#     print("Running")
#     count += 1
#     if count == 5:
#         break

#KHI GẶP TỪ KHÓA "break" thì sẽ dừng luôn vòng lặp và không quan tâm code ở bên dưới như thế nào
#KHI DÙNG biến trạng thái thì code bên dưới false vẫn sẽ chạy
# while loop:
#     print("Running")
#     count += 1
#     if count == 5:
#         break
#         print("Bye")
#Không in ra từ bye


while loop:
    print("Running")
    count += 1
    if count == 5:
        loop = False
        print("Bye")