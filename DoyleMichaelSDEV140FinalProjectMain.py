"""
Author: Michael Doyle
File Name: SDEV 140 Final Project Main
Description: The main program module for the color palette GUI application. Takes the definitions laid out in
DoyleMichaelSDEV140FinalProjectClasses.py and puts them to work, depending on user interactions.
"""

import tkinter as tk
# import pillow # for insertion of JPG and/or PNG files into the window elements

class ColorPaletteApp(tk.Tk):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (tk.Tk)"""
        self.title("Color Palette Accessor and Mutator Suite")
        self.geometry("1200x1200")
        self.configure(bg="#a8e4a0")
        # Red Component
        self.redLabel = tk.Label(self, text="Red Value", fg="red")
        self.redLabel.configure(bg="#a8e4a0")
        self.redLabel.pack(side='top', anchor='s')
        self.redSlider = tk.Scale(self, from_=0, to=255, orient="horizontal", command=self.calculateRGB)
        self.redSlider.configure(bg="#a8e4a0")
        self.redSlider.pack(side='top', anchor='s')

        # Green Component
        self.greenLabel = tk.Label(self, text="Green Value", fg="green")
        self.greenLabel.pack(side='left')
        self.greenLabel.configure(bg="#a8e4a0")
        self.greenSlider = tk.Scale(self, from_=0, to=255, orient='horizontal', command=self.calculateRGB)
        self.greenSlider.configure(bg="#a8e4a0")
        self.greenSlider.pack(side='left')

        # Blue Component
        self.blueLabel = tk.Label(self, text="Blue Value", fg="blue")
        self.blueLabel.pack(side='right')
        self.blueSlider = tk.Scale(self, from_=0, to=255, orient='horizontal', command=self.calculateRGB)
        self.blueSlider.pack(side='right')

        # Color Display Canvas
        self.canvasLabel = tk.Label(self, text="Curent Color")
        self.canvasLabel.pack(side='top', anchor ='n', fill='x')
        self.myCanvas = tk.Canvas(self, width=100, height=100, background="black")
        self.myCanvas.pack(side='top')

        # RGB Code Display
        self.rgbLabel = tk.Label(self, text="RGB Value")
        self.rgbLabel.pack(side='top', anchor='n', fill='x')
        self.rgbD = tk.Entry(self, state="readonly")
        self.rgbD.configure(bg="white")
        self.rgbD.pack(side='top')
        # RGB Copy Button
        self.cpyRGB = tk.Button(self, text= "Copy Code", command=self.copyRGB)
        self.cpyRGB.pack(side='top', anchor='n', fill='x')

        # HSV Code Display
        self.hsvLabel = tk.Label(self, text="HSV Value")
        self.hsvLabel.pack(side='left', fill='x')
        self.hsvD = tk.Entry(self, state="readonly")
        self.hsvD.configure(bg="white")
        self.hsvD.configure(bg="white")
        self.hsvD.pack(side='left', fill='x')
        # HSV Copy Button
        self.hsvCpy = (tk.Button(self, text= "Copy Code", command=self.copyHSV))
        self.hsvCpy.configure(bg="white")
        self.hsvCpy.pack(side='left', fill='x')

        # CYMK Code Display
        self.cymkLabel = tk.Label(self, text="CYMK Value")
        self.cymkLabel.pack(side='right', fill='x')
        self.cymkD = tk.Entry(self, state="readonly")
        self.cymkD.configure(bg="white")
        self.cymkD.pack(side='right', fill='x')
        #CYMK Clipboard Copy Button
        self.cymkCpy = tk.Button(self, text="Copy Code", command=self.copyCYMK)
        self.cymkCpy.configure(bg="white")
        self.cymkCpy.pack(side='right', fill='x')
        # RGB Inverter Button
        self.RGBInvLabel = tk.Label(self, text="RGB Value Invert")
        self.RGBInvLabel.pack(side='left', fill='x')
        # HSV Interver Button
        self.HSVInvLabel = tk.Label(self, text="HSV Value Invert")
        self.HSVInvLabel.pack(side='top', fill='x')
        # CYMK Inverter Button
        self.CYMKInvLabel = tk.Label(self, text="CYMK Value Invert")
        self.CYMKInvLabel.pack(side='right', fill='x')
        # Quit Button
        self.quitButton = tk.Button(self, text="Quit", command=self.quit)
        self.quitButton.pack(side='bottom', anchor='s')

    # Calculate RGB Hex Code
    def  calculateRGB(self, event):
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
        self.hsvD.configure(state='readonly')

        ## HSV Code Generation ##
    def calculateHSV(self, event):
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
        HSVValue = f"{colorHue:2x} {colorSaturation:2x} {colorValue:2x}"
        self.myCanvas.config(bg=HSVValue)
    def calculateCYMK(self, event):
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
        m = round(m * 100)
        y = round(y * 100)
        k = round(k * 100)

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
        r = self.redSlider.get()
        g = self.greenSlider.get()
        b = self.blueSlider.get()
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
if __name__ == '__main__':
    app = ColorPaletteApp()
    app.mainloop()