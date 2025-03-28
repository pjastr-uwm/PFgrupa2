from unittest.mock import Mock

mock2 = Mock(autospec=True)

mock2.get_data.side_effect = [78, True, "ABC"]

print(mock2.get_data(44))
print(mock2.get_data(333))
print(mock2.get_data("PP"))


def modify(args):
    return args*2


mock2.get_data.side_effect = modify
print(mock2.get_data(44))
print(mock2.get_data("XYZ"))

mock2.get_data.side_effect = ValueError("Wrong value")
try:
    mock2.get_data()
except ValueError as err:
    print(err)

