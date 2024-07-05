import re
import json
import tkinter as tk
import tkinter.font as tkFont
import tkinter.filedialog as filebox
import tkinter.messagebox as messagebox
from tkinter import ttk
import os
import webbrowser
import ctypes
import platform

useWindowsFix = platform.system().lower() == "windows"

if useWindowsFix:
    hWnd = ctypes.windll.user32.GetForegroundWindow()
    ctypes.windll.user32.ShowWindow(hWnd, 0)

window = tk.Tk()

# Just get the level data (inner string) from https://gdcolon.com/gdsave/
filename = "level"
output = "level.json"
prettyTk = tk.BooleanVar()
pretty = False # if false the output will be smaller

def object_to_dict(obj):
    objdict = {"glow": True}
    for proprety in obj:
        pid = int(proprety.split(",")[0])
        pv = proprety.split(",")[1]

        match pid:
            case 1: # ID
                objdict["id"] = int(pv)

            case 2: # X
                objdict["x"] = float(pv)

            case 3: # Y
                objdict["y"] = float(pv)

            case 4: # Flipped X?
                objdict["flipped_x"] = bool(pv)

            case 5: # Flipped Y?
                objdict["flipped_y"] = bool(pv)

            case 6: # Rotation
                objdict["rotation"] = float(pv)

            case 7: # Red
                objdict["red"] = int(pv)

            case 8: # Green
                objdict["green"] = int(pv)

            case 9: # Blue
                objdict["blue"] = int(pv)

            case 10: # Duration
                objdict["duration"] = float(pv)

            case 11: # Touch Triggered?
                objdict["touchTrigger"] = bool(pv)

            case 12: # Coin ID
                objdict["coinID"] = int(pv)

            case 13: # Checked?
                objdict["checked"] = bool(pv)

            case 14: # Tint Ground?
                objdict["tintGround"] = bool(pv)

            case 15: # Player Color 1
                objdict["pc1"] = bool(pv)

            case 16: # Player Color 2
                objdict["pc2"] = bool(pv)

            case 17: # Blending
                objdict["blending"] = bool(pv)

            case 19: # Legacy Color ID
                objdict["legacyChannel"] = int(pv)

            case 20: # Editor Layer 1
                objdict["editorLayer1"] = int(pv)

            case 21: # Main Color Channel
                objdict["mainChannel"] = int(pv)

            case 22: # Secondary Color Channel
                objdict["secondaryChannel"] = int(pv)

            case 23: # Target Color Channel
                objdict["targetChannel"] = int(pv)

            case 24: # Z Layer
                objdict["zlayer"] = int(pv)

            case 25: # Z Order
                objdict["zorder"] = int(pv)

            case 28: # Offset X
                objdict["offx"] = int(pv)

            case 29: # Offset Y
                objdict["offy"] = int(pv)

            case 30: # Easing
                objdict["easing"] = int(pv)

            case 31: # Text
                objdict["text"] = str(pv)

            case 32: # Scale
                objdict["scale"] = float(pv)

            case 33: # Single Group
                objdict["group"] = int(pv)

            case 34: # Group Parent
                objdict["groupParent"] = bool(pv)

            case 35: # Opacity
                objdict["opacity"] = float(pv)

            case 41: # Main HSV Enabled
                objdict["mainHsvEnabled"] = bool(pv)

            case 42: # Secondary HSV Enabled
                objdict["secondaryHsvEnabled"] = bool(pv)

            case 43: # Main HSV
                color = pv.split("a")
                fullColor = {"h": color[0], "s": color[1], "v": color[2], "sCheck": color[3], "vCheck": color[4]}
                objdict["mainHsv"] = fullColor

            case 44: # Secondary HSV
                color = pv.split("a")
                fullColor = {"h": color[0], "s": color[1], "v": color[2], "sCheck": color[3], "vCheck": color[4]}
                objdict["secondaryHsv"] = fullColor

            case 45: # Fade In
                objdict["fadeIn"] = float(pv)

            case 46: # Hold
                objdict["hold"] = float(pv)

            case 47: # Fade Out
                objdict["fadeOut"] = float(pv)

            case 48: # Pulse Mode
                objdict["pulseMode"] = int(pv)

            case 49: # Copied HSV
                color = pv.split("a")
                fullColor = {"h": color[0], "s": color[1], "v": color[2], "sCheck": color[3], "vCheck": color[4]}
                objdict["copiedHsv"] = fullColor

            case 50: # Copied Color ID
                objdict["copiedId"] = int(pv)

            case 51: # Target Group ID
                objdict["targetGroup"] = int(pv)

            case 52: # Pulse Target
                objdict["pulseTargetType"] = int(pv)

            case 54: # Portal Offset
                objdict["portalOffset"] = float(pv)

            case 55: # Portal Ease
                objdict["portalEase"] = bool(pv)

            case 56: # Activate Group
                objdict["activateGroup"] = bool(pv)

            case 57: # Groups
                groupsRaw = pv.split(".")
                groups = []

                for i in groupsRaw:
                    groups.append(int(i))

                objdict["groups"] = groups

            case 58: # Lock to Player X
                objdict["lockPlayerX"] = bool(pv)

            case 59: # Lock to Player Y
                objdict["lockPlayerY"] = bool(pv)

            case 60: # Copy Opacity
                objdict["copyOpacity"] = bool(pv)

            case 61: # Editor Layer 2
                objdict["editorLayer2"] = int(pv)

            case 62: # Spawn Triggered
                objdict["spawned"] = bool(pv)

            case 63: # Spawn Delay
                objdict["spawnDelay"] = float(pv)

            case 64: # Don't Fade
                objdict["dontFade"] = bool(pv)

            case 65: # Main Only
                objdict["mainOnly"] = bool(pv)

            case 66: # Detail Only
                objdict["detailOnly"] = bool(pv)

            case 67: # Don't Enter
                objdict["dontEnter"] = bool(pv)

            case 68: # Degrees
                objdict["rotTrigDegrees"] = int(pv)

            case 69: # Times 360
                objdict["times360"] = int(pv)

            case 70: # Lock Rotation
                objdict["lockRotation"] = bool(pv)

            case 71: # Secondary Group ID
                objdict["secondaryGroup"] = int(pv)

            case 72: # X Mod
                objdict["xMod"] = float(pv)

            case 73: # Y Mod
                objdict["yMod"] = float(pv)

            case 75: # Strength
                objdict["strength"] = float(pv)

            case 76: # Animation ID
                objdict["animation"] = int(pv)

            case 77: # Count
                objdict["count"] = int(pv)

            case 78: # Subtract Count
                objdict["subtract"] = bool(pv)

            case 79: # Pickup Mode
                objdict["pickupMode"] = int(pv)

            case 80: # Item ID
                objdict["itemID"] = int(pv)

            case 81: # Hold Mode
                objdict["holdMode"] = bool(pv)

            case 82: # Toggle Mode
                objdict["touchToggleMode"] = int(pv)

            case 84: # Interval
                objdict["interval"] = float(pv)

            case 85: # Easing Rate
                objdict["easeRate"] = float(pv)

            case 86: # Exclusive
                objdict["exclusive"] = bool(pv)

            case 87: # Multi Trigger
                objdict["multiTrigger"] = bool(pv)

            case 88: # Comparison
                objdict["instantComp"] = int(pv)

            case 89: # Touch Dual
                objdict["touchDual"] = bool(pv)

            case 90: # Speed
                objdict["fpySpeed"] = float(pv)

            case 91: # Follow Delay
                objdict["fpyDelay"] = float(pv)

            case 92: # Y Offset
                objdict["fpyOffset"] = float(pv)

            case 93: # Trigger On Exit
                objdict["triggerOnExit"] = bool(pv)

            case 94: # Dynamic Block
                objdict["dynamicBlock"] = bool(pv)

            case 95: # Block B ID
                objdict["blockB"] = int(pv)

            case 96: # Disable Glow
                objdict["glow"] = not bool(pv)

            case 97: # Custom Rotation Speed
                objdict["rotationSpeed"] = float(pv)

            case 98: # Disable Rotation
                objdict["disableRotation"] = bool(pv)

            case 99: # Multi Activate Orb
                objdict["multiActivate"] = bool(pv)

            case 100: # Enable Use Target
                objdict["useTarget"] = bool(pv)

            case 101: # Target Pos
                objdict["targetPos"] = int(pv)

            case 102: # Disable in Editor
                objdict["editDisable"] = bool(pv)

            case 103: # High Detail
                objdict["highDetail"] = bool(pv)

            case 104: # Multi Activate Trigger
                objdict["multiActivate"] = bool(pv)

            case 105: # Max Speed
                objdict["maxSpeed"] = float(pv)

            case 106: # Randomize Start
                objdict["randomizeStart"] = bool(pv)

            case 107: # Animation Speed
                objdict["animSpeed"] = float(pv)

            case 108: # Linked ID
                objdict["linkedID"] = int(pv)
        
    return objdict

