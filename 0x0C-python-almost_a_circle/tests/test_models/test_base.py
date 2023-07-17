        try:
            os.remove("Base.json")
        except OSError:
            pass
        try:
            os.remove("Rectangle.json")
        except OSError:
            pass
        try:
            os.remove("Square.json")
        except OSError:
            pass

    def test_load_from_file_rectangle(self):
        rect = Rectangle(10, 7, 2, 8, 23)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rect, rect2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rect), str(list_rectangles_output[0]))
        self.assertEqual(str(rect2), str(list_rectangles_output[1]))

    def test_load_from_file_rectnagle_type(self):
        rect = Rectangle(10, 7, 2, 8, 23)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rect, rect2])
        list_o = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in list_o))

    def test_load_from_file_square(self):
        sq = Square(10, 2, 1)
        sq2 = Square(10, 2, 1, 12)
        Square.save_to_file([sq, sq2])
        list_o = Square.load_from_file()
        self.assertEqual(str(sq), str(list_o[0]))
        self.assertEqual(str(sq2), str(list_o[1]))

    def test_load_from_file_square_type(self):
        sq = Square(10, 2, 1)
        sq2 = Square(10, 2, 1, 12)
        Square.save_to_file([sq, sq2])
        list_o = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in list_o))

    def test_load_from_file_no_file(self):
        list_o = Square.load_from_file()
        self.assertEqual([], list_o)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], [])


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created rectangle.jspn or square.json file"""
        try:
            os.remove("Base.json")
        except OSError:
            pass
        try:
            os.remove("Rectangle.json")
        except OSError:
            pass
        try:
            os.remove("Square.json")
        except OSError:
            pass

    def test_save_to_file_csv_rectangle(self):
        rect = Rectangle(10, 2, 5, 4, 6)
        Rectangle.save_to_file_csv([rect])
        with open("Rectangle.csv", "r") as fd:
            self.assertTrue("10,2,5,4,6", fd.read())

        rect2 = Rectangle(2, 7, 3, 6, 4)
        Rectangle.save_to_file_csv([rect, rect2])
        result = "10,2,5,4,6\n2,7,3,6,4"
        with open("Rectangle.csv", "r") as fd:
            self.assertTrue(result, fd.read())

    def test_save_to_file_csv_one_square(self):
        sq = Square(3, 9, 2, 4)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "r") as f:
            self.assertTrue("3,9,2,4", f.read())

        sq2 = Square(2, 1, 5, 3)
        Square.save_to_file_csv([sq, sq2])
        result = "3,9,2,4\n2,1,5,3"
        with open("Square.csv", "r") as fd:
            self.assertTrue(result, fd.read())

    def test_save_to_file_cls_name_creation(self):
        sq = Square(3, 9, 2, 4)
        Base.save_to_file_csv([sq])
        with open("Base.csv", "r") as f:
            self.assertTrue("3,9,2,4", f.read())

    def test_save_to_file_csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_without_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], [])


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """
    Test for laod from
    """
    @classmethod
    def tearDown(self):
        try:
            os.remove("Base.csv")
        except OSError:
            pass
        try:
            os.remove("Rectangle.csv")
        except OSError:
            pass
        try:
            os.remove("Square.csv")
        except OSError:
            pass

    def test_load_from_file_csv_no_file(self):
        output = Rectangle.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_rectangle(self):
        rect = Rectangle(10, 2, 5, 4, 6)
        rect2 = Rectangle(2, 7, 3, 6, 4)
        Rectangle.save_to_file_csv([rect, rect2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect), str(list_rectangles_output[0]))

        self.assertEqual(str(rect2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        rect = Rectangle(10, 2, 5, 4, 6)
        rect2 = Rectangle(2, 7, 3, 6, 4)
        Rectangle.save_to_file_csv([rect, rect2])
        l_out = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in l_out))

    def test_load_from_file_csv_square(self):
        sq = Square(3, 9, 2, 4)
        sq2 = Square(2, 1, 5, 3)
        Square.save_to_file_csv([sq, sq2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(sq), str(list_squares_output[0]))
        self.assertEqual(str(sq2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        sq = Square(3, 9, 2, 4)
        sq2 = Square(2, 1, 5, 3)
        Square.save_to_file_csv([sq, sq2])
        l_out = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in l_out))

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], [])


if __name__ == "__main__":
    unittest.main()
