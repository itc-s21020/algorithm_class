data = [
    ["佐藤", "0000-0000-0000"],
    ["鈴木", "1111-1111-1111"],
    ["高橋", "2222-2222-2222"],
    ["田中", "3333-3333-3333"]
]
n = len(data)
s = input("検索する相手の名字は？")
i = 0
while i < n and data[i][0] != s:
    i += 1
if i == n:
    print("その名は登録されてません")
else:
    print(data[i][0]+"さんの番号は "+data[i][1]+"です")