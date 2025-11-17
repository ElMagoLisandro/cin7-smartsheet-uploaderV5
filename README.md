# Cin7 to Smartsheet Uploader v5.0

Professional inventory upload tool for Futura Trailers - Production Release

## Features

- ✅ Fixed column duplication (ProductCode/Product mapped correctly)
- ✅ Scrollable UI (works on 1920x1080)
- ✅ Position-based intelligent column mapping
- ✅ Batch upload optimized (50 rows per batch)
- ✅ Auto-save credentials
- ✅ Comprehensive error handling

## Installation

### Windows
```bash
pip install -r requirements.txt
python cin7_smartsheet_uploader_v5.py
```

### macOS
Download the pre-built .app from Releases

## Building

### macOS
```bash
pip install -r requirements.txt
pip install py2app
python setup.py py2app
```

### Windows
```bash
pip install pyinstaller
pyinstaller --onefile --windowed cin7_smartsheet_uploader_v5.py
```

## Version History

- v5.0 (2025-01-13): Production release with fixed macOS packaging
- v4.0: Fixed column mapping and added scrollbar
- v3.0: Initial automated version

## Support

Lisandro Agüero - lisandro39@gmail.com
```

---

### **📄 Archivo 6: `.github/workflows/build-macos.yml`**

**IMPORTANTE:** Este archivo va en una SUBCARPETA.

**Estructura:**
```
cin7-v5/
├── .github/
│   └── workflows/
│       └── build-macos.yml
├── cin7_smartsheet_uploader_v5.py
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md