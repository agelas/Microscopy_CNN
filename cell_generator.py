import numpy as np
import decimal
import matplotlib.pyplot as plt

class Cell_Generator:
    def generate_centroids(self, lowX, highX, lowY, highY):
        '''
        Generates a random number of cells that are sufficiently separated so as to be
        interesting
        '''
        np.random.seed(5) #Make this predictable for now
        randX = np.random.randint(low = -10, high = 10, size = 5)
        np.random.seed(7)
        randY = np.random.randint(low = -5, high = 5, size = 5)
        fig, ax = plt.subplots(figsize=(12, 9))
        plt.title('Scattered Cell Points')
        plt.scatter(randX, randY)
        plt.show()

        xInt = []
        yInt = []
        #One of the function calls gets extremely upset with numpy.int32 because it's not
        #a straight up int so we have to do this. 
        for i in range (0, len(randX)):
            convertX = randX[i]
            convertX = int(convertX.item())
            convertY = randY[i]
            convertY = int(convertY.item())
            xInt.append(convertX)
            yInt.append(convertY)
    
        centroids = self.merge_lists(xInt, yInt)
    
        return centroids

    def merge_lists(self, list1, list2):
        merged_list = [(list1[i], list2[i]) for i in range (0, len(list1))]
        return merged_list