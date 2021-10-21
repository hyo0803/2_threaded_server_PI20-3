import socket, threading, time
from progress.bar import IncrementalBar #необходимо установить модуль Progress (pip install progress)

ports=[]
# функция для сканирования порта
def scan_p(ip,port):
    global ports
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    try:
        sock.connect((ip,port))
        sock.close()
        ports.append(port)
    except:
        pass

def print_port():
                 # Выполните цикл подключенных клиентов и создайте соответствующий поток
        for p in range(i):
            # Если поток уже существует, пропустить
            if p in ports:
                continue
            index = threading.Thread(target = scan_p,args = (ip,p))
            index.start()
        if len(ports)>=1:
            print('\n',f"------ Количество октрытых портов {len(ports)} ------")
            print(' ------ Порты:')
            for port in ports:
                print(f' --------- {port}')
        else:
            print('Нет открытых портов')

#N = 2**16 - 1 - максимальное количество возможных портов

ip = input('Введите ваш IP-адрес(пример 127.0.0.1): ')
i = 1000   #кол-во портов, у которых будем проверять возможность подключения
bar = IncrementalBar('Countdown', max = i) #объявляем объект Progress Bar с максимальной выборкой max

# запускаем цикл по портам и создаем каждый раз новый поток для соотв. порта
for port in range(i):
    thread = threading.Thread(target=scan_p, args=(ip,port))
    thread.start()

    bar.next()#запуск progress bar
    time.sleep(0.1)

thread2 = threading.Thread(target=print_port, name='open')
thread2.start()
thread2.join()    

bar.finish()