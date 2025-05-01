# Photo-Organizer
This Python script automatically organizes photos from a specified source folder into subdirectories based on their **EXIF capture date**. It's especially useful for photographers or hobbyists with unorganized photo dumps.

---

## 🚀 Features

- Organizes images by **date taken** (from EXIF metadata)
- Moves files to folders like `YYYY-MM-DD/`
- Supports multiple image formats: `.jpg`, `.jpeg`, `.png`, `.tiff`, `.bmp`
- Processes files in batches using **multi-threading** for speed
- Includes a clean progress bar with `tqdm`
- Logs info and errors to help debug

---

## 🧰 Requirements

- Python 3.7+
- Required libraries:
  ```bash
  pip install pillow tqdm
  ```

---

## 🗂️ Directory Structure

Before running:

```
D:/
└── Photos42024/
    ├── image1.jpg
    ├── image2.png
    └── ...
```

After running:

```
D:/Programming/Python/Project/Organized Photos/
└── 2024-04-01/
    ├── image1.jpg
    └── image2.png
```

---

## ⚙️ Configuration

You can modify these constants in the script:

```python
PHOTO_DIR = 'D:/Photos42024/'  # Source folder of your images
PARENT_DIR = 'D:/Programming/Python/Project/Organized Photos/'  # Destination folder
BATCH_SIZE = 10  # Number of photos to process per thread batch
DELAY = 1  # Not used currently, reserved for future throttling
```

---

## ▶️ How to Run

```bash
python organize_photos.py
```

---

## 📝 Logging Output

Logs helpful messages:

```
2025-05-01 14:00:00 [INFO] Processing 200 files...
2025-05-01 14:00:01 [WARNING] Capture date not found in image4.png
2025-05-01 14:00:05 [INFO] Moved image1.jpg to 2024-04-01/
```

---

## 🛠️ Future Improvements

- Handle files without EXIF by using file creation/modification time
- Support for videos (MP4, MOV)
- Add a GUI with drag-and-drop
- Option to copy instead of move

---

## 📄 License

This project is open-source under the [MIT License](https://opensource.org/licenses/MIT).

---

## 🤝 Contributions

Feel free to fork, open issues, or submit pull requests to improve or customize this tool!

