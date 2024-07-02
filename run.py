from PIL import Image
import os

while True:
    folder_path = input('輸入資料夾路徑: ')

    if not os.path.exists(folder_path):
        print('請輸入有效路徑。')
    else:
        break

for image in os.listdir(folder_path):
    image_path = os.path.join(folder_path, image)

    try:
        im = Image.open(image_path)
        im2 = im.crop(im.getbbox())
        im2.save(image_path)

        print(f'成功裁切 {image_path}。')
    except Exception as e:
        print(f'錯誤，跳過 {image_path} - {e}')