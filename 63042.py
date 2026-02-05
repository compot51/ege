n = 712
skipped = 0
cnt_a = 0
cnt_b = 0
a = []
b = []
#  print(a)

with open("input.txt", "r") as f:
    for i in range(n):
        flag = 0
        time_arrive, time_in_queue, choice = map(int, f.readline().split())
        if i == 0:
            time_free = time_arrive + time_in_queue
            a.append(time_free)
        elif i == 1:
            time_free = time_arrive + time_in_queue
            b.append(time_free)
        else:
            while time_arrive >= a[0]:
                    a.pop(0)
                    cnt_a += 1
            while time_arrive >= b[0]:
                    b.pop(0)
                    cnt_b += 1
            if choice == 0 and len(a) == 12 and len(b) == 12:
                flag = 1
            elif choice == 2 and len(b) == 12:
                flag = 1
            elif choice == 1 and len(a) == 12:
                flag = 1
            elif choice == 0 and len(a) < 12 and len(a) < len(b):
                time_free = time_in_queue + a[len(a) - 1]
                a.append(time_free)
            elif choice == 0 and len(b) < 12 and len(b) < len(a):
                time_free = time_in_queue + b[len(b) - 1]
                b.append(time_free)
            elif choice == 1 and len(a) < 12:
                time_free = time_in_queue + a[len(a) - 1]
                a.append(time_free)
            elif choice == 2 and len(b) < 12:
                time_free = time_in_queue + b[len(b) - 1]
                b.append(time_free)


        print(time_arrive, time_in_queue, choice, '                   освободится в', time_free, '                  ПРОПУСК' if flag else '')
        print('Очередь А:', a)
        print('Очередь В:', b)
        print('-----------------------------------------------------------------------')

print(cnt_a + len(a), 712 - cnt_a - cnt_b - len(a) - len(b))

