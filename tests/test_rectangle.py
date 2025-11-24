from polygon_calculator import Rectangle, Square


def test_rectangle_area():
    rect = Rectangle(10, 5)
    assert rect.get_area() == 50


def test_rectangle_perimeter():
    rect = Rectangle(4, 3)
    assert rect.get_perimeter() == 14


def test_rectangle_diagonal():
    rect = Rectangle(3, 4)
    assert rect.get_diagonal() == 5.0  # 3-4-5 triangle


def test_rectangle_picture_small():
    rect = Rectangle(3, 2)
    expected = "***\n***\n"
    assert rect.get_picture() == expected


def test_rectangle_picture_too_big():
    rect = Rectangle(51, 4)
    assert rect.get_picture() == "Too big for picture."


def test_rectangle_string_repr():
    rect = Rectangle(10, 5)
    assert str(rect) == "Rectangle(width=10, height=5)"


def test_get_amount_inside_rectangle():
    outer = Rectangle(16, 8)
    inner = Rectangle(4, 2)
    assert outer.get_amount_inside(inner) == 16  # 4x4 grid


def test_get_amount_inside_square():
    outer = Rectangle(16, 8)
    inner = Square(4)
    assert outer.get_amount_inside(inner) == 8
