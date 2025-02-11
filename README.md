# Image Watermarking Desktop App
A desktop application built with Python and Tkinter for managing and watermarking images, featuring a modern interface with theme customization and resolution control.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)
![PIL](https://img.shields.io/badge/Pillow-Image_Processing-green)
![Platform](https://img.shields.io/badge/Platform-Desktop-purple)

## 🎯 Overview
A desktop application under active development that currently provides:
1. Image batch loading and preview
2. Customizable interface themes (Light/Dark)
3. Multiple resolution support (800x600/1280x720)
4. Scrollable image gallery
5. Modern tabbed interface

🚧 **Work In Progress**: Watermarking functionality is currently under development.

### Planned Features
- Image watermarking capabilities
- Watermark customization options
- Batch watermark processing
- Export functionality
- Additional image operations

## 🖼️ Features
### Interface Elements
- Modern tabbed interface
- Dark/Light theme support
- Resolution adjustment (800x600/1280x720)
- Scrollable image gallery
- Add images button

### Image Management
- Multi-format support (JPEG, PNG, WEBP, ICO)
- Batch image loading
- Image preview thumbnails
- Dynamic resizing
- Grid-based gallery

## 🔧 Technical Components
### Resolution Management
```python
def change_resolution(self, root, resolution):
    window_width, window_height = resolution[0], resolution[1]
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2) - 60
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
```

### Key Features
1. **Interface Customization**
   - Theme switching
   - Resolution adjustment
   - Window positioning
   - Style management

2. **Image Processing**
   - Multi-format support
   - Batch processing
   - Dynamic resizing
   - Preview generation

3. **UI Components**
   - Navigation bar
   - Image gallery
   - Scrollable view
   - Custom styling

## 💻 Implementation Details
### Class Structure
- `Interface`: Main application window
- `NavigationBar`: Menu system
- `FrameNotebook`: Image gallery
- Custom styling implementation

### Component Management
- Centralized window positioning
- Dynamic image resizing
- Theme management
- Event handling

## 🚀 Usage
1. Install required packages:
```bash
pip install pillow
```

2. Run the application:
```bash
python main.py
```

3. Use the interface:
   - Click "Add Images" to load images
   - Use Options menu for customization
   - Navigate through image gallery
   - Apply operations to selected images

## 🎯 Features
### Interface Controls
- Theme switching (Light/Dark)
- Resolution adjustment
- Image addition
- Gallery navigation

### Image Operations
- Multiple format support
- Batch processing
- Preview generation
- Gallery management

## 🛠️ Project Structure
```
image-watermark-app/
├── main.py              # Application entry
├── interface.py         # Main window
├── interface_navbar.py  # Navigation
├── interface_notebook.py# Image gallery
└── add_image.png       # Default icon
```

## 📊 Supported Formats
- JPEG/JPG
- PNG
- WEBP
- ICO

Images can be loaded from any directory, with desktop as the default starting location.

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author
Burak TÜZEL
