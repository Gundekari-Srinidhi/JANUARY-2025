class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for i in range(n)]
        res=[]
        def safe(r,c,board):
            for row in range(r-1,-1,-1):
                if board[row][c]=="Q":
                    return False
            row=r-1
            col=c-1
            while row>-1 and col>-1:
                if board[row][col]=="Q":
                    return False
                row-=1
                col-=1
            row,col=r-1,c+1
            while row>-1 and col<n:
                if board[row][col]=="Q":
                    return False
                row-=1
                col+=1
            return True

        def queens(r,n,board):
            if r==n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if safe(r,c,board):
                    board[r][c]="Q"
                    queens(r+1,n,board)
                    board[r][c]="."   
        queens(0,n,board)
        return res

        