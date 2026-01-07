# QR Code Generator

A simple Python command-line tool to generate QR codes from URLs or text.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic usage

```bash
python generate_qr.py "https://example.com"
```

### Specify output filename

```bash
python generate_qr.py "https://example.com" my_qrcode.png
```

### Custom colors

```bash
# NYU Purple QR code
python generate_qr.py "https://example.com" --color "#57068c"

# White QR on black background
python generate_qr.py "https://example.com" --color white --bg black
```

### Adjust size

```bash
# Larger boxes (15px per module)
python generate_qr.py "https://example.com" --size 15
```

### All options

```bash
python generate_qr.py "https://example.com" output.png \
    --color black \
    --bg white \
    --size 10 \
    --border 4 \
    --error-correction H
```

## Command-line Options

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `data` | | (required) | URL or text to encode |
| `output` | | `qrcode_TIMESTAMP.png` | Output filename |
| `--color` | `-c` | `black` | QR code color |
| `--bg` | `-b` | `white` | Background color |
| `--size` | `-s` | `10` | Box size in pixels |
| `--border` | | `4` | Border width in boxes |
| `--error-correction` | `-e` | `H` | Error correction level |

## Error Correction Levels

| Level | Recovery | Use Case |
|-------|----------|----------|
| `L` | ~7% | Smallest QR, clean environments |
| `M` | ~15% | Standard use |
| `Q` | ~25% | Moderate damage expected |
| `H` | ~30% | Best for print/posters |

Higher error correction allows the QR code to remain scannable even if partially damaged or obscured.

## Python API

```python
from generate_qr import generate_qr_code

# Basic usage
output = generate_qr_code("https://example.com")

# With options
output = generate_qr_code(
    data="https://example.com",
    output_path="my_qr.png",
    fill_color="#57068c",
    back_color="white",
    box_size=12,
    error_correction="H"
)
```

## License

MIT
