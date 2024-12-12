# Building an Unbeatable Tic-Tac-Toe AI

## Project Objectives and Approach

### Statement of Project Objectives
The objective of this project is to develop an AI agent for Tic-Tac-Toe that **cannot be defeated by a human player**. The AI leverages the **Minimax algorithm with Alpha-Beta Pruning** to evaluate all possible moves, ensuring it always wins or forces a draw. This project aims to demonstrate optimal decision-making in a simple, yet illustrative two-player game environment.

### Approach

#### Tools and Techniques
- **Programming Language**: Python
- **AI Techniques**:
  - *Minimax Algorithm*: Evaluates all possible game outcomes, enabling the AI to make optimal moves.
  - *Alpha-Beta Pruning*: Optimizes the Minimax algorithm by reducing the number of moves evaluated.
- **Game Representation**:
  - *Game Tree Construction*: Represents the game's possible moves and states in a tree structure for efficient traversal.
  - *Depth-First Search (DFS)*: Explores each potential game outcome in the game tree.
- **Optional Tools**:
  - *Graphical Interface*: Optionally use `pygame` to create a visual interface for the Tic-Tac-Toe board.

---

## Project Deliverables
1. **Tic-Tac-Toe AI Code**: Core Python program implementing the Minimax algorithm with Alpha-Beta Pruning.
2. **Documentation**: Explanation of algorithms, decision-making process, and code structure.
3. **Graphical Interface (Optional)**: A basic graphical representation of the game board using `pygame` or a similar library for human-AI gameplay.
4. **Performance Metrics Report**: Evaluation of the AI's performance based on win rate, decision time, and optimal move selection.

---

## Evaluation Methodology

### 1. Win Rate
The AI consistently wins or forces a draw in every game, demonstrating its unbeatable nature.

### 2. Decision Time
Measure the time taken for the AI to make a move, highlighting the efficiency of Alpha-Beta Pruning in reducing the number of moves evaluated.

### 3. Optimal Move Selection
Verify that the AI consistently selects the optimal move in each game state, adhering to the Minimax algorithm's logic.

---

## Results and Demonstration
The AI ('X') demonstrates its ability to select optimal moves using the Minimax algorithm with Alpha-Beta pruning. Below are highlights of the implementation:
- The AI consistently wins or forces a draw.
- The interactive GUI enhances the player experience.

---

