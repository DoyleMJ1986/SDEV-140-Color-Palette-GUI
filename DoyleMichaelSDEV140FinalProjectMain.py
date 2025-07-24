"""
Author: Michael Doyle
File Name: SDEV 140 Final Project Main
Description: The main program module for the color palette GUI application. Takes the definitions laid out in
DoyleMichaelSDEV140FinalProjectClasses.py and puts them to work, depending on user interactions.
"""
# Tkinter is main GUI interface resource library
import tkinter as tk
# import PIL library for insertion of JPG and/or PNG files into the window elements
from PIL import ImageTk, Image

# The class which contains all objects necessary for program execution and operation
class ColorPaletteApp(tk.Tk):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (tk.Tk)"""
        self.title("Color Palette Accessor and Mutator Suite")
        self.geometry("1200x1200")
        self.configure(bg="#a8e4a0")
        # Red Component
        self.redLabel = tk.Label(self, text="Red Value", fg="red")
        self.redLabel.configure(bg="#a8e4a0")
        self.redLabel.grid(row=0, column=0, sticky="nsew")
        self.redEntryLabel = tk.Label(self, text="Enter Red Value Here")
        self.redEntryLabel.grid(row=1, column=0, sticky="nsew")
        self.redEntry = tk.Entry(self, state = "normal")
        self.redEntry.grid(row=2, column=0, sticky="nsew")
        self.redEntryButton = tk.Button(self, text="Set Red", command=self.setRed)
        self.redEntryButton.grid(row=3, column=0, sticky="nsew")
        self.redSlider = tk.Scale(self, from_=0, to=255, orient="horizontal", command=self.calculateRGB)
        self.redSlider.configure(bg="#a8e4a0")
        self.redSlider.grid(row=4, column=0, sticky="nsew")

        # Green Component
        self.greenLabel = tk.Label(self, text="Green Value", fg="green")
        self.greenLabel.grid(row=0, column=1, sticky="nsew")
        self.greenLabel.configure(bg="#a8e4a0")
        self.greenEntryLabel =tk.Label(self, text="Enter Green Value Here")
        self.greenEntryLabel.grid(row=1, column=1, sticky="nsew")
        self.greenEntry = tk.Entry(self, state = "normal")
        self.greenEntry.grid(row=2, column=1, sticky="nsew")
        self.greenEntryButton = tk.Button(self, text="Set Green", command=self.setGreen)
        self.greenEntryButton.grid(row=3, column=1, sticky="nsew")
        self.greenSlider = tk.Scale(self, from_=0, to=255, orient='horizontal', command=self.calculateRGB)
        self.greenSlider.configure(bg="#a8e4a0")
        self.greenSlider.grid(row=4, column=1, sticky="nsew")

        # Blue Component
        self.blueLabel = tk.Label(self, text="Blue Value", fg="blue")
        self.blueLabel.grid(row=0, column=2, sticky="nsew")
        self.blueEntryLabel = tk.Label(self, text="Enter Blue Value Here")
        self.blueEntryLabel.grid(row=1, column=2, sticky="nsew")
        self.blueEntry = tk.Entry(self, state = "normal")
        self.blueEntry.grid(row=2, column=2, sticky="nsew")
        self.blueEntrybutton = tk.Button(self, text="Set Blue", command=self.setBlue)
        self.blueEntrybutton.grid(row=3, column=2, sticky="nsew")
        self.blueSlider = tk.Scale(self, from_=0, to=255, orient='horizontal', command=self.calculateRGB)
        self.blueSlider.grid(row=4, column=2, sticky="nsew")

        # Color Display Canvas
        self.canvasLabel = tk.Label(self, text="Curent Color")
        self.canvasLabel.grid(row=5, column=5, sticky="nsew")
        self.myCanvas = tk.Canvas(self, width=100, height=100, background="black")
        self.myCanvas.grid(row=6, column=5, sticky="nsew")

        # RGB Code Display
        self.rgbLabel = tk.Label(self, text="RGB Value")
        self.rgbLabel.grid(row=10, column=5, sticky="nsew")
        self.rgbD = tk.Entry(self, state="readonly")
        self.rgbD.configure(bg="white")
        self.rgbD.grid(row=11, column=5, sticky="nsew")
        # RGB Copy Button
        self.cpyRGB = tk.Button(self, text= "Copy Code", command=self.copyRGB)
        self.cpyRGB.grid(row=12, column=5, sticky="nsew")

        # HSV Code Display
        self.hsvLabel = tk.Label(self, text="HSV Value")
        self.hsvLabel.grid(row=13, column=5, sticky="nsew")
        self.hsvD = tk.Entry(self, state="readonly")
        self.hsvD.configure(bg="white")
        self.hsvD.grid(row=13, column=5, sticky="nsew")
        # HSV Copy Button
        self.hsvCpy = tk.Button(self, text= "Copy Code", command=self.copyHSV)
        self.hsvCpy.configure(bg="white")
        self.hsvCpy.grid(row=14, column=5, sticky="nsew")

        # CYMK Code Display
        self.cymkLabel = tk.Label(self, text="CYMK Value")
        self.cymkLabel.grid(row=15, column=5, sticky="nsew")
        self.cymkD = tk.Entry(self, state="readonly")
        self.cymkD.configure(bg="white")
        self.cymkD.grid(row=16, column=5, sticky="nsew")
        #CYMK Clipboard Copy Button
        self.cymkCpy = tk.Button(self, text="Copy Code", command=self.copyCYMK)
        self.cymkCpy.configure(bg="white")
        self.cymkCpy.grid(row=17, column=5, sticky="nsew")
        # RGB Inverter Button
        self.RGBInvLabel = tk.Label(self, text="RGB Value Invert")
        self.RGBInvLabel.grid(row=18, column=5, sticky="nsew")
        # HSV Interver Button
        self.HSVInvLabel = tk.Label(self, text="HSV Value Invert")
        self.HSVInvLabel.grid(row=19, column=5, sticky="nsew")
        # CYMK Inverter Button
        self.CYMKInvLabel = tk.Label(self, text="CYMK Value Invert")
        self.CYMKInvLabel.grid(row=20, column=5, sticky="nsew")
        # Quit Button
        self.quitButton = tk.Button(self, text="Quit", command=self.quit)
        self.quitButton.grid(row=21, column=5, sticky="nsew")

    # Calculate RGB Hex Code
    def calculateRGB(self, event):
        # Accessing RGB color values from sliders
        r = self.redSlider.get()
        g = self.greenSlider.get()
        b = self.blueSlider.get()
        # RGB Hexidecimal Color Representation and transfer of color onto panel
        hexColor = f"#{r:02x}{g:02x}{b:02x}"
        self.myCanvas.config(bg=hexColor)
        self.rgbD.configure(state='normal')
        self.rgbD.delete(0, tk.END)
        self.rgbD.insert(0, hexColor)
        self.rgbD.configure(state='readonly')

    # Get Value for Red from entry box and transfer it to the slider
    def setRed(self):
        try:
            r = self.redEntry.get()
            # Accept Numerical values from 0 to 255 only
            if not r.isdigit():
                raise ValueError
            else:
                # Convert only when the content is the right type
                intR = int(r)
                if intR < 0 or intR > 255:
                    raise ValueError

                else:
                    # Set the value on the Green Slider to the value entered here
                    self.redSlider.set(intR)
        except ValueError:
            self.redValueError = tk.Message(self, text= "ERROR! Please enter a numbner from 0 to 255")
   # Get Value for Green from entry box and transfer it to the slider
    def setGreen(self):
        try:
            g = self.greenEntry.get()
            # Accept Numerical Values from 0 to 255 only
            if not g.isdigit():
                raise ValueError
            else:
                intG = int(g)
                if intG < 0 or intG > 255:
                    raise ValueError
                else:
                # Set the Value on the Green Slider to the value entered here
                    self.greenSlider.set(intG)
        except ValueError:
            self.greenValueError = tk.Message(self, text= "ERROR! Please enter a numbner from 0 to 255")

    # Get Value for Blue from entry box and transfer it to the slider
    def setBlue(self):
        try:
            b = self.blueEntry.get()
            # Accept Numerical Values fromn 0 to 255 only
            if not b.isdigit():
                raise ValueError
            else:
                intB = int(b)
                if intB < 0 or intB > 255:
                    raise ValueError
                else:
                    # Set the value on the Green Slider to the value entered here
                    self.blueSlider.set(intB)
        except ValueError:
            self.blueValueError = tk.Message(self, text= "ERROR! Please enter a numbner from 0 to 255")

        ## HSV Code Generation ##
    def calculateHSV(self):
        # Used in calculations for (hue, saturation, value) later
        colorHue = 0
        colorSaturation = 0
        colorValue = 0
        r = self.redSlider.get()
        g = self.greenSlider.get()
        b = self.blueSlider.get()
        redNormalized, greenNormalized, blueNormalized = r/ 255.0, g/ 255.0,\
                                                        b/ 255.0 # Maximum of 255 (or FF in hex)
                                                                  # for each of r, g, and b
        # Highest and lowest values of the sets of red, green and blue components
        colorMax = max(redNormalized, greenNormalized, blueNormalized)
        colorMin = min(redNormalized, greenNormalized, blueNormalized)
        colorDelta = colorMax - colorMin
        # Hue Calculations (colorHue)
        if delta == 0:
            colorHue = 0 # This is what we may know as either grayscale or black-and-white
        elif colorMax == redNormalized:
            colorHue = (((greenNormalized - blueNormalized) / colorDelta ) % 6)
        elif colorMax == greenNormalized:
            colorHue = (((blueNormalized - redNormalized) / colorDelta) + 2)
        elif colorMax == blueNormalized:
            colorHue = (((redNormalized - greenNormalized) / colorDelta) + 4)
        # Hue must be positive
        if h < 0:
            h += 360    # Hue has min value of 0 and max of 3601
        # Saturation Calculations (Saturation)
        if colorMax == 0:
            colorSaturation = 0
        else:
            colorSaturation = (delta / colorMax) * 100

        # Value Calculations (colorValue)
        colorValue = colorMax * 100
        HSVValue = f"{colorHue}, {colorSaturation}, {colorValue}"
        self.hsvD.configure(state='normal')
        self.hsvD.delete(0, tk.END)
        self.hsvD.insert(0, HSVValue)
        self.hsvD.configure(state='readonly')

    def calculateCYMK(self):
        r = self.redSlider.get()
        g = self.greenSlider.get()
        b = self.blueSlider.get()
        # CYMK Start Values
        c = 0
        y = 0
        m = 0
        k = 0
        # Normalize RGB values before conversion (range 0-255)
        rNorm = r / 255.0
        gNorm = g / 255.0
        bNorm = b / 255.0


        # Black Value. This is whichever of the normlaized values is greatest
        k = 1 - max(rNorm, gNorm, bNorm)
        # Cyan Value
        if k == 1: # Pure black gives division by zero in case of pure black
            c = 0   # as shown by division calculations
        else:
            # Because cyan is opposite of red
            c = (1 - rNorm - k) / (1 - k)
        # MAgenta Value
        if k == 1:
            m = 0
        else:
            # Because magenta is opposite of green
            m = (1 - gNorm - k) / (1 - k)
        # Yellow Value
        if k == 1:
            y = 0
        else:
            # Because yellow is opposite of blue
            y = (1 - bNorm - k) / (1 - k)

        # Convert above totals to percentages, rounded to nearest whole numbers
        c = round(c * 100)
        y = round(m * 100)
        m = round(y * 100)
        k = round(k * 100)
        cymkValue = f"({c},{y},{m},{k})"
        cymkD.configure(state='normal')
        cymkD.delete(0, tk.END)
        cymkD.insert(0, cymkValue)
        cymkD.configure(state='readonly')
    # Copy RGB to Clipboard
    def copyRGB(self):
        rgbc = self.rgbD.get()
        self.clipboard_append(rgbc)
    # Copy HSV to CLipboard
    def copyHSV(self):
        hsvc = self.hsvD.get()
        self.clipboard_append(hsvc)
    # Copy CYMK to clipboard
    def copyCYMK(self):
        cymkc = self.cymkD.get()
        self.clipboard_append(cymkc)
    # RGB Inversion
    def rgbInvert(self):
        # Initial Values
        r = self.redSlider.get()
        intR = int(r)
        g = self.greenSlider.get()
        intG = int(g)
        b = self.blueSlider.get()
        intB = int(b)

        #RGB Inversion
        invR = 255 - intR
        invG = 255 - intG
        invB = 255 - intB

        redSlider.set(invR)
        greenSlider.set(invG)
        blueSlider.set(invB)


    # HSV Inversion
    def hsvInvert(self):
        r = self.redSlider.get()
        g = self.greenSlider.get()
        b = self.blueSlider.get()

    #CYMK Inversion
    def cymkInvert(self):
        r = self.redSlider.get()
        g = self.greenSlider.get()
        b = self.blueSlider.get()

# Main Program, executes only if ran as standalone
if __name__ == '__main__':
    app = ColorPaletteApp()
    app.mainloop()