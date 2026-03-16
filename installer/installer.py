"""
Prepares a grid config that can be imported into Grid 3

The main purpose of this file is to lookup where the external scripts
are being stored so that the grid config points to the right paths

"""

import os
import sys
import zipfile
import shutil
import time

all_resources = 'resources.zip'
all_resources_files = 'resources - dont delete'
grid_resources = f'{all_resources_files}/Controller.zip'
extracted_files = f'{all_resources_files}/Controller'
file_to_edit = f'{all_resources_files}/Controller/Grids/RC Controller/grid.xml'
output_file = 'RC Grid.zip'
output_file_final = 'RC Grid.gridset'

PATH_VAR = '$APP_BASE_PATH$'

print("=" * 80)
print("Preparing an importable grid")
print("=" * 80)
print()

print(f"Extracting {all_resources} to {all_resources_files}...")
os.makedirs(all_resources_files, exist_ok=True)
with zipfile.ZipFile(all_resources, 'r') as zip_ref:
    zip_ref.extractall(all_resources_files)
print("Done!\n")

print(f"Extracting {grid_resources} to {extracted_files}...")
os.makedirs(extracted_files, exist_ok=True)
with zipfile.ZipFile(grid_resources, 'r') as zip_ref:
    zip_ref.extractall(extracted_files)
print("Done!\n")

print(f"Configuring files to point to the scripts stored here (in {os.getcwd()})...")
res_dir = os.path.join(os.getcwd(), all_resources_files).strip('/').strip('\\')
intext = ""
with open(file_to_edit, 'r') as infile:
    intext = infile.read()
with open(file_to_edit, 'w') as outfile:
    outfile.write(intext.replace(PATH_VAR, res_dir))

print("Done!\n")

print(f"Packaging files up as {output_file}...")
shutil.make_archive(output_file.replace('.zip', ''), 'zip', extracted_files)
shutil.move(output_file, output_file_final)
print("Done!\n")

print(f"Removing temporary files from...")
shutil.rmtree(extracted_files)
print("Done!\n")

print("=" * 80)
print("Completed successfully!")
print(f"Please import the grid named {output_file}")
print("=" * 80)
print("\n")

input("Press any key to exit...")
