
mkdir output -Force > $null

cd main
.\venv\Scripts\activate
#pyinstaller -F main.py
deactivate
cd ..
cp main/dist/main.exe output/

cd installer
.\venv\Scripts\activate
#pyinstaller -F installer.py
deactivate
cd ..
cp installer/dist/installer.exe output/


