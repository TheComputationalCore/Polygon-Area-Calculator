from polygon_calculator import Square, Rectangle


def test_square_is_subclass():
    sq = Square(5)
    assert isinstance(sq, Rectangle)
    assert isinstance(sq, Square)


def test_square_area():
    sq = Square(9)
    assert sq.get_area() == 81


def test_square_set_side_updates_both_dimensions():
    sq = Square(5)
    sq.set_side(7)
    assert sq.width == 7
    assert sq.height == 7


def test_square_set_width_overridden():
    sq = Square(5)
    sq.set_width(4)
    assert sq.width == 4
    assert sq.height == 4


def test_square_set_height_overridden():
    sq = Square(5)
    sq.set_height(3)
    assert sq.width == 3
    assert sq.height == 3


def test_square_diagonal():
    sq = Square(4)
    assert round(sq.get_diagonal(), 5) == round((4**2 + 4**2) ** 0.5, 5)


def test_square_picture():
    sq = Square(3)
    expected = "***\n***\n***\n"
    assert sq.get_picture() == expected


def test_square_to_string():
    sq = Square(5)
    assert str(sq) == "Square(side=5)"
