import os

def delete_files_by_extension(folder_path, extension):
    files = os.listdir(folder_path)
    for file in files:
        if file.endswith(extension):
            file_path = os.path.join(folder_path, file)
            os.remove(file_path)
            print(f"Deleted {file}")iles
    if new_path.exists():
        print(f"Skipping {item.name}, target {new_name} already exists.")
        continue
    
    try:
        shutil.move(item, new_path)
    except Exception as e:
        print(f"Error renaming {item.name}: {e}")

print("Files renaming completed.")