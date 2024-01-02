while True:
    N = input()
    if N == "0":
        break
    answer = "no"

    if N == N[::-1]:
        answer = "yes"
    
    print(answer)



        

