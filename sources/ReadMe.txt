# About
These files add support for controlling an RC toy using a connected arduino circuit from a Grid 3 gridset.


# Contents
The files in this folder are:
 * installer.exe - An executable file that prepares a Grid3 grid for you
 * resources.zip - Code and a template gridset for you to add to Grid 3
 * ReadMe.txt - Instructions (this file)


# Installation
1. Copy the files listed in Contents onto your computer somewhere they can stay (e.g. in a new folder "Documents/RC Controller")
2. Double-click on the file "installer.exe" - you should see a terminal window pop up saying that it successfully generated a grid
3. Open Grid 3 and select a user to login as
4. Double-click on the generated gridset "RC Grid.gridset" (from step 2) to add it to Grid 3


# Usage
1. In Grid 3, open the gridset you generated above
2. Connect an RC controller circuit (one of the black boxes) using a USB-A to USB-C cable that can transfer data (Note: some USB-C cables only work for charging devices)
3. Click on "Connect" in the Grid 3 grid - a black window should pop up telling you if it can connect successfully
4. The buttons are ready to use


# Customization
Each Grid 3 button is configured to send a command to the connected arduino circuit, which has been programmed to listen for instructions.

The instruction must be one of the following:
## Pressing a button
Format: press_[button A]-[duration in milliseconds]_[button B]-[duration]...
E.g. "press_1-1000" to press button 1 for 1000 milliseconds (1 second)
Or, "press_2-100_3-100" to press and hold two buttons at the same time for 100 ms.

Optionally, use a duration of -1 to hold the button indefinitely
E.g. "press_2--1" Note the double '-'

## Releasing a button
Format: release_[button A]_[button B]...
E.g. "release_2_3"
Similar to pressing a button but without the need for a duration

## Extending/shortening a button press duration
Format: mult_[multiplier]
E.g. "mult_2.5" to multiply any subsequent button press duration by 2.5 (e.g. turn a 100 ms button press into a 250 ms button press)
This is useful for fine-tuning how long 


## Button numbers
Both controllers in the initial version only have 4 buttons each. These buttons have been numbered clockwise as follows:
1: Forward
2: Right
3: Back
4: Left
