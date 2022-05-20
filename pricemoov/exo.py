from dataclasses import dataclass
from typing import Iterable, Dict, Any, List


@dataclass
class Product:
    name: str
    prices: Dict[str, Any]


class Catalog:
    def __init__(self, products: Iterable[Product]):
        self.products = products

    def export_2D(self):
        """
        Exports the prices in a tabular format.
        We can assume the product prices will always be in two dimensions.
        """
        for product in self.products:
            for (date, d) in product.prices.items():
                for k, v in d.items():
                    yield [product.name, date, k, v]

    def export_nD(self):
        # res = []

        def loop(d, row) -> List[List[Any]]:
            if not isinstance(d, dict):
                return row + [d]

            acc = []

            for (k, v) in d.items():
                # res.append(loop(v, row + [k]))
                acc.append(loop(v, row + [k]))

            return acc

        for product in self.products:
            for (date, d) in product.prices.items():
                for k, v in d.items():
                    # loop(v, [product.name, date, k])
                    for x in loop(v, [product.name, date, k]):
                        yield x

        # return res


def test_export_2D():
    catalog = Catalog(
        products=[
            Product(
                name="one",
                prices={
                    "2030-01-01": {"web": 10.0, "shop": 20.0},
                    "2030-01-02": {"web": 30.0, "shop": 40.0},
                },
            ),
            Product(
                name="two",
                prices={
                    "2030-01-01": {"web": 11.0, "shop": 21.0},
                    "2030-01-02": {"web": 31.0, "shop": 41.0},
                },
            ),
        ]
    )
    res = catalog.export_2D()
    assert list(res) == [
        ["one", "2030-01-01", "web", 10.0],
        ["one", "2030-01-01", "shop", 20.0],
        ["one", "2030-01-02", "web", 30.0],
        ["one", "2030-01-02", "shop", 40.0],
        ["two", "2030-01-01", "web", 11.0],
        ["two", "2030-01-01", "shop", 21.0],
        ["two", "2030-01-02", "web", 31.0],
        ["two", "2030-01-02", "shop", 41.0]
    ]


# Q4: implement export_nD() (test_export_nD below must pass)
def test_export_nD():
    catalog = Catalog(
        products=[
            Product(
                name="one",
                prices={
                    "2030-01-01": {
                        "web": {"fr": 10.0, "en": 11.0},
                        "shop": {"fr": 20.0, "en": 21.0},
                    },
                    "2030-01-02": {
                        "web": {"fr": 30.0, "en": 31.0},
                        "shop": {"fr": 40.0, "en": 41.0},
                    },
                },
            ),
            Product(
                name="two",
                prices={
                    "2030-01-01": {
                        "web": {"fr": 15.0, "en": 16.0},
                        "shop": {"fr": 25.0, "en": 26.0},
                    },
                    "2030-01-02": {
                        "web": {"fr": 35.0, "en": 36.0},
                        "shop": {"fr": 45.0, "en": 46.0},
                    },
                },
            ),
        ]
    )

    res = catalog.export_nD()
    assert list(res) == [
        ["one", "2030-01-01", "web", "fr", 10.0],
        ["one", "2030-01-01", "web", "en", 11.0],
        ["one", "2030-01-01", "shop", "fr", 20.0],
        ["one", "2030-01-01", "shop", "en", 21.0],
        ["one", "2030-01-02", "web", "fr", 30.0],
        ["one", "2030-01-02", "web", "en", 31.0],
        ["one", "2030-01-02", "shop", "fr", 40.0],
        ["one", "2030-01-02", "shop", "en", 41.0],
        ["two", "2030-01-01", "web", "fr", 15.0],
        ["two", "2030-01-01", "web", "en", 16.0],
        ["two", "2030-01-01", "shop", "fr", 25.0],
        ["two", "2030-01-01", "shop", "en", 26.0],
        ["two", "2030-01-02", "web", "fr", 35.0],
        ["two", "2030-01-02", "web", "en", 36.0],
        ["two", "2030-01-02", "shop", "fr", 45.0],
        ["two", "2030-01-02", "shop", "en", 46.0]
    ]


if __name__ == "__main__":
    test_export_2D()
    test_export_nD()
