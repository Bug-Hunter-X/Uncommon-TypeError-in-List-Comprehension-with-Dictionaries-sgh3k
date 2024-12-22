def function_with_uncommon_error_solution(data):
    result = []
    for item in data:
        try:
            if isinstance(item, dict) and 'value' in item:
                result.append(item['value'])
        except KeyError:
            pass
        except TypeError:
            pass
    return result
data = [{'value': 1}, {'another_key': 2}, {'value': 3}]
result = function_with_uncommon_error_solution(data)
print(f"Result: {result}")

data = [{'value': 1}, {'another_key': 2}, 3]
result = function_with_uncommon_error_solution(data)
print(f"Result: {result}")

data = [{'value': 1}, {'another_key': 2}, {'value': 3}, None]
result = function_with_uncommon_error_solution(data)
print(f"Result: {result}") 