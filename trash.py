def foo(arr, threshold=30, min_len=5):
    result = []
    counter = 0
    start = 0
    to_write = False
    for i, val in enumerate(arr):
        if val > threshold:
            counter += 1
            if counter >= min_len:
                to_write = True
        elif to_write:
            result.append((i - counter, i - 1))
            to_write = False
            counter = 0

                
    return result

if __name__ == "__main__":
    arr = [72, 75, 78, 130, 135, 138, 80, 77, 76, 140, 145, 90]
    print(foo(arr, threshold=120, min_len=2))