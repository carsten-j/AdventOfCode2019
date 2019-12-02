import time


def timer(func):
    def call_func(*args, **kwargs):
        start_time = time.process_time()
        result = func(*args, **kwargs)
        end_time = time.process_time() - start_time
        print(f"\nExecution time: {end_time*1000:.3f} ms\n")
        return result

    return call_func


def compare_lists(result, expected):
    assert len(result) == len(expected)
    assert all([a == b for a, b in zip(expected, result)])
