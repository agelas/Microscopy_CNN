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
        randX = np.random.randint(low = lowX, high = highX, size = 20)
        np.random.seed(7)
        randY = np.random.randint(low = lowY, high = highY, size = 20)
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
        #print(centroids)
        centroids = self.distribute_centroids(centroids)
        
        #Want to distribute our points somewhat in our plane
    
        return centroids

    def merge_lists(self, list1, list2):
        merged_list = [(list1[i], list2[i]) for i in range (0, len(list1))]
        return merged_list

    def distribute_centroids(self, centroids_list):
        print(centroids_list)
        for index, item in enumerate(centroids_list):
            x_coord, y_coord = item[0], item[1]
            #print('outer loop', item)

            while not self.distances_good(x_coord, y_coord, centroids_list):
                #If distances_good is not true, then change coordinates
                x_coord = x_coord + 1
                y_coord = y_coord + 1
                change_coord = list(item)
                change_coord[0] = x_coord
                change_coord[1] = y_coord
                reinsert = tuple(change_coord)
                centroids_list[index] = reinsert
            print('Edited: ', centroids_list)
        return centroids_list

    def distances_good(self, x_coord, y_coord, ref_list):
        
        for item in ref_list:
            #print('check against', item)
            if not self.check_distance(x_coord, y_coord, item[0], item[1]):
                return False
        #If we make it here all distances are good
        return True

    def check_distance(self, x1, y1, x2, y2):
        #print('x1: ', x1, 'x2: ', x2)
        dist = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        #print(dist)
        if dist == 0:
            #Don't replace itself, although if you move centroid onto another one could be false True
            return True
        if dist < 4:
            print('Found')
            return False
        return True
