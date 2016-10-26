from multiprocessing import Process, Queue
l=10**2
a=[]
for i in range(l):
	a.append(l)

def do_sum(q,l):
    q.put(sum(l))

def main():
    my_list = range(100)

    q = Queue()

    p1 = Process(target=do_sum, args=(q,my_list[:50]))
    p2 = Process(target=do_sum, args=(q,my_list[50:]))
    p1.start()
    p2.start()
    r1 = q.get()
    r2 = q.get()
    print r1+r2

if __name__=="__main__":
	main()
