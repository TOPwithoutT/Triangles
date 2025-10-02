from __future__ import annotations
from typing import Union
import argparse
import sys

Number = Union[int, float]


def _valid_number(x: Number) -> bool:
    try:
        if isinstance(x, bool):
            return False
        return float(x) > 0.0
    except (TypeError, ValueError):
        return False


def _is_triangle(a: float, b: float, c: float) -> bool:
    return a + b > c and a + c > b and b + c > a


def classify_triangle(a: Number, b: Number, c: Number) -> str:
    """
    Returns one of:
    "Equilateral" | "Isosceles" | "Scalene" | "Right" |
    "NotATriangle" | "InvalidInput"
    """
    if not (_valid_number(a) and _valid_number(b) and _valid_number(c)):
        return "InvalidInput"

    x, y, z = float(a), float(b), float(c)

    if not _is_triangle(x, y, z):
        return "NotATriangle"

    s1, s2, s3 = sorted([x, y, z])
    eps = 1e-7
    if abs(s1 * s1 + s2 * s2 - s3 * s3) <= eps:
        return "Right"

    # Equilateral / Isosceles / Scalene
    if abs(x - y) <= eps and abs(y - z) <= eps:
        return "Equilateral"
    if abs(x - y) <= eps or abs(y - z) <= eps or abs(x - z) <= eps:
        return "Isosceles"
    return "Scalene"


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Enter three side lengths to determine whether they form a triangle and its type."
    )
    parser.add_argument("sides", nargs="*", help="Three sides, e.g., 3 4 5")
    return parser.parse_args(argv)


def _to_number(s: str) -> Number | None:
    """Convert a string to float (accepts ints/floats); return None on failure."""
    try:
        if s.lower() in {"true", "false"}:
            return None
        return float(s)
    except Exception:
        return None


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv or sys.argv[1:])

    if len(args.sides) == 0:

        try:
            a = _to_number(input("Enter side a: ").strip())
            b = _to_number(input("Enter side b: ").strip())
            c = _to_number(input("Enter side c: ").strip())
        except (EOFError, KeyboardInterrupt):
            print("\nCancelled.")
            return 1
    elif len(args.sides) == 3:
        a = _to_number(args.sides[0])
        b = _to_number(args.sides[1])
        c = _to_number(args.sides[2])
    else:
        print("Incorrect number of arguments: provide 0 (for interactive mode) or 3 values, e.g.: python triangles.py 3 4 5")
        return 2

    if a is None or b is None or c is None:
        print("InvalidInput")
        return 0

    result = classify_triangle(a, b, c)
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
