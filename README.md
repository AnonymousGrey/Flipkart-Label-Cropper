✨ Smart Flipkart Label Cropper ✨

An intelligent PDF label cropping tool designed to trim and resize shipping labels from Flipkart (long vertical) and 2D (horizontal) formats automatically. Built with a user-friendly GUI using Python and Tkinter. 💻

✨ Features

- 📥 Select multiple PDF shipping labels at once
- ✂️ Automatically detects label orientation (Flipkart)
- 🔍 Smart cropping and trimming of the label area
- 📐 Resizes and pads images to standard 4x6 inches (1200x1800 px)
- 🖼️ Save all cropped labels as a single combined PDF
- 🧑‍💻 Simple GUI

------------------------------------------------------------------------------------------
  
🛠️ Installation

✅ Step 1: Clone the repository

```

git clone https://github.com/yourusername/smart-label-cropper.git`
cd smart-label-cropper

```

✅ Step 2: Install dependencies
Make sure you have Python 3.8+ installed. Then run in terminal:

```

pip install PyMuPDF Pillow

```

▶️ Usage
Run the GUI tool using:

```

python main.py

```
------------------------------------------------------------------------------------------
🧰 Build .exe (Optional)

🔧 Step 1: Install PyInstaller
```

pip install pyinstaller

```

🏗️ Step 2: Create .exe file
```

pyinstaller --noconsole --onefile --icon=icon.ico main.py

```
⚠️Don't have an icon? Just skip --icon=icon.ico.

The .exe will be available inside the dist/ folder:
dist/
└── SmartLabelCropper.exe

🥳Now you can run it directly on any Windows PC without installing Python! 💡

------------------------------------------------------------------------------------------
👨‍💻 Author
Vivek Sankath
🔥 Python Developer | 🛡️ Cybersecurity Enthusiast | 🧠 Automation Lover
📬 LinkedIn ( www.linkedin.com/in/vivek-sankath )

🪪 License
MIT License – Free to use, modify, and share with credit! 🙌

------------------------------------------------------------------------------------------
