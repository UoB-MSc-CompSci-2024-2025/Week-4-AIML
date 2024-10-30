import math
import numpy as np
import matplotlib.pyplot as plt

def generate_vector(dimensions, num_vectors):
    """
    Returns a vector according to the specified dimensions
    """
    vector = np.array([])
    print(f"Please enter the co-ordinates for vector {num_vectors + 1}")
    while len(vector) < dimensions:
        try:
            coordinate = int(input(f"Input co-ordinate {len(vector) + 1}: "))
            vector = np.append(vector, coordinate)
        
        except ValueError:
            print("Invalid input; please try again")
    return vector

def calculate_euclidean_norm(vector):
    """
    Returns the value of the Euclidean norm of the vector inputted
    """
    return math.sqrt(sum(value**2 for value in vector))

def generate_graph(list_of_vectors, list_of_norms):
    """
    Generates a graph of inputted vectors and their related Euclidean norms
    If the dimensions of the vectors are in 2d or 3d, they will be plotted to a graph, otherwise their values will just be printed to the terminal
    """
    if all(len(vector) == 2 for vector in list_of_vectors): # Makes sure all the vectors are in the same dimensions
        plt.figure()

        all_x = [vector[0] for vector in list_of_vectors]
        all_y = [vector[1] for vector in list_of_vectors]
        
        x_min, x_max = min(all_x) - 2, max(all_x) + 2
        y_min, y_max = min(all_y) - 2, max(all_y) + 2

        plt.xlim(x_min, x_max) # Tries to dynamically increase and decrease size of graph depending on size of vectors (sometimes it doesn't work, idk why)
        plt.ylim(y_min, y_max)

        for i, vector in enumerate(list_of_vectors):
            plt.scatter(vector[0], vector[1]) # Plots the vectors onto the graph
            plt.plot([0, vector[0]], [0, vector[1]], 'r--', linewidth=1) # Draws the dotted line from 0, 0 to the vector
            plt.text(vector[0], vector[1], f'|norm|={list_of_norms[i]:.2f}', ha='right', va='bottom', color='red') # Writes the norm value next to the vector

        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid() # Turns the graph into a grid for visual clarity

        # Turns the x and y lines along '0' into a thicker line for visual clarity
        plt.axhline(0, color='black',linewidth=1)
        plt.axvline(0, color='black',linewidth=1)
        
        plt.show()

    elif all(len(vector) == 3 for vector in list_of_vectors): # Does basically all of the same stuff as the 2d graph, but has different functions cause it's 3d
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.grid(True)
        for i, vector in enumerate(list_of_vectors):
            ax.scatter(vector[0], vector[1], vector[2])
            ax.plot([0, vector[0]], [0, vector[1]], [0, vector[2]], linestyle=":", color="blue", linewidth=1)
            ax.text(vector[0], vector[1], vector[2], s=f'|norm|={list_of_norms[i]:.2f}', ha='right', va='bottom', color='red')
        
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_zlabel("Z-axis")
        plt.title("3D Scatter Plot")
        plt.show()

    elif all(len(vector) < 2 or len(vector) > 3 for vector in list_of_vectors): # If the dimension is too small or too great to be mapped onto a graph
        print("Vector could not be mapped onto a graph due to incompatible dimensions")
        print("Your vectors and their respective norms: ")
        for i, vector in enumerate(list_of_vectors):
            print(f"Vector {i + 1}: {vector}, Norm: {list_of_norms[i]:.2f}")
        exit()


def main():
    list_of_vectors = []
    list_of_norms = []
    while True:
        try:
            dimensions = int(input("How many dimensions would you like to use? "))
            if dimensions <= 0:
                raise ValueError("Please input a positive integer")
            break
        except ValueError as e:
            print(e)
                
    
    num_vectors = int(input("How many vectors would you like to map? "))


    for i in range(num_vectors):
        vector = generate_vector(dimensions, i)
        
        list_of_vectors.append(vector)
    
        euclidean_norm = calculate_euclidean_norm(vector)
        list_of_norms.append(euclidean_norm)

    generate_graph(list_of_vectors, list_of_norms)


if __name__ == "__main__":
    main()