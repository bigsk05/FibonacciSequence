import time
def calc(n):
    if n <= 1:
        return n
    else:
        return (calc(n - 1) + calc(n - 2))
def main():
    ts=time.time()
    for i in range(0,30):
        #print(calc(i))
        calc(i)
    print("[{}]".format(time.time()-ts))
main()