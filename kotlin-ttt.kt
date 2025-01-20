fun main() {
    val board = Array(3) { CharArray(3) { ' ' } }
    var currentPlayer = 'X'

    while (true) {
        printBoard(board)
        println("Player $currentPlayer, enter your move (row and column): ")

        try {
            val input = readLine()!!.split(" ").map { it.toInt() }
            val row = input[0]
            val col = input[1]

            if (row !in 0..2 || col !in 0..2) {
                println("Invalid position! Row and column must be between 0 and 2.")
                continue
            }

            if (board[row][col] != ' ') {
                println("This position is already taken. Choose another!")
                continue
            }

            board[row][col] = currentPlayer

            if (checkWin(board, currentPlayer)) {
                printBoard(board)
                println("Player $currentPlayer wins!")
                break
            }

            if (isDraw(board)) {
                printBoard(board)
                println("It's a draw!")
                break
            }

            currentPlayer = if (currentPlayer == 'X') 'O' else 'X'
        } catch (e: Exception) {
            println("Invalid input! Please enter row and column as two numbers separated by a space.")
        }
    }
}

fun printBoard(board: Array<CharArray>) {
    println("\n  0 1 2")
    for (i in board.indices) {
        print("$i ")
        println(board[i].joinToString("|"))
        if (i < board.size - 1) {
            println("  -+-+-")
        }
    }
    println()
}

fun checkWin(board: Array<CharArray>, player: Char): Boolean {
    // Check rows, columns, and diagonals
    for (i in 0..2) {
        if (board[i].all { it == player }) return true
        if ((0..2).all { board[it][i] == player }) return true
    }
    if ((0..2).all { board[it][it] == player }) return true
    if ((0..2).all { board[it][2 - it] == player }) return true
    return false
}

fun isDraw(board: Array<CharArray>): Boolean {
    return board.all { row -> row.all { it != ' ' } }
}
