import argparse
from .rectangle import Rectangle
from .square import Square


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Polygon Area Calculator — compute area, perimeter, diagonal, "
            "and ASCII representations for rectangles and squares."
        )
    )

    parser.add_argument(
        "--rectangle",
        nargs=2,
        metavar=("WIDTH", "HEIGHT"),
        help="Compute properties of a rectangle.",
    )

    parser.add_argument(
        "--square",
        metavar="SIDE",
        help="Compute properties of a square.",
    )

    args = parser.parse_args()

    # Rectangle mode
    if args.rectangle:
        width, height = map(float, args.rectangle)
        rect = Rectangle(width, height)
        print(f"Rectangle(width={width}, height={height})")
        print(f"Area: {rect.get_area()}")
        print(f"Perimeter: {rect.get_perimeter()}")
        print(f"Diagonal: {rect.get_diagonal()}")
        print("Picture:")
        print(rect.get_picture())
        return

    # Square mode
    if args.square:
        side = float(args.square)
        sq = Square(side)
        print(f"Square(side={side})")
        print(f"Area: {sq.get_area()}")
        print(f"Perimeter: {sq.get_perimeter()}")
        print(f"Diagonal: {sq.get_diagonal()}")
        print("Picture:")
        print(sq.get_picture())
        return

    parser.print_help()
