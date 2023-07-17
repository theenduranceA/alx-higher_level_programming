    def test_e17(self):
        """test x"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, None)

    def test_e18(self):
        """test width"""
        with self.assertRaises(ValueError):
            r = Rectangle(0, 1)

    def test_e19(self):
        """test height"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_14(self):
        """update 1"""
        r = Rectangle(1, 1, 1, 1)
        r.update(2)
        self.assertEqual(r.id, 2)

    def test_15(self):
        """update 2"""
        r = Rectangle(1, 1, 1, 1)
        r.update(2, 3)
        self.assertEqual(r.id, 2)
        self.assertEqual(r. width, 3)

    def test_16(self):
        """update 2"""
        r = Rectangle(1, 1, 1, 1)
        r.update(2, 3, 4)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)

    def test_17(self):
        """update 2"""
        r = Rectangle(1, 1, 1, 1)
        r.update(2, 3, 4, 5)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)

    def test_18(self):
        """update 2"""
        r = Rectangle(1, 1, 1, 1)
        r.update(2, 3, 4, 5, 6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_19(self):
        """test x getter"""
        r = Rectangle(1, 1, 1, 1)
        r.x = 10
        self.assertEqual(r.x, 10)

    def test_20(self):
        """test y getter"""
        r = Rectangle(1, 1, 1, 1)
        r.y = 10
        self.assertEqual(r.y, 10)

    def test_21(self):
        """test docstring"""
        self.assertIsNotNone(Rectangle.__doc__)