def convert_it():
    global progressBar
    print("Reading...")

    with open(filename) as file:
        levelraw = file.read()

    levelraw = levelraw.split("|")[-1]
    splitlevel = levelraw.split(";")[1:]
    leveldata = []

    print("Splitting...")

    for i in splitlevel:
        if len(i) != 0:
            leveldata.append(re.findall("[^,]+,[^,]+", i))

    level = []

    print("Parsing...")

    for i in leveldata:
        level.append(object_to_dict(i))

    print("Encoding...")

    with open(output, "w") as file:
        if pretty:
            json.dump(level, file, sort_keys=True, indent=4)

        else:
            json.dump(level, file, sort_keys=False, indent=None, separators=None, default=None)

    print("Done!")
    messagebox.showinfo(window, message="Done!")

# ok here's the tk code lol

def select_file():
    global filename

    old_filename = filename

    try:
        new_filename = filebox.askopenfilename()
        relative_path = os.path.relpath(new_filename)
        filename = relative_path

    except:
        filename = old_filename

    filenameLabel.config(text = f"Loading from {filename}")

def select_outfile():
    global output

    old_filename = output

    try:
        new_filename = filebox.asksaveasfilename()
        relative_path = os.path.relpath(new_filename)
        output = relative_path

    except:
        output = old_filename

    outputFilenameEntryLabel.config(text = f"Saving to {output}")

