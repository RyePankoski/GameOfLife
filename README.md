Every dev must make game of life at some point. Here is mine.

Rather simple. We have a dict of cells. I chose a dict because I wanted to add intermediate states. The dict key is its location in space, and the value is its state. At this time, its just 1. If a cell is dead, it is just removed from the dict. We only iterate over live cells and its immediate neighbors which is not very efficient, I could store a tuple that contains the no of living neighbors that any given cell has and skip checking the dead neighbors of living cells, but at least its not iterating over every dead cell.

<img width="2089" height="1435" alt="image" src="https://github.com/user-attachments/assets/fbe06418-f4aa-4548-9553-d68f8b272f52" />
