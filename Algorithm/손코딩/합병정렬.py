def merge_sort(arr: list):
    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = r = 0

    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] < right_arr[r]:
            merged_arr.append(left_arr[l])
            l += 1
        else:
            merged_arr.append(right_arr[r])
            r += 1

    merged_arr += left_arr[l:]
    merged_arr += right_arr[r:]

    return merged_arr


def main():
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(merge_sort(arr))


if __name__ == "__main__":
    main()
