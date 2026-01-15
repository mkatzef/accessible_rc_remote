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

grid_resources = 'grid_resources.zip'
extracted_files = 'grid_resources'
output_file = 'RC Grid.zip'
output_file_final = 'RC Grid.gridset'

print("=" * 80)
print("Preparing an importable grid")
print("=" * 80)
print()

print(f"Extracting {grid_resources} to {extracted_files}...")
os.makedirs(extracted_files, exist_ok=True)
with zipfile.ZipFile(grid_resources, 'r') as zip_ref:
    zip_ref.extractall(extracted_files)
print("Done!\n")

print(f"Configuring files to point to the scripts stored here (in {os.getcwd()})...")
print(os.getcwd())
print("Done!\n")

print(f"Packaging files up as {output_file}...")
shutil.make_archive(output_file.replace('.zip', ''), 'zip', extracted_files)
os.move(output_file, output_file_final)
print("Done!\n")

#print(f"Removing temporary files from...")
#shutil.rmtree(extracted_files)

print("=" * 80)
print("Completed successfully!")
print(f"Please import the grid named {output_file}")
print("=" * 80)
print("\n")

input("Press any key to exit...")
