from html2image import Html2Image
import shutil
import download

hti = Html2Image()
files = [
   "index_1.html", "index_2.html"
]
files_sorted = sorted(files)

folder_path = str(input("Enter the PATH of the projecto to save the images you want to build: \n>> "))

for file in files:
    image_name = f"image_{file.replace('.html', '')}.jpg"
    print(file + "->" + image_name)
    hti.screenshot(
        html_file=file, css_file='style.css', save_as=image_name
    )
    src_path = image_name
    dst_path = rf"{folder_path}\{image_name}"
    print("Moved :" + image_name)
    shutil.move(src_path, dst_path)

# Download Musica
download_musica = download.download_music(folder_path)
