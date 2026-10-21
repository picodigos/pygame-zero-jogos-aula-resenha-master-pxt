import matplotlib.pyplot as plt

def plot(x,y):
    plt.plot(x,y) 
    plt.xlabel('crescimento')
    plt.ylabel('tempo')
    plt.title('crescimento pelo tempo')
    plt.grid()
    plt.show()

plot([1,2,3,4], [1,4,9,16])