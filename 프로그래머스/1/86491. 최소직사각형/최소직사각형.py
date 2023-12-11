def solution(sizes):
    answer = 0
    w_lst, h_lst = [], []    

    for w, h in sizes:
        w_lst.append(max(w, h))
        h_lst.append(min(w, h))
    
    answer = max(w_lst)*max(h_lst)
        

    return answer
