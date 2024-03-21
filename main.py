import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, simpledialog

class QualityDialog(simpledialog.Dialog):
    def body(self, master):
        tk.Label(master, text="Quality (1-100):").grid(row=0)
        self.quality = tk.IntVar(master, value=90)
        tk.Spinbox(master, from_=1, to=100, textvariable=self.quality).grid(row=0, column=1)
        return None  # initial focus

    def apply(self):
        self.result = self.quality.get()

def optimize_image(image_path, output_dir, quality):
    # Open the image file.
    with Image.open(image_path) as img:
        # Create output path.
        output_path = os.path.join(output_dir, "optimized_" + os.path.basename(image_path))
        # Save the image again with reduced quality.
        img.save(output_path, optimize=True, quality=quality)

def main(input_dir, output_dir, quality):
    # Get all files in the input directory.
    files = os.listdir(input_dir)
    # Filter out all non-jpeg files.
    jpg_files = [f for f in files if f.endswith('.jpg') or f.endswith('.jpeg')]
    # Optimize all jpeg images.
    for jpg in jpg_files:
        optimize_image(os.path.join(input_dir, jpg), output_dir, quality)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window.
    input_dir = filedialog.askdirectory(title="Select Input Directory")
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    quality = QualityDialog(root).result
    main(input_dir, output_dir, quality)