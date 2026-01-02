# conftest is used to define fixtures ans configs that
# can be shared across multiple test files
import pytest
from fastapi.testclient import TestClient
from src.app import app


# fixtures are reusable pieces of setup code
@pytest.fixture
def client():
    return TestClient(app)  # Arrange