def setPrettyValue():
    global pretty

    pretty = prettyTk.get()

def openColonWebsite():
    # i love gd cologne
    messagebox.showinfo(window, message="Opening a web browser. Upload %localappdata%\\GeometryDash\\CCLocalLevels.dat, extract the level you'd like, and use the \"Inner String\" option to save the level to your computer.")
    webbrowser.open("https://gdcolon.com/gdsave/")

window.title("GD2JSON")
window.geometry("600x580")

titleFont = tkFont.Font(font=("Roboto Bold", 64))
normalFont = tkFont.Font(font=("Roboto", 24))

titleLabel = tk.Label(window, text="GD2JSON", font=titleFont)
titleLabel.pack()

colonButton = tk.Button(window, text="EXTRACT YOUR LEVEL!!!", font=normalFont, command=openColonWebsite)
colonButton.pack()

filenameLabel = tk.Label(window, text=f"Loading from {filename}", font=normalFont)
filenameLabel.pack()

selectFileButton = tk.Button(window, text="Select a different file", font=normalFont, command=select_file)
selectFileButton.pack()

outputFilenameEntryLabel = tk.Label(window, text=f"Saving to {output}", font=normalFont)
outputFilenameEntryLabel.pack()

outputFilenameEntrySubmit = tk.Button(window, text="Change output", font=normalFont, command=select_outfile)
outputFilenameEntrySubmit.pack()

prettyToggle = tk.Checkbutton(window, text="Beautify output?", variable=prettyTk, onvalue=True, offvalue=False, command=setPrettyValue, font=normalFont)
prettyToggle.pack()

prettyInfo = tk.Label(window, text="If off, the output will be smaller.", font=normalFont)
prettyInfo.pack()

runButton = tk.Button(window, text="Convert!", font=normalFont, command=convert_it)
runButton.pack()

window.mainloop()
