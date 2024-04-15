
# i have some files with names like this: Screenshot 2024-04-11 122137.png, i need to change them to zelda1.png til the last file, 
# write me the python code

# import os
# import re

# def rename_wechat_files(directory):
#     """Renames WeChat files in the specified directory to 'girlx.mp4' with sequential numbering.

#     Args:
#         directory (str): The path to the directory containing the WeChat files.
#     """

#     girl_count = 1
#     for filename in os.listdir(directory):
#         if filename.startswith("Screenshot") and filename.endswith(".png"):
#             # Extract the timestamp from the filename
#             timestamp_match = re.search(r'\d{14}', filename)
#             if timestamp_match:
#                 new_filename = f"zelda{girl_count}.png"
#                 old_filepath = os.path.join(directory, filename)
#                 new_filepath = os.path.join(directory, new_filename)
#                 os.rename(old_filepath, new_filepath)
#                 girl_count += 1

# # Specify your directory containing the WeChat files
# directory = "E:\CYAI\images\Zelda"  # Example: "C:/Users/YourName/Downloads"

# print("Files renamed successfully!")

# # Call the function to rename files
# rename_wechat_files(directory)


# import os

# def rename_files(directory):
#     # Get a list of all files in the directory
#     files = os.listdir(directory)

#     # Counter for generating new file names
#     counter = 128

#     # Iterate through each file
#     for filename in files:
#         # Check if the file is a PNG image
#         if filename.endswith('.png') and filename.startswith("ll"):
#             # Generate the new file name
#             new_filename = f'season_resized{counter}.png'

#             # Construct the full path of the file
#             old_path = os.path.join(directory, filename)
#             new_path = os.path.join(directory, new_filename)

#             # Rename the file
#             os.rename(old_path, new_path)

#             # Increment counter for the next file
#             counter += 1

# # Specify the directory containing the files
# directory = 'E:\CYAI\images\season_resized'

# print("Files renamed successfully!")

# # Call the function to rename files
# rename_files(directory)



# import os

# directory = "e:\CYAI\images\Zelda"

# print("Directory exists:", os.path.exists(directory))

# try:
#     for season_number in range(28, 49):
#         filename = f"zelda{season_number}.txt"
#         filepath = os.path.join(directory, filename)

#         print("Creating file:", filepath)

#         with open(filepath, 'w') as file:
#             pass 

#     print("Files created successfully!")

# except Exception as e:
#     print("An error occurred:", e)


# import os
# import glob

# def rename_files(directory):
#     # Get a list of all files in the directory
#     files = glob.glob(os.path.join(directory, '*.mp4'))

#     # Sort files based on creation time
#     files.sort(key=os.path.getctime)

#     # Counter for generating new file names
#     counter = 189

#     # Iterate through each file
#     for filename in files:
#         # Check if the file name length is more than 20 characters
#         if len(os.path.basename(filename)) > 20 and filename.endswith('.mp4'):
#             # Generate the new file name
#             new_filename = f'season_RS{counter}.mp4'

#             # Construct the full path of the file
#             old_path = filename
#             new_path = os.path.join(directory, new_filename)

#             # Rename the file
#             os.rename(old_path, new_path)

#             # Increment counter for the next file
#             counter += 1

# # Specify the directory containing the files
# directory = 'E:\CYAI\images\season_resized'

# print("Files renamed successfully!")

# # Call the function to rename files
# rename_files(directory)
