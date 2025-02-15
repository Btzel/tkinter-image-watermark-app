# Image Watermarking Desktop App
A sophisticated desktop application built with Python and Tkinter for adding customizable watermarks to images, featuring an advanced UI with theme customization and dynamic text controls.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)
![PIL](https://img.shields.io/badge/Pillow-Image_Processing-green)
![Platform](https://img.shields.io/badge/Platform-Desktop-purple)

## 🎯 Overview
A professional watermarking tool that provides:
1. Advanced text watermarking functionality
2. Multi-image batch processing
3. Real-time watermark preview
4. Customizable text styling
5. Grid-based watermark tiling

## 🖼️ Features
### Watermark Customization
- Text content and color
- Font selection and sizing
- Rotation control
- Position adjustment
- Grid tiling options

### Interface Elements
- Dark/Light theme support
- Multiple resolution support (800x600/1280x720)
- Tabbed image interface
- Scrollable image gallery
- Real-time preview

## 🔧 Technical Components
### Watermark Control System
```python
def create_repeating_grid_text(self):
    y_grid_length = (self.image_bottom_border - self.image_top_border)
    y_step = y_grid_length / self.spacing
    x_grid_length = (self.image_right_border - self.image_left_border)
    x_step = x_grid_length / self.spacing
    
    # Create grid of watermarks
    while y_start_point <= y_end_point:
        x_start_point = x_step / 2
        while x_start_point <= x_end_point:
            self.create_watermark_at_position(x_start_point, y_start_point)
```

### Key Features
1. **Watermark Customization**
   - Text styling
   - Position control
   - Rotation adjustment
   - Grid spacing
   - Color selection

2. **Image Processing**
   - Multiple format support
   - Batch processing
   - Size preservation
   - Quality control
   - Export options

3. **UI Components**
   - Navigation system
   - Image gallery
   - Control panels
   - Theme management
   - Resolution control

## 💻 Implementation Details
### Class Structure
- `Interface`: Main application window
- `ImagePanel`: Watermark control panel
- `CanvasModifier`: Watermark rendering
- `FrameNotebook`: Image management

### Watermark Controls
- Font and size selection
- Color picker
- Position sliders
- Rotation control
- Grid spacing

## 📘 How to Use

### Loading Images
1. Launch the application
2. Click the "Add Images" buttons to upload image files
3. Select one or multiple images from your computer
4. Your images will appear in the scrollable gallery

### Adding Watermarks
1. Click on an image in the gallery to open it in a new tab
2. Use the right panel to customize your watermark:
   - Enter text in the "Text" field
   - Choose color using "Pick Color" button
   - Select font from the dropdown menu
   - Adjust font size using the slider
   - Control rotation with the rotation slider

### Position and Layout
1. Adjust watermark position:
   - Use "Offset X" slider for horizontal position
   - Use "Offset Y" slider for vertical position
2. Choose watermark pattern:
   - Select "No Tile" for single watermark
   - Choose "Repeated Grid" for pattern
   - Adjust spacing when using grid pattern

### Saving Your Work
1. Click "Save Image" button
2. Choose save location and format
3. Your watermarked image will be saved in the selected format

### Additional Features
- Change resolution: Options → Resolution
- Switch themes: Options → Theme
- Use mouse wheel to scroll through gallery
- Multiple image tabs can be open simultaneously

## 🎯 Features
### Watermark Options
- Text content editing
- Font customization
- Color selection
- Position control
- Grid tiling

### Image Operations
- Multi-format support (JPEG, PNG, WEBP, ICO)
- Batch image loading
- Preview generation
- Size preservation
- Export options

## 🛠️ Project Structure
```
watermark-app/
├── main.py              # Application entry
├── interface.py         # Main window
├── image_panel.py       # Watermark controls
├── canvas_modifier.py   # Watermark rendering
├── interface_navbar.py  # Navigation
├── interface_notebook.py# Image management
└── notebook_style.py    # UI styling
```

## 🎨 Example Output

![Watermark Example](./copyright.png)

*Example of a photo with repeated "Copyright©" watermark using grid pattern*

Features demonstrated in this example:
- Grid pattern watermarking
- Text rotation
- Consistent spacing
- Professional copyright protection
- Full image coverage

Settings used for this example:
- Text: "Copyright©"
- Pattern: Repeated Grid
- Rotation: 45 degrees
- Grid Spacing: 11
- White text color

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author
Burak TÜZEL