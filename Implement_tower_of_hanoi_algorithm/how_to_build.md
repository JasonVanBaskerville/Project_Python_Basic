# Implementing the Tower of Hanoi Algorithm

The Tower of Hanoi is an algorithm for moving `n` disks from peg **A** to peg **C**, using peg **B** as an auxiliary peg. A larger disk must never be placed on top of a smaller disk.

In this implementation, the algorithm uses an **iterative** approach. The minimum number of steps required is `2^n - 1`.

## Algorithm Logic

1. **Determine the movement direction of the smallest disk**
   - If `n` is odd, disk `1` moves according to the pattern:
     `A → C → B → A`
   - If `n` is even, disk `1` moves according to the pattern:
     `A → B → C → A`

2. **Odd-numbered steps**
   
   At every odd-numbered step, the smallest disk (`1`) is moved to the next peg in its rotation sequence.

3. **Even-numbered steps**
   
   At every even-numbered step, disk `1` does not move. The program identifies the other two pegs and performs the only legal move by comparing the top disks on those two pegs.

4. **Repeat the process**
   
   The process continues until all disks are located on peg `C`.

Using this approach, the Tower of Hanoi problem can be solved without recursion. Each move is represented using lists `A`, `B`, and `C`, allowing the state of the three pegs to be displayed at every step.