LEFT = 0
RIGHT = 1
DATA = 2
node = [
    [1,    2,    "38.5℃以上発熱がある？"],
    [3,    4,    "元気がある？"],
    [5,    6,    "胸がひいひい？"],
    [None, None, "氷枕で病院"],
    [None, None, "様子を見る"],
    [None, None, "解熱剤で病院"],
    [None, None,  "速攻で病院"]
]

q = 0

if input(node[q][DATA]+"(y/n)") == "y":
    q += 1

