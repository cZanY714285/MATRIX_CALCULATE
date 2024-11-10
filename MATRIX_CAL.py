# 获取矩阵的行（row），列（column，此处简称col），此处row/col是整数而不是列表
row = int(input("请输入矩阵的行数："))
col = int(input("请输入矩阵的列数："))

# 输入矩阵1（矩阵martix简称mat）
# 注意这里引入了row_list来表示列表，而row还是表示整数
print("请输入矩阵1的元素，数字用空格分隔开来:")
mat_1 = []
for i in range(row):
    row_list = list(map(int, input(f"请输入第{i+1}行：").split()))  # 用空格分隔输入的数字并转换为整数
    mat_1.append(row_list)

# 输入矩阵2
print("请输入矩阵2的元素,数字用空格分隔开来：")
mat_2 = []
for i in range(row):
    row_list = list(map(int, input(f"请输入第{i+1}行：").split()))  # 同样用空格分隔输入并转换为整数
    mat_2.append(row_list)

# 创建一个空矩阵用来存放结果
mat_result = [
    [0] * col for _ in range(row)  # 创建一个与输入矩阵大小相同的结果矩阵，初始值为0
]

# 选择矩阵的运算方式
print("请问你要进行矩阵的什么运算？")
print("请回答：加/减/乘/除")

# 根据输入运算方式（calculate method,简称cal_met)来选择对应的操作
cal_met=input()

# 当输入“加”时
if cal_met == "加":
    for i in range(row):
        for j in range(col):
            mat_result[i][j] = mat_1[i][j] + mat_2[i][j]

# 当输入“减”时
elif cal_met == "减":
    for i in range(row):
        for j in range(col):
            mat_result[i][j] = mat_1[i][j] - mat_2[i][j]

# 当输入“乘”时
elif cal_met == "乘":
    for i in range(row):
        for j in range(col):
            mat_result[i][j] = mat_1[i][j] * mat_2[i][j]

# 当输入“除”时
elif cal_met == "除":
    print("注意输入元素不能为0哦")
    for i in range(row):
        for j in range(col):
            if mat_2[i][j] == 0:
                mat_result[i][j] = float('NaN')     #要是输入元素有0还非要算除法就返回NaN
            else:
                mat_result[i][j] = mat_1[i][j] / mat_2[i][j]

# 输出结果
print("计算结果是：")
for row in mat_result:
    print(row)
