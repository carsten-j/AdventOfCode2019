import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"\nTime required: {(time.time() - start_time)*1000:.2f} ms\n")
        return result

    return wrapper


def compare_lists(result, expected):
    assert len(result) == len(expected)
    assert all([a == b for a, b in zip(expected, result)])
