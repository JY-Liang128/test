def sortArray(nums):
    n = len(nums)

    for i in range (n):
        for j in range (0 , n-i-1):
            if nums[j] > nums [j+1]:
                nums[j] , nums[j+1] = nums[j+1] , nums[j]

    return nums

def main():
    arr_input = input("输入:nums = ")
    nums = [int(x) for x in arr_input.strip('[]').split(',')]

    result = sortArray(nums)
    print(f"输出:{result}")

    input("按任意键退出...")

if __name__=="__main__":
    main()