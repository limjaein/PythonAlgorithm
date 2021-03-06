import copy


def solution():
    n = int(input())
    result = 0
    up = []
    down = []
    tmp = []

    up = list(map(int, input().split()))

    for i in range(1, n):
        down = list(map(int, input().split()))
        tmp = [0] * len(down)

        for idx, u in enumerate(down):
            if idx != 0 and idx != len(down) - 1:
                tmp[idx] = max(up[idx-1], up[idx]) + down[idx]
            elif idx == 0:
                tmp[idx] = up[idx] + down[idx]
            elif idx == len(down) - 1:
                tmp[idx] = up[idx-1] + down[idx]

        print(tmp)

        up = copy.deepcopy(tmp)

    for num in up:
        result = max(result, num)

    return result

print(solution())