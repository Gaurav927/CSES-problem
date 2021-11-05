import bisect
if __name__ == '__main__':
    num_applicants, num_free_apartments, max_allowed_diff = list(map(int, input().split()))

    desired_apar_size = list(map(int, input().split()))

    size_of_apart = list(map(int, input().split()))

    desired_apar_size.sort()
    size_of_apart.sort()

    sol = 0

    room_pointer = 0
    applicants_pointer = 0

    while room_pointer < num_free_apartments and applicants_pointer < num_applicants:

        low = desired_apar_size[applicants_pointer] - max_allowed_diff
        high = desired_apar_size[applicants_pointer] + max_allowed_diff

        room_size = size_of_apart[room_pointer]

        if low <= room_size <= high:
            sol += 1
            room_pointer += 1
            applicants_pointer += 1

        elif room_size < low:
            room_pointer += 1

        else:
            applicants_pointer += 1

    print(sol)






