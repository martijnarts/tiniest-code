def bubble_sort(ls):
    for i in range(len(ls)-1):
        if ls[i] > ls[i+1]:
            ls[i], ls[i+1] = ls[i+1], ls[i]
    return bubble_sort(ls) if any([ls[i] > ls[i+1] for i in range(len(ls)-1)]) else ls
