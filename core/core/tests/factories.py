import factory

from core.product.models import Brand, Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Category
    name=factory.Sequence(lambda n:f"Category_{n}")


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Brand
    name="test_brand"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Product
    name="test_product"
    description="test_desc"
    digital=True
    brand=factory.SubFactory(BrandFactory)
    category=factory.SubFactory(CategoryFactory)