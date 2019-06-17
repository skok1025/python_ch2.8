from point import Point


def test_bound_instance_method():
    p = Point()
    p.setx(10)
    p.sety(20)
    p.show()


def test_unbound_class_method():
    p = Point()
    Point.setx(p,10)
    Point.sety(p,20)
    Point.show(p)


def main():
    test_bound_instance_method()


if __name__ == '__main__':
    main()


def test_order_method():
    print(Point.class_method())
    print(Point.static_method())