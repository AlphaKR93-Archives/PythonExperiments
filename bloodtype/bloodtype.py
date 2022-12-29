A = ['AA', 'AO']
B = ['BB', 'BO']
O = ['OO']
AB = ['AB']
query = []
app = []
x = 0


m = A + B + O + AB
f = O
var = O
debug = False

for i in f:
    for j in m:
        query.append(f"{i} + {j} =")
        app.append(f"{i[0:1]}{j[0:1]}")
        app.append(f"{i[0:1]}{j[1:2]}")
        app.append(f"{i[1:2]}{j[0:1]}")
        app.append(f"{i[1:2]}{j[1:2]}")

for i in range(len(app)):
    if app[i] == "OA":
        app[i] = "AO"
    elif app[i] == "OB":
        app[i] = "BO"
    elif app[i] == "BA":
        app[i] = "AB"

if debug is True:
    for i in range(int(len(app) / 4)):
        print(query[i], app[i * 4], app[i * 4 + 1], app[i * 4 + 2], app[i * 4 + 3])

for i in app:
    if i in var:
        x += 1

print(f"전체 경우의 수: {len(app)}, {var} 이(가) 나올 확률: {x}")
print(f"{x} / {len(app)} = {x/len(app)} = {x/len(app)*100}%")
if debug is not True:
    print("산출된 혈액형을 보려면 debug = True 로 변경하십시오.")
