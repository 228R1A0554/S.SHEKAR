import threading


def t_square(n):
    print("square=",n*n)

     def f_cube(m):

    print("cub=",n*n*n)
t1=threading.Thread(target=f_square,args=(5,))
t2=threading.Thread(terget=f_cube,args=(101,))
   t1.start()
   t2.start()
   t1.start()
   t2.start()