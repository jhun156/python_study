import sys
sys.stdin = open("input.txt","r")

T = 10
for test_case in range(1, T + 1):
    num = int(input())
    input_list = [i for i in map(int,input().split())]
    main_list = [0,0,*input_list,0,0]
    def get_point(index):
        temp_list = [main_list[index + i] for i in range(5)]
        temp_max = max(temp_list)
        result = 0
        result_list = []
        for i in range(5):
            result_list.append(temp_list[i] - temp_max)
        for i in range(5):
            if result_list[i] > 0:
                result += result_list[i]
        return result

    answer = 0
    for i in range(10):
        temp = 0
        temp += get_point(i)
        answer += temp

    print(f"#{test_case} {answer}")