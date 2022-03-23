
C = 0
 
def run(num=8):
    result = [-1] * num
    row = 0
    backtrack(result, row)
 
def backtrack(result, row):
    n = len(result)
    if row == n:
        global C
        C += 1
        print(result)
        return
    for i in range(n):
        result[row] = i
        if isvalid(result, row):
            backtrack(result, row+1)
 
def isvalid(ans, pos):
    valid = True
    for i in range(pos):
        diag = pos - i
        if ans[pos] in [ans[i], ans[i] - diag, ans[i] + diag]:
                valid = False
                break
    return valid
 
 
 
if __name__ == '__main__':
    run(num=8)
    print('solution num:', C)