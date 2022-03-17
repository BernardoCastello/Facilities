import os

def main():
   
    folder = "IMG"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"{str(count+1).zfill(5)}.png"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)


if __name__ == '__main__':
     
    # Calling main() function
    main()