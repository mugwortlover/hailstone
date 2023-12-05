from HailstoneData import HailstoneData
import matplotlib.pyplot as plt
import pickle

def main(total_to_check):
    #data = HailstoneData()
    #data.add(1, 0)
    with open('data.pickle', 'rb') as file:
        data = pickle.load(file)

    starting_num = data.checked_up_to + 1

    for i in range(starting_num, starting_num + total_to_check + 1):
        print(i)
        check(i, data)

    
    data.checked_up_to = starting_num + total_to_check + 1


    with open('data.pickle', 'wb') as file:
        pickle.dump(data, file)

    
    '''m = max([speed[1] for speed in speeds])
    print([speed for speed in speeds if speed[1] == m])'''

    
    plt.scatter(data.nums_checked, data.speeds)
    plt.xlabel('Numbers')
    plt.ylabel('Steps')
    plt.title('Hailstone Problem Steps')
    plt.show()
        

def step(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num * 3 + 1
    

def check(number, data):
    num = number
    steps = 0
    while True:
        num = step(num)
        steps += 1
        if data.contains(num):
            data.add(number, data.get_speed(num) + steps)
            break
        elif num == 1:
            data.add(number, steps)
            break
    
if __name__ == '__main__':
    main(2000)