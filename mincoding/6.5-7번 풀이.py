def main():
    arr = list(input().split())

    for i in range(len(arr)):
        if ord(arr[i]) >= ord("A") and ord(arr[i]) <= ord("Z"):
            arr[i] = arr[i].lower()
        else:
            arr[i] = arr[i].upper()

    print(*arr)

main()