
import pytest

pytestmark=pytest.mark.django_db

class TestCategoryModels:
    def test_category_model(self,category_factory):
        # Arrange
        # Act
        x=category_factory()
        # print(x.__str__())
        # Assert
        assert x.__str__()=='Category_4'

class TestBrandModels:
    def test_brand_model(self,brand_factory):
        # Arrange
        # Act
        x=brand_factory()
        # Assert
        assert x.__str__()=='test_brand'
    


class TestProductModels:
    def test_product_model(self,product_factory):
        # Arrange
        # Act
        x=product_factory()
        # Assert
        assert x.__str__()=='test_product'