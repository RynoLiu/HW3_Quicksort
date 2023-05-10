# Function
def Quicksort(array, start, end):
    if start >= end:
        return array
    
    pivot = array[start] # 初始化為新的基準點
    left = start
    right = end
    
    while left <= right:
        print(array)
        while array[right] > pivot and right >= start:
            right -= 1
        
        while array[left] < pivot and left <= end:
            left += 1
            
        if right > left: # 條件如果成立，則左右值交換
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        else:
            break
    
    array[start], array[right] = array[right], array[start]
    Quicksort(array, start, right - 1) # end=基準點左邊1格
    Quicksort(array, right + 1, end) # start=基準點右邊1格
    return array


# 主程式
if __name__ == "__main__":        
    demo_list = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
    sorted_list = Quicksort(demo_list, 0, len(demo_list)-1)
    print("最終結果:", sorted_list)