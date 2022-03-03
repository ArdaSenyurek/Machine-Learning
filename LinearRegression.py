import numpy as np
import matplotlib.pyplot as plt 
import time
import imageio
import os
# a = np.array([[1,3],[2,6],[3,4]])
# a = np.insert(a, 0,values= 1, axis= 1)
# print(a)
def gradient(inputs, y, parameter, comp):
    sum = 0
    for i in range(inputs.size):
        sp = np.concatenate((np.array([1]), np.array([inputs[i]])))
        sum += (np.dot(parameter, sp) - y[i]) * sp[comp]
    return sum

# sum = gradient(np.array([1,2,3]), np.array([2,4,6]), np.array([0,0]), 1)
# print(sum)
def ConstructGradient(inputs, y, parameter):
    gradientVector = np.zeros(parameter.size)
    for i in range(parameter.size):
        gradientVector[i] = gradient(inputs, y, parameter, i)
    return gradientVector
# grad = ConstructGradient(np.array([1,2,3]), np.array([2,4,6]), np.array([0,0]))
# print(grad)

def UpdateParameter(inputs, y, save = False):
    parameter = np.zeros(2)
    counter = 0
    while counter < 40000:
        counter += 1
        # print(parameter)
        # print(counter)
        if counter == 1000 or counter == 30000 or counter == 70000:
            plt.figure(1)
            plt.plot(inputs, y, '.')
            plt.plot(inputs, parameter[1] * inputs + parameter[0])
            plt.title(f'{counter} iterations')
            # plt.show()
            plt.savefig(fname =  r'C:\Users\arda_\Desktop\VS Code 2\Lab10\v3' + f'\Lab10 {counter}' + '.png', bbox_inches = 'tight')
            plt.close('all')
            
        # print('parameter', parameter)
        parameter = parameter - 0.00007 * ConstructGradient(inputs, y, parameter)
        print('COSTFUNCTION:', costFunct(inputs, y, parameter))

    return parameter

def costFunct(inputs, outputs, parameter):
    sum = 0
    # sp = np.insert(np.array([inputs[x]]), 0, 1, axis = 1)
    
    for x in range(inputs.size):
        # print(inputs[x].shape)
        # print(np.array([1]).shape)
        sp = np.concatenate((np.array([1]), np.array([inputs[x]])))
        sum += (np.dot(sp, parameter) - outputs[x])**2
    return 1/2 * sum
# print(costFunct(np.array([[1,3],[2,6],[3,4]]), np.array([1,2,3]), np.array([0,0,0])))
# plt.figure(1)
# plt.plot(np.array([1,2,3]), np.array([2,4,6]), '.')
# plt.plot(np.array([1,2,3]), param[1] * np.array([1,2,3]) + param[0])
# plt.savefig()
# plt.show()
def GenerateData():
    np.random.seed(0)
    a = 0
    x = 5 * np.random.rand(3) 
    y = - 10 * x + 5 * np.random.rand(3)
    for i in y:
        a+= i
    return x, y 

def Gif():
    images = []
    with imageio.get_writer(r'C:\Users\arda_\Desktop\VS Code 2\linearwhile\movie4.gif', mode='I') as writer:
        for i in range(1, 370):
            print(i)
            image = imageio.imread(r'C:\Users\arda_\Desktop\VS Code 2\Lab10Plots' + f'\{i}.png')
            writer.append_data(image)
                
    
x, y = GenerateData()
# strains = 1e-3 * np.array([0.56, 0.84, 1.32])
# shearStress = 1e3 * np.array([12.49, 24.98, 37.47])
param = UpdateParameter(x, y, save = False)

