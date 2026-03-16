# About
This repo contains an arduino sketch and a python-based web server to convert REST requests into IR/RF commands for an RC toy. These components let a user control an RC toy from their PC or (the main target) a Grid 3 gridset, making RC toys accessible to a wider audience.


# Components
This repo consists of the following components:
* `grid3_remote/` - arduino sketch  
* `main/` - python web server  
* `installer/` - preprocessing steps to find the installation path/cwd and add it to a grid3 gridset as needed.  
* `sources/` - grid3 resources including a templated gridset (needs to know the absolute path to send_command.vbs) and a vbs script to send commands to the python web server  


# Developer notes
The installer step is only necessary if we don't know the path of the vbs or other resources in advance. I didn't want to jump the gun and copy these files to a known absolute path like `Program files (x86)` in advance.

Installer and main were both run inside their own python virtual environments. Use the bundled requirements files to recreate these envs with the following commands:  
```
python -m venv venv
pip install -r requirements.txt
```

The installer and main were made portable across windows x86/64 systems using `pyinstaller`. The included `build.ps1` script goes through the full set of build steps on a windows PC to generate an installer and web server as `.exe` executables and bundles in resources/readme. The output of this script is an /output directory (originally shared on USB) that has been committed here too for anyone who wants to skip to the good part.

The arduino sketch was written to be installed on an arduino nano or RP2040, with the intention of emulating button presses on a remote by being wired into a circuit and pulling pins high/low. In two initial remotes, the arduino needed to pull pins low for ~200ms to be read as a usual button press.

The two circuits this was tested on consisted of an arduino nano for a remote that was 5V tolerant and RP2040 for 3.3V.

Hardware-wise, the next steps could be:  
* Adding a logic-level converter and using the same MCU for any remote
* Connecting an IR LED or RF transmitter directly to the MCU to generate some "universal" RC toy controller. Note: this is plausible for IR or old RF devices, but 2.4GHz devices try hard to prevent interference/crosstalk from arbitrary remotes
* Use the same MCU and a standardised GPIO layout/header so remotes can be plug and play 


# Authors
* [Marc Katzef](mailto:marckatzef@gmail.com) - feel free to reach out


# Repo
[https://github.com/mkatzef/accessible_rc_remote](https://github.com/mkatzef/accessible_rc_remote)