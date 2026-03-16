Remove-Item -Path "output" -Recurse -Force
mkdir output > $null

cd installer
.\venv\Scripts\activate
pyinstaller -F installer.py
deactivate
cd ..
cp installer/dist/installer.exe output/

mkdir output/resources -Force > $null

cp "sources/RC Controller.gridset" output/resources/Controller.zip
cp "sources/send_command.vbs" output/resources/send_command.vbs
cp "sources/ReadMe.txt" output/resources/ReadMe.txt

cd main
.\venv\Scripts\activate
pyinstaller -F main.py
deactivate
cd ..
cp main/dist/main.exe output/resources/main.exe

cd output
Compress-Archive -Path "resources/*" -DestinationPath "resources.zip" -Force
Remove-Item -Path "resources" -Recurse -Force
cd ..
