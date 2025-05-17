# Maze Solver

## Maze Qualities:
- 1 Entrance
- 1 Exit
- Dead Ends
- Forks
- 1 Solution (Path from entrance to exit)

## Ideas
- To Determine Entrance:
    - First cell drawn is the entrance.
    - Choose random number and make that be the entrance.
        - Keep track of number of cells drawn and when that cell number matches


## Data Structure
- When a maze is intialized, cells are created and are organized in a list of lists. There is a list of columns and each column list contains the rows of Cells.
- Essentially this will be treated as a Graph since each cell will have edges and vertices and this will aid in creating the maze itself.
- To craft the maze itself, a depth-first search algorithm will be used.


## Cell Class
- Needs two points:
    - Top Left: x_1, y_1
    - Bottom Right x_2, y_2

- Four Walls:
    - Each wall is a Line, which consists of 2 points. The coordinates of these points come from the Cell Class point coordinates
    - Right Wall (vertical):
        - Top Point: x_2, y_1
        - Bottom Point: x_2, y_2
    - Bottom Wall (horizontal):
        - Left Point: x_1, y_2 
        - Right Point: x_2, y_2 
    - Left Wall:
        - Top Point: x_1, y_1
        - Bottom Point: x_1, y_2
    - Top Wall:
        - Left Point: x_1, y_1
        - Right Point: x_2, y_1
- Movement:
    - Moving from cell to cell is determined by the existence of a wall. If wall exists, then can't move that way.
- Starting with simplest set up: Equal number of cells horizontal and vertical.
- Each cell will:
    - be equal size and will be square.
        - All lines will be equal length.
    - Have at least one wall not present
- Cell Types:
    - External: One wall is on a vertical or horizontal edge
    - Internal: No walls touch vertical or horizontal edge
    - Path
        - 2 openings
    - Dead End
        - 1 opening
    - Fork
        - At least 3 openings
- If a cell has an opening, the joining cell with which it opens to must have that wall open as well.
- A cell is drawn on the window in a right to left manner, once max number of cells is reached, a new row is started directly below the last one. 

## Potential Pseudocode:
- Create Cell
- Determine walls to draw
- Draw Cell
- Move onto next cell.

first row:
first cell:
- x1: 50 (starting point + (size * (col_# - 1)))
- y1: 50 (starting point + (size * (row_# - 1)))
- x2: 100 (starting point + (size * col_#))
- y2: 100 (starting point + (size * row_#))
second cell:
- x1: 100 (50 + (50 * 1))
- y1: 50 (50 + (50  * 0))
- x2: 150 (50 + (50 * 2))
- y2: 100 (50 + (50 * 1))
third cell:
- x1: 150 (50 + (50 * 2))
- y1: 50 (50 + (50  * 0))
- x2: 200 (50 + (50 * 3))
- y2: 100 (50 + (50 * 1))

second row:
first cell: 
- x1: 50 (50 + (50 * (1 - 0)))
- y2: 100 (50 + (50 * (2 - 1)))
- x2: 100 (50 + (50 * 1))
- y2: 150 (50 + (50 * 2))

For each cell:
- There are two x points:
    - x1 = starting point + (size * (col_# - 1))
    - x2 = starting point + (size * col_#)
- There are two y points:
    - y1 = starting point + (size * (row_# - 1))
    - y2 = starting point + (size * row_#)

Pseudo Code:
- Initialize Grid Size to some number
- Initialize a Starting Point to some number
- Initialize a Size variable to some number
- Initialize Row Count to 1
- Initialize Col Count to 1
- While the row count is less than grid size:
    - initialize a cells variable to empty list
    - While the col count is less than grid size:
        - Create the top left point based on the algorithm
            - x1 = starting point + (size * (col_# - 1))
            - y1 = starting point + (size * (row_# - 1))
        - Create the bottom right point:
            - x2 = starting point + (size * col_#)
            - y2 = starting point + (size * row_#)
        - Create a cell using those points and append them to cells variable
        - increment the col size by 1
    - set Col Count back to 1
    - draw each cell in the cells list using a for loop
    increment row size by 1