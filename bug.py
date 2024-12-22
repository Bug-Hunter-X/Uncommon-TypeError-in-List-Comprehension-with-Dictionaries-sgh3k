def function_with_uncommon_error(data):
    try:
        # Assume 'data' is a list of dictionaries
        result = [item['value'] for item in data if 'value' in item]
        return result
    except KeyError as e:
        print(f"KeyError: {e}")
        return []
    except TypeError as e:
        print(f"TypeError: {e}")
        return []
data = [{'value': 1}, {'another_key': 2}, {'value': 3}]
result = function_with_uncommon_error(data)
print(f"Result: {result}")

data = [{'value': 1}, {'another_key': 2}, 3]
result = function_with_uncommon_error(data)
print(f"Result: {result}")