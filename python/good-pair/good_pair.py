def goodPair(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    return count


def main():
    nums = [1, 2, 3, 1, 1, 3]
    print(goodPair(nums))


if __name__ == "__main__":
    main()
