import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
list_of_boards = [1, 2, 3]
move_counts = [21, 15, 33]


# Create a DataFrame 
data = pd.DataFrame({
    'Board': list_of_boards,
    'Move Counts': move_counts
})

# Plot
sns.barplot(x='Board', y='Move Counts', data=data, palette='viridis')

# Add labels and title
plt.title('Move Counts for Each 6x6 Board BFS')
plt.xlabel('Board')
plt.ylabel('Move Counts')

# Show the plot
plt.show()


list_of_boards = ['Random','Hillclimber','BFS']
move_counts = [336, 181, 15]

# Create a DataFrame 
data = pd.DataFrame({
    'Board': list_of_boards,
    'Move Counts': move_counts
})

# Plot
sns.barplot(x='Board', y='Move Counts', data=data, palette='viridis')

# Add labels and title
plt.title('Move Counts for 6x6 Board #1')
plt.xlabel('Board')
plt.ylabel('Move Counts')

# Show the plot
plt.show()

list_of_boards = ['Random','Hillclimber','BFS']
move_counts = [1749, 1595, 27]

# Create a DataFrame 
data = pd.DataFrame({
    'Board': list_of_boards,
    'Move Counts': move_counts
})

# Plot
sns.barplot(x='Board', y='Move Counts', data=data, palette='viridis')

# Add labels and title
plt.title('Move Counts for 9x9 Board #1')
plt.xlabel('Board')
plt.ylabel('Move Counts')

# Show the plot
plt.show()