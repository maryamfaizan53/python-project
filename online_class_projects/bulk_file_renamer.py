# import os

# def main():
#     i = 0
#     path = "c:/Users/LENOVO/Documents/"

#     if not os.path.exists(path):
#         print("Error: Path does not exist.")
#         return

#     for filename in os.listdir(path):
#         # Filter only image files (JPG, JPEG, PNG)
#         if filename.lower().endswith(('.jpg', '.jpeg', '.png')):  
#             my_source = os.path.join(path, filename)
#             my_dest = os.path.join(path, f"image{i}.jpg")

#             os.rename(my_source, my_dest)
#             print(f"Renamed {filename} -> image{i}.jpg")

#             i += 1

# if __name__ == "__main__":
#     main()
import os
import streamlit as st
from pathlib import Path
import shutil

# Streamlit UI
st.title("📂 Image Renamer App")
st.write("Upload a folder with images, and rename them sequentially!")

# Select directory
folder_path = st.text_input("Enter the folder path:", "")

# Button to load files
if st.button("Load Images"):
    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        if files:
            st.success(f"Found {len(files)} images.")
            st.session_state['files'] = files
        else:
            st.warning("No images found in the folder!")
    else:
        st.error("Invalid folder path. Please enter a correct path.")

# Show images and rename
if 'files' in st.session_state:
    files = st.session_state['files']
    renamed_files = []
    
    # Preview images
    for i, file in enumerate(files):
        file_path = os.path.join(folder_path, file)
        st.image(file_path, caption=file, width=200)

    if st.button("Rename Images"):
        for i, file in enumerate(files):
            old_path = os.path.join(folder_path, file)
            new_name = f"image{i}.jpg"
            new_path = os.path.join(folder_path, new_name)

            os.rename(old_path, new_path)
            renamed_files.append(new_name)

        st.success("Images renamed successfully!")
        st.write("Renamed Files:")
        st.write(renamed_files)
        st.balloons()