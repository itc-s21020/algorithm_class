data = [
    ["佐藤", "0000-0000-0000"],
    ["鈴木", "1111-1111-1111"],
    ["高橋", "2222-2222-2222"],
    ["田中", "3333-3333-3333"],
    [None]
]
while True:
    s = input("検索する相手の名字は？")
    i = 0
    while None != data[i][0] and data[i][0] != s:
        i += 1
    if data[i][0] == None:
        print("その名は登録されてません")
        data.pop(-1)
        a = input("電話番号を登録")
        data.append([s, a])
        data.append([None])
    else:
        print(data[i][0] + "さんの番号は " + data[i][1] + "です")
