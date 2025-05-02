import fitz  
from PIL import Image, ImageChops
import io
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Global state
selected_files = []
cropped_images = []

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    return im.crop(bbox) if bbox else im

def resize_with_padding(img, target_size=(1200, 1800)):
    img_ratio = img.width / img.height
    target_ratio = target_size[0] / target_size[1]

    if img_ratio > target_ratio:
        new_width = target_size[0]
        new_height = round(target_size[0] / img_ratio)
    else:
        new_height = target_size[1]
        new_width = round(target_size[1] * img_ratio)

    img_resized = img.resize((new_width, new_height), Image.LANCZOS)
    new_img = Image.new("RGB", target_size, "white")
    paste_x = (target_size[0] - new_width) // 2
    paste_y = (target_size[1] - new_height) // 2
    new_img.paste(img_resized, (paste_x, paste_y))
    return new_img

def select_pdfs():
    global selected_files
    files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if files:
        selected_files = list(files)
        file_list_var.set("\n".join(os.path.basename(f) for f in selected_files))

def crop_labels():
    global cropped_images
    cropped_images = []

    if not selected_files:
        messagebox.showerror("Error", "Please select PDF files first.")
        return

    try:
        for file in selected_files:
            doc = fitz.open(file)
            for page in doc:
                full_rect = page.rect
                width = full_rect.width
                height = full_rect.height
                is_flipkart = height > width

                if is_flipkart:
                    crop_rect = fitz.Rect(0, 0, width, height * 0.45)
                    pix = page.get_pixmap(clip=crop_rect, dpi=300)
                    img = Image.open(io.BytesIO(pix.tobytes()))
                    img = trim(img)
                    img = resize_with_padding(img)
                else:
                    crop_rect = fitz.Rect(0, 0, width, height * 0.40)
                    pix = page.get_pixmap(clip=crop_rect, dpi=300)
                    img = Image.open(io.BytesIO(pix.tobytes()))
                    img = img.rotate(270, expand=True)
                    img = trim(img)

                cropped_images.append(img)

        messagebox.showinfo("Done", f"Total {len(cropped_images)} labels cropped successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"Cropping failed:\n{e}")

def save_pdf():
    if not cropped_images:
        messagebox.showerror("Error", "No cropped labels found. Click 'Crop Labels' first.")
        return

    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if output_path:
        try:
            cropped_images[0].save(output_path, save_all=True, append_images=cropped_images[1:])
            messagebox.showinfo("Success", f"Combined PDF saved to:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Saving failed:\n{e}")

# GUI setup
root = tk.Tk()
root.title("Smart Label Cropper – Flipkart + 2D")
root.geometry("500x450")
root.resizable(False, False)

file_list_var = tk.StringVar()

tk.Label(root, text="Select Multiple Label PDFs:", font=("Arial", 12)).pack(pady=10)
tk.Button(root, text="Select PDFs", command=select_pdfs, bg="lightblue").pack()

tk.Label(root, textvariable=file_list_var, fg="blue", wraplength=460, justify="left").pack(pady=10)

tk.Button(root, text="Crop Labels", command=crop_labels, bg="green", fg="white", font=("Arial", 11)).pack(pady=10)
tk.Button(root, text="Save Combined PDF", command=save_pdf, bg="orange", fg="white", font=("Arial", 11)).pack(pady=10)

tk.Label(root, text="Made By Vivek Sankath 🔥", fg="gray", font=("Arial", 8)).pack(side="bottom", pady=10)

root.mainloop()
