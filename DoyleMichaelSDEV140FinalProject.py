"""
Author: Michael Doyle
File Name: Color Palette GUI Suite
Description: This program combines a suite of tools for color plaette operation and gradient creation into a pair of
windows for color experimentation. Within the main window, the user can set the values of color with either sliders
or ertry into fields, and also derive equivalent values for HSV (Hue, Saturation, Brightness) and CYMK (Cyan, Yellow,
Magenta, Black) color systems) from the curent RGB (red. blue and green) color values.

The second window (opened by a button on the main window), has the same sliders for Red, Green and Blue values and the
fields for entry, but also includes a canvas which contains an image with a generated gradient based on
colors that a user specifies for the segments contained within.
"""
# Tkinter is main GUI interface resource library
import tkinter as tk
# For Error Messages
from tkinter import messagebox
# For better widget and window formatting
from tkinter import ttk
# For Ebedding Pictures into Windows
from PIL import Image, ImageTk
# Color Gradient Creation System
import numpy as np

# The class which contains all objects necessary for program execution and operation
class ColorPaletteMainWindow(tk.Tk):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class (tk.Tk)"""
        self.title("Color Palette Accessor and Mutator Suite")
        self.geometry("800x800")
        self.configure(bg="#a8e4a0")
        """ Red Component """
        self.redFrame = tk.Frame(self, width=266, height=300, background="#ff2c2c")
        self.redFrame.place(x=0, y=0)
        self.redFrame.update()
        self.redLabel = tk.Label(self, text="Red Value", fg="red")
        self.redLabel.configure(bg="#a8e4a0")
        self.redLabel.place(x=50, y=20)
        self.redLabel.update()
        # For cases where you want to just enter a value, instead of using the slider
        self.redEntryLabel = tk.Label(self, text="Enter Red Value Here")
        self.redEntryLabel.configure(bg="#a8e4a0")
        self.redEntryLabel.place(x=50, y=40)
        self.redEntryLabel.update()
        # Fill out this field with desired red value
        self.redEntry = tk.Entry(self, state = "normal")
        self.redEntry.place(x=50,y=60)
        self.redEntry.update()
        # Press this to input
        self.redEntryButton = tk.Button(self, text="Set Red", command=self.setRed)
        self.redEntryButton.place(x=50, y=100)
        self.redEntryButton.update()
        # Slider
        self.redSlider = tk.Scale(self, from_=0, to=255, orient="horizontal", command=self.calculateRGB)
        self.redSlider.configure(bg="#a8e4a0")
        self.redSlider.place(x=50, y=140)
        self.redSlider.update()
        """ Green Component """
        self.greenFrame = tk.Frame(self, width=266, height=300, background="#2cff2c")
        self.greenFrame.place(x=266, y=0)
        self.greenFrame.update()
        self.greenLabel = tk.Label(self, text="Green Value", fg="green")
        self.greenLabel.configure(bg="#a8e4a0")
        self.greenLabel.place(x=300, y=20)
        self.greenLabel.update()
        # For cases where you want to just enter a value, instead of using the slider
        self.greenEntryLabel =tk.Label(self, text="Enter Green Value Here")
        self.greenEntryLabel.config(bg="#a8e4a0")
        self.greenEntryLabel.place(x=300, y=40)
        self.greenEntryLabel.update()
        # Fill out this field with desired green value
        self.greenEntry = tk.Entry(self, state = "normal")
        self.greenEntry.place(x=300,y=60)
        self.greenEntry.update()
        # Press this to input
        self.greenEntryButton = tk.Button(self, text="Set Green", command=self.setGreen)
        self.greenEntryButton.place(x=300, y=100)
        self.greenEntryButton.update()
        # Slider
        self.greenSlider = tk.Scale(self, from_=0, to=255, orient='horizontal', command=self.calculateRGB)
        self.greenSlider.configure(bg="#a8e4a0")
        self.greenSlider.place(x=300, y=140)
        self.greenSlider.update()

        """ Blue Component"""
        self.blueFrame = tk.Frame(self, width=268, height=300, background="#2c2cff")
        self.blueFrame.place(x=532, y=0)
        self.blueFrame.update()
        self.blueLabel = tk.Label(self, text="Blue Value", fg="blue")
        self.blueLabel.configure(bg="#a8e4a0")
        self.blueLabel.place(x=600, y=20)
        self.blueLabel.update()

        # For cases where you want to just enter a value, instead of using the slider
        self.blueEntryLabel = tk.Label(self, text="Enter Blue Value Here")
        self.blueEntryLabel.config(bg="#a8e4a0")
        self.blueEntryLabel.place(x=600, y=40)
        self.blueEntryLabel.update()
        self.blueEntry = tk.Entry(self, state = "normal")
        self.blueEntry.place(x=600,y=60)
        self.blueEntry.update()
        self.blueEntrybutton = tk.Button(self, text="Set Blue", command=self.setBlue)
        self.blueEntrybutton.place(x=600, y=100)
        self.blueEntrybutton.update()
        # Slider
        self.blueSlider = tk.Scale(self, from_=0, to=255, orient='horizontal', command=self.calculateRGB)
        self.blueSlider.configure(bg="#a8e4a0")
        self.blueSlider.place(x=600, y=140)
        self.blueSlider.update()

        # Color Display Canvas
        self.canvasFrame = tk.Frame(self, width=266, height=300, background="#fffdd0")
        self.canvasFrame.place(x=266, y=300)
        self.canvasFrame.update()
        self.canvasLabel = tk.Label(self, text="Curent Color")
        self.canvasLabel.place(x=370, y=350)
        self.canvasLabel.update()
        self.mainCanvas = tk.Canvas(self, width=100, height=100, background="black")
        self.mainCanvas.place(x=355, y=375)
        self.mainCanvas.update()

        # RGB Code Display
        self.rgbLabel = tk.Label(self, text="RGB Value")
        self.rgbLabel.place(x=50, y=200)
        self.rgbLabel.update()
        self.rgbD = tk.Entry(self, state="readonly")
        self.rgbD.configure(bg="white")
        self.rgbD.place(x=50, y=225)
        self.rgbD.update()

        # RGB Copy Button
        self.cpyRGB = tk.Button(self, text= "Copy RGB Code", command=self.copyRGB)
        self.cpyRGB.place(x=50, y=250)
        self.cpyRGB.update()

        """ HSV Color System """
        # HSV Code Display
        self.hsvButton = tk.Button(self, text="Get HSV Value", command=self.calculateHSV)
        self.hsvButton.place(x=300, y=200)
        self.hsvButton.update()
        self.hsvD = tk.Entry(self, state="readonly")
        self.hsvD.configure(bg="white")
        self.hsvD.place(x=300, y=225)
        self.hsvD.update()

        # HSV Copy Button
        self.hsvCpy = tk.Button(self, text= "Copy HSV Code", command=self.copyHSV)
        self.hsvCpy.configure(bg="white")
        self.hsvCpy.place(x=300, y=250)
        self.hsvCpy.update()

        """CYMK Color System """

        # CYMK Code Display
        self.cymkButton = tk.Button(self, text="Get CYMK Value", command=self.calculateCYMK)
        self.cymkButton.place(x=600, y=200)
        self.cymkButton.update()
        self.cymkD = tk.Entry(self, state="readonly")
        self.cymkD.configure(bg="white")
        self.cymkD.place(x=600, y=225)
        self.cymkD.update()

        #CYMK Clipboard Copy Button
        self.cymkCpy = tk.Button(self, text="Copy CYMK Code", command=self.copyCYMK)
        self.cymkCpy.configure(bg="white")
        self.cymkCpy.place(x=600, y=250)
        self.cymkCpy.update()

        """ RGB Inverter Button """
        inv_image = Image.open("Images/InvertButton.png").resize((100, 100), resample=3)
        self.invImage = ImageTk.PhotoImage(inv_image)
        self.invCanvas = tk.Canvas(self, width=98, height=98, background="black")
        self.invCanvas.create_image(50, 50, image=self.invImage)
        self.invCanvas.place(x=80, y=390)
        self.invCanvas.update()
        self.RGBInvButton= tk.Button(self, text="Invert RGB Value", command=self.rgbInvert)
        self.RGBInvButton.place(x=82, y=430)
        self.RGBInvButton.update()

        """Button Links to Other Windows (HSV Color Tools, CYMK Color Tools)"""
        # Color Averaging Window
        grd_image = Image.open("Images/HSVButton.jpg").resize((100, 100), resample=3)
        self.grdImage = ImageTk.PhotoImage(grd_image)
        self.grdCanvas = tk.Canvas(self, width=98, height=98, background="black")
        self.grdCanvas.create_image(50, 50, image=self.grdImage)
        self.grdCanvas.place(x=630, y=390)
        self.grdToolsButton = tk.Button(self, text="Color Averaging Tools", command=self.grdOnBtnClick)
        self.grdToolsButton.place(x=618, y=430)
        self.grdToolsButton.update()

        # Quit Button
        quit_image = Image.open("Images/QuitButton.jpg").resize((31,50), resample=3)
        self.QuitGraphic = ImageTk.PhotoImage(quit_image)
        self.QuitCanvas = tk.Canvas(self, width=31, height=50)
        self.QuitCanvas.place(x=750, y=700)
        self.QuitCanvas.create_image(16,25, image=self.QuitGraphic)
        self.QuitCanvas.update()
        self.quitButton = tk.Button(self, text="Quit", command=self.destroy)
        self.quitButton.place(x=750, y=750)
        self.quitButton.update()


    # Calculate RGB Hex Code
    def calculateRGB(self, event):
        # Accessing RGB color values from sliders
        r = self.redSlider.get()
        g = self.greenSlider.get()
        b = self.blueSlider.get()

        # RGB Hexidecimal Color Representation and transfer of color onto panel
        hexColor = f"#{r:02x}{g:02x}{b:02x}"
        self.mainCanvas.config(bg=hexColor)
        self.rgbD.configure(state='normal')
        self.rgbD.delete(0, tk.END)
        self.rgbD.insert(0, hexColor)
        self.rgbD.configure(state='readonly')
        return hexColor

    # Get Value for Red from entry box and transfer it to the slider
    def setRed(self):
        try:
            r = self.redEntry.get()

            if not r.isdigit():
                # Accept Numerical values from 0 to 255 only
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
           messagebox.showerror("ERROR!", "Please enter a number between 0 and 255")
   # Get Value for Green from entry box and transfer it to the slider
    def setGreen(self):
        try:
            g = self.greenEntry.get()

            if not g.isdigit():
                # Accept Numerical Values from 0 to 255 only
                raise ValueError
            else:
                intG = int(g)
                if intG < 0 or intG > 255:
                    raise ValueError
                else:
                # Set the Value on the Green Slider to the value entered here
                    self.greenSlider.set(intG)
        except ValueError:
           messagebox.showerror("ERROR!", "Please enter a number from 0 to 255")

    def setBlue(self):
         # Get Value for Blue from entry box and transfer it to the slider
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
            self.blueValueError = messagebox.showerror("ERROR!", "Please enter a number from 0 to 255")

        ## HSV Code Generation ##
    def calculateHSV(self):
        # Used in calculations for (hue, saturation, value) later
        r = self.redSlider.get()
        g = self.greenSlider.get()
        b = self.blueSlider.get()

        # Normalized Color Values
        redNormalized = r / 255.0
        greenNormalized = g / 255.0
        blueNormalized = b / 255.0

        # Highest and lowest values of the sets of red, green and blue components
        colorMax = max(redNormalized, greenNormalized, blueNormalized)
        colorMin = min(redNormalized, greenNormalized, blueNormalized)

        # Difference between highest and lowest values
        colorDelta = colorMax - colorMin

        # Hue Calculations (colorHue)
        if colorDelta == 0:
            colorHue = 0 # This is what we may know as either grayscale or black-and-white
        elif colorMax == redNormalized:
            colorHue = ((((greenNormalized - blueNormalized) / colorDelta ) + 360) % 360)
        elif colorMax == greenNormalized:
            colorHue = ((((blueNormalized - redNormalized) / colorDelta) + 120) % 360)
        else:
            colorHue = ((((redNormalized - greenNormalized) / colorDelta) + 240) % 360)

        # Hue must be positive
        if colorHue < 0:
            colorHue += 360    # Hue has min value of 0 and max of 360

        # Saturation Calculations (Saturation)
        if colorMax == 0:
            colorSaturation = 0
        else:
            colorSaturation = (colorDelta / colorMax) * 100

        # Value Calculations (colorValue)
        colorValue = colorMax * 100
        HSVValue = f"({int(colorHue)}°, {int(colorSaturation)}%, {int(colorValue)}%)"
        self.hsvD.configure(state='normal')
        self.hsvD.delete(0, tk.END)
        self.hsvD.insert(0, HSVValue)
        self.hsvD.configure(state='readonly')


    def calculateCYMK(self):
        # Red, Green and Blue Values for Conversion
        r = self.redSlider.get()
        g = self.greenSlider.get()
        b = self.blueSlider.get()

        # CYMK Start Values
        c = 0.0   # Cyan
        y = 0.0   # Yellow
        m = 0.0   # Magenta
        k = 0.0   # Black

        # Normalize RGB values before conversion (range 0-255)
        rNorm = r / 255.0
        gNorm = g / 255.0
        bNorm = b / 255.0

        # Black Value. This is whichever of the normalized values is greatest
        k = 1 - max(rNorm, gNorm, bNorm)

        # Pure Black Yields 100% of black color and all others 0% by definition
        if r == 0 and g == 0 and b == 0:
            cymkValue = "0%, 0%, 0%, 100%"
        # Otherwise, perform the normal calculations
        else:
            # Cyan Value
            if k - 1 == 0: # Pure black gives division by zero in case of pure black
                c = 0.0   # as shown by division calculations
                y = 0.0
                m = 0.0
                k = 100

            else:
                # Note: values for c, y, m and k are represented as percentages
                c = (1 - rNorm - k) / (1 - k) * 100
                y = (1 - bNorm - k) / (1 - k) * 100
                m = (1 - gNorm - k) / (1 - k) * 100
                k *= 100

            cymkValue = f"({int(c)}%,{int(y)}%,{int(m)}%,{int(k)}%)"

        # Paste cymkValue into corresponding field in GUI
        self.cymkD.configure(state='normal')
        self.cymkD.delete(0, tk.END)
        self.cymkD.insert(0, cymkValue)
        self.cymkD.configure(state='readonly')
        return c, y, m, k

    # Copy RGB to Clipboard
    def copyRGB(self):
        rgbc = self.rgbD.get()
        self.clipboard_append(rgbc)
    # Copy HSV to Clipboard
    def copyHSV(self):
        hsvc = self.hsvD.get()
        self.clipboard_append(hsvc)
    # Copy CYMK to Clipboard
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

        # Apply to Inverses to Slider Values
        self.redSlider.set(invR)
        self.greenSlider.set(invG)
        self.blueSlider.set(invB)

    # Button link to HSV Color Tools
    def grdOnBtnClick(self):
        newWindow = CreateAverageColor(self)
        newWindow.grab_set()
        newWindow.wait_window(newWindow)

# Window for all items related to HSV color system, opened from button on main window
class CreateAverageColor(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Color Average Creator")
        self.geometry("800x800")
        self.configure(bg="#ff474c")

        """ Red Component """
        self.redFrame = tk.Frame(self, width=266, height=300, background="#ff2c2c")
        self.redFrame.place(x=0, y=0)
        self.redFrame.update()
        self.redLabel = tk.Label(self, text="Red Value", fg="red")
        self.redLabel.configure(bg="#a8e4a0")
        self.redLabel.place(x=50, y=20)
        self.redLabel.update()
        # For cases where you want to just enter a value, instead of using the slider
        self.redEntryLabel = tk.Label(self, text="Enter Red Value Here")
        self.redEntryLabel.configure(bg="#a8e4a0")
        self.redEntryLabel.place(x=50, y=40)
        self.redEntryLabel.update()
        # Fill out this field with desired red value
        self.redEntry = tk.Entry(self, state="normal")
        self.redEntry.place(x=50, y=60)
        self.redEntry.update()
        # Press this to input
        self.redEntryButton = tk.Button(self, text="Set Red", command=self.setRed)
        self.redEntryButton.place(x=50, y=100)
        self.redEntryButton.update()
        # Slider
        self.redSlider = tk.Scale(self, from_=0, to=255, orient="horizontal", command=self.calculateRGB)
        self.redSlider.configure(bg="#a8e4a0")
        self.redSlider.place(x=50, y=140)
        self.redSlider.update()

        """ Green Component """
        self.greenFrame = tk.Frame(self, width=266, height=300, background="#2cff2c")
        self.greenFrame.place(x=266, y=0)
        self.greenFrame.update()
        self.greenLabel = tk.Label(self, text="Green Value", fg="green")
        self.greenLabel.configure(bg="#a8e4a0")
        self.greenLabel.place(x=300, y=20)
        self.greenLabel.update()
        # For cases where you want to just enter a value, instead of using the slider
        self.greenEntryLabel = tk.Label(self, text="Enter Green Value Here")
        self.greenEntryLabel.config(bg="#a8e4a0")
        self.greenEntryLabel.place(x=300, y=40)
        self.greenEntryLabel.update()
        # Fill out this field with desired green value
        self.greenEntry = tk.Entry(self, state="normal")
        self.greenEntry.place(x=300, y=60)
        self.greenEntry.update()
        # Press this to input
        self.greenEntryButton = tk.Button(self, text="Set Green", command=self.setGreen)
        self.greenEntryButton.place(x=300, y=100)
        self.greenEntryButton.update()
        # Slider
        self.greenSlider = tk.Scale(self, from_=0, to=255, orient='horizontal', command=self.calculateRGB)
        self.greenSlider.configure(bg="#a8e4a0")
        self.greenSlider.place(x=300, y=140)
        self.greenSlider.update()

        """ Blue Component """
        self.blueFrame = tk.Frame(self, width=268, height=300, background="#2c2cff")
        self.blueFrame.place(x=532, y=0)
        self.blueFrame.update()
        self.blueLabel = tk.Label(self, text="Blue Value", fg="blue")
        self.blueLabel.configure(bg="#a8e4a0")
        self.blueLabel.place(x=600, y=20)
        self.blueLabel.update()
        # Slider
        self.blueSlider = tk.Scale(self, from_=0, to=255, orient='horizontal', command=self.calculateRGB)
        self.blueSlider.configure(bg="#a8e4a0")
        self.blueSlider.place(x=600, y=140)
        self.blueSlider.update()

        # For cases where you want to just enter a value, instead of using the slider """
        self.blueEntryLabel = tk.Label(self, text="Enter Blue Value Here")
        self.blueEntryLabel.config(bg="#a8e4a0")
        self.blueEntryLabel.place(x=600, y=40)
        self.blueEntryLabel.update()
        self.blueEntry = tk.Entry(self, state="normal")
        self.blueEntry.place(x=600, y=60)
        self.blueEntry.update()
        self.blueEntrybutton = tk.Button(self, text="Set Blue", command=self.setBlue)
        self.blueEntrybutton.place(x=600, y=100)
        self.blueEntrybutton.update()
        self.blueSlider = tk.Scale(self, from_=0, to=255, orient='horizontal', command=self.calculateRGB)
        self.blueSlider.configure(bg="#a8e4a0")
        self.blueSlider.place(x=600, y=140)
        self.blueSlider.update()

        """ Color Display Canvas """
        self.canvasFrame = tk.Frame(self, width=266, height=300, background="#fffdd0")
        self.canvasFrame.place(x=266, y=300)
        self.canvasFrame.update()
        self.canvasLabel = tk.Label(self, text="Curent Color")
        self.canvasLabel.place(x=340, y=290)
        self.canvasLabel.update()
        self.mainCanvas = tk.Canvas(self, width=100, height=100, background="black")
        self.mainCanvas.place(x=340, y=320)
        self.mainCanvas.update()

        """ RGB Code Display """
        self.rgbLabel = tk.Label(self, text="RGB Value")
        self.rgbLabel.place(x=50, y=200)
        self.rgbLabel.update()
        self.rgbD = tk.Entry(self, state="readonly")
        self.rgbD.configure(bg="white")
        self.rgbD.place(x=50, y=225)
        self.rgbD.update()
        self.getDecimalRGB = tk.Button(self, text="Get Decimal RGB", command=self.calculateRGBDecimal)
        self.getDecimalRGB.configure(bg="white")
        self.getDecimalRGB.place(x=50, y=300)
        self.getDecimalRGB.update()
        self.rgbDecimal = tk.Entry(self, state="readonly")
        self.rgbDecimal.configure(bg="white")
        self.rgbDecimal.place(x=50, y=275)
        self.rgbDecimal.update()

        """ RGB Inverter Button """
        inv_image = Image.open("Images/InvertButton.png").resize((100, 100), resample=3)
        self.invImage = ImageTk.PhotoImage(inv_image)
        self.invCanvas = tk.Canvas(self, width=98, height=98, background="black")
        self.invCanvas.create_image(50, 50, image=self.invImage)
        self.invCanvas.place(x=80, y=390)
        self.invCanvas.update()
        self.RGBInvButton = tk.Button(self, text="Invert RGB Value", command=self.rgbInvert)
        self.RGBInvButton.place(x=82, y=430)
        self.RGBInvButton.update()

        """ Left Color of Average """
        self.grdSetLeft = tk.Button(self, text="Set Left Color", command=self.setLeft)
        self.grdSetLeft.place(x=650, y=350)
        self.grdSetLeft.update()
        self.grdLeftEntry = tk.Entry(self, state="readonly")
        self.grdLeftEntry.place(x=650, y=320)
        self.grdLeftEntry.update()

        """ Right color of Average """
        self.grdSetRight = tk.Button(self, text="Set Right Color", command=self.setRight)
        self.grdSetRight.place(x=650, y=450)
        self.grdSetRight.update()
        self.grdRightEntry = tk.Entry(self, state="readonly")
        self.grdRightEntry.place(x=650, y=420)
        self.grdSetRight.update()

        """ Create Average Color from Left and Right """
        self.grdCreate = tk.Button(self, text="Create Average Color", command=self.createAverage)
        self.grdCreate.place(x=650, y=550)
        self.grdCreate.update()

        """ Average Color Canvas, where the resultant canvas will appear """
        self.avgLabel = tk.Label(self, text="Average color of left and right")
        self.avgLabel.place(x=270, y=450)
        self.avgCanvas = tk.Canvas(self, width=266, height=100, background="#000000")
        self.avgCanvas.place(x=270, y=500)
        self.avgCanvas.update()

        """ Quit Button """
        quit_image = Image.open("Images/QuitButton.jpg").resize((31, 50), resample=3)
        self.QuitGraphic = ImageTk.PhotoImage(quit_image)
        self.QuitCanvas = tk.Canvas(self, width=31, height=50)
        self.QuitCanvas.place(x=750, y=700)
        self.QuitCanvas.create_image(16, 25, image=self.QuitGraphic)
        self.QuitCanvas.update()
        self.quitButton = tk.Button(self, text="Quit", command=self.destroy)
        self.quitButton.place(x=750, y=750)
        self.quitButton.update()

    # Returns RGB slider values
    def getRedSlider(self):
        return int(self.redSlider.get())
    def getGreenSlider(self):
        return int(self.greenSlider.get())
    def getBlueSlider(self):
        return int(self.blueSlider.get())

    # Return RGB Color as Tuple
    def calculateRGBDecimal(self):
        r = self.getRedSlider()
        g = self.getGreenSlider()
        b = self.getBlueSlider()
        # Used for outputting to Decimal RGB field in real time
        value = f"({r},{g},{b})"
        # Used for Gradient Creation
        valueList = [r,g,b]
        # Put the string value in the field and return the tuple.
        self.rgbDecimal.config(state="normal")
        self.rgbDecimal.delete(0, "end")
        self.rgbDecimal.insert(0, value)
        self.rgbDecimal.config(state="readonly")
        return tuple(valueList)

    # Calculate RGB Hex Code
    def calculateRGB(self, RGB_decimal):
     # Accessing RGB color values from sliders
     r = self.getRedSlider()
     g =self.getGreenSlider()
     b =self.getBlueSlider()

    # RGB Hexidecimal Color Representation and transfer of color onto panel
     hexValue = f"#{r:02x}{g:02x}{b:02x}"
     self.mainCanvas.config(bg=hexValue)
     self.rgbD.configure(state='normal')
     self.rgbD.delete(0, tk.END)
     self.rgbD.insert(0, hexValue)
     self.rgbD.configure(state='readonly')
     return hexValue

    # Get Value for Red from entry box and transfer it to the slider
    def setRed(self):
        try:
            r = self.redEntry.get()

            if not r.isdigit():
                # Accept Numerical values from 0 to 255 only
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
            messagebox.showerror("ERROR!", "Please enter a number between 0 and 255")

        # Get Value for Green from entry box and transfer it to the slider
    def setGreen(self):
        try:
            g = self.greenEntry.get()

            if not g.isdigit():
                # Accept Numerical Values from 0 to 255 only
                raise ValueError
            else:
                intG = int(g)
                if intG < 0 or intG > 255:
                    raise ValueError
                else:
                    # Set the Value on the Green Slider to the value entered here
                    self.greenSlider.set(intG)
        except ValueError:
            messagebox.showerror("ERROR!", "Please enter a number from 0 to 255")

    def setBlue(self):
         # Get Value for Blue from entry box and transfer it to the slider
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
            self.blueValueError = messagebox.showerror("ERROR!", "Please enter a number from 0 to 255")

         # RGB Inversion

    def rgbInvert(self):
        # Initial Values
        r = self.redSlider.get()
        intR = int(r)
        g = self.greenSlider.get()
        intG = int(g)
        b = self.blueSlider.get()
        intB = int(b)

        # RGB Inversion
        invR = 255 - intR
        invG = 255 - intG
        invB = 255 - intB

        # Apply to Inverses to Slider Values
        self.redSlider.set(invR)
        self.greenSlider.set(invG)
        self.blueSlider.set(invB)

    # Gets the left side of the gradient
    def getLeft(self):
        grdLeftEntry = self.grdLeftEntry.get()
        return grdLeftEntry

    # Sets the left side of the gradient
    def setLeft(self):
        # Get RGB Slider Values
        r = self.getRedSlider()
        g = self.getGreenSlider()
        b = self.getBlueSlider()
        # Apply string to field and return tuple of integers
        left = f"({r},{g},{b})"
        self.grdLeftEntry.configure(state='normal')
        self.grdLeftEntry.delete(0, tk.END)
        self.grdLeftEntry.insert(0, left)
        self.grdLeftEntry.configure(state='readonly')

    # Gets the right side of the gradient
    def getRight(self):
        grdRightEntry = self.grdRightEntry.get()
        return grdRightEntry

    # Sets the right side of the gradient
    def setRight(self):
        # Get the RGB Slider Values
        r = self.getRedSlider()
        g = self.getGreenSlider()
        b = self.getBlueSlider()
        # Apply string to field and return tuple of integers
        right = f"({r},{g},{b})"
        rightInt = (r,g,b)
        self.grdRightEntry.configure(state='normal')
        self.grdRightEntry.delete(0, tk.END)
        self.grdRightEntry.insert(0, right)
        self.grdRightEntry.configure(state='readonly')


    # Create Average color from left and right colors stored above
    def createAverage(self):
        try:
            # Colors for deriving an average
           firstColor = self.getLeft().strip("(").strip(")").split(",")
           firstColor = [int(c) for c in firstColor]
           firstColor = list(map(int, firstColor))
           secondColor = self.getRight().strip("(").strip(")").split(",")
           secondColor = list(map(int, secondColor))


           # Color Averages
           avg_r = round((firstColor[0] + secondColor[0])/ 2)
           avg_g = round((firstColor[1] + secondColor[1])/ 2)
           avg_b = round((firstColor[2] + secondColor[2])/ 2)

           average_color = f"#{avg_r:02x}{avg_g:02x}{avg_b:02x}"
           self.avgCanvas.config(bg=average_color)

        except ValueError:
            messagebox.showerror("ERROR!", "An invalid value was used")
# Main Program, executes only if ran as standalone
if __name__ == '__main__':
    app = ColorPaletteMainWindow()
    app.mainloop()