#!/usr/bin/env python3
"""
QR Code Generator

A simple command-line tool to generate QR codes from URLs or text.

Usage:
    python generate_qr.py <url_or_text> [output_filename] [--color COLOR] [--bg BGCOLOR] [--size SIZE]

Examples:
    python generate_qr.py "https://example.com"
    python generate_qr.py "https://example.com" my_qrcode.png
    python generate_qr.py "https://example.com" --color "#57068c" --bg white
    python generate_qr.py "https://example.com" --size 15
"""

import argparse
import qrcode
from datetime import datetime
from pathlib import Path

def generate_qr_code(
    data: str,
    output_path: str = None,
    fill_color: str = "black",
    back_color: str = "white",
    box_size: int = 10,
    border: int = 4,
    error_correction: str = "H"
) -> str:
    """
    Generate a QR code image from the provided data.

    Parameters
    ----------
    data : str
        The URL or text to encode in the QR code.
    output_path : str, optional
        Output file path. If not provided, generates a timestamped filename.
    fill_color : str, default="black"
        Color of the QR code modules (the dark squares).
    back_color : str, default="white"
        Background color of the QR code.
    box_size : int, default=10
        Size of each box (module) in pixels.
    border : int, default=4
        Border size in boxes (minimum is 4 per QR spec).
    error_correction : str, default="H"
        Error correction level: L (~7%), M (~15%), Q (~25%), H (~30%).

    Returns
    -------
    str
        Path to the saved QR code image.
    """
    # Map error correction levels
    ec_levels = {
        "L": qrcode.constants.ERROR_CORRECT_L,
        "M": qrcode.constants.ERROR_CORRECT_M,
        "Q": qrcode.constants.ERROR_CORRECT_Q,
        "H": qrcode.constants.ERROR_CORRECT_H,
    }

    ec_level = ec_levels.get(error_correction.upper(), qrcode.constants.ERROR_CORRECT_H)

    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=ec_level,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate image
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Determine output path
    if output_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"qrcode_{timestamp}.png"

    # Ensure .png extension
    if not output_path.lower().endswith('.png'):
        output_path += '.png'

    # Save image
    img.save(output_path)

    return output_path

def main():
    parser = argparse.ArgumentParser(
        description="Generate QR codes from URLs or text.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "https://example.com"
  %(prog)s "https://example.com" output.png
  %(prog)s "https://example.com" --color "#57068c"
  %(prog)s "https://example.com" --size 15 --error-correction H

Error Correction Levels:
  L - ~7%  recovery (smallest QR code)
  M - ~15% recovery
  Q - ~25% recovery
  H - ~30% recovery (largest QR code, best for print)
        """
    )

    parser.add_argument(
        "data",
        help="URL or text to encode in the QR code"
    )
    parser.add_argument(
        "output",
        nargs="?",
        default=None,
        help="Output filename (default: qrcode_TIMESTAMP.png)"
    )
    parser.add_argument(
        "--color", "-c",
        default="black",
        help="QR code color (default: black)"
    )
    parser.add_argument(
        "--bg", "-b",
        default="white",
        help="Background color (default: white)"
    )
    parser.add_argument(
        "--size", "-s",
        type=int,
        default=10,
        help="Box size in pixels (default: 10)"
    )
    parser.add_argument(
        "--border",
        type=int,
        default=4,
        help="Border width in boxes (default: 4)"
    )
    parser.add_argument(
        "--error-correction", "-e",
        choices=["L", "M", "Q", "H"],
        default="H",
        help="Error correction level (default: H)"
    )

    args = parser.parse_args()

    output_path = generate_qr_code(
        data=args.data,
        output_path=args.output,
        fill_color=args.color,
        back_color=args.bg,
        box_size=args.size,
        border=args.border,
        error_correction=args.error_correction
    )

    print(f"QR code saved to: {output_path}")

if __name__ == "__main__":
    main()
