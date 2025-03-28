from unittest.mock import Mock

mock3 = Mock()

mock3(3,4,5)
mock3(x="a", p=False)
mock3(9, -4, False, "XYZ", text="abc", x=7, p=False)
print(mock3.called)
print(mock3.call_count)
print(mock3.call_args)
print(mock3.call_args[0])
print(mock3.call_args[1])
print(mock3.call_args_list)

print("loop")
for i, call in enumerate(mock3.call_args_list):
    print("Number", i)
    print("Positional arguments", call[0])
    print("Keyword argument", call[1])

