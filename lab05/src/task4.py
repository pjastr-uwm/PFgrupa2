from unittest.mock import Mock, MagicMock

mock1 = Mock()
mock2 = MagicMock()

print(hasattr(mock1, "__str__"))
print(hasattr(mock2, "__str__"))

print(hasattr(mock1, "__len__"))
print(hasattr(mock2, "__len__"))

mock2.__len__.return_value = 5
mock2.__add__.return_value = "wynik dodawania"
mock2.__getitem__.side_effect = lambda key: f"wartość dla {key}"

print(len(mock2))
print(mock2 + 7)
print(mock2[5])
print(mock2["klucz"])

mock_context = MagicMock()
mock_context.__enter__.return_value = "wartość wewnątrz kontekstu"
mock_context.__exit__.return_value = False

with mock_context as context:
    print(context)
