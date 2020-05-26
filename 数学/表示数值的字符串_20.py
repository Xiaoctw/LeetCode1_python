class Solution:
    '''
    确定有穷自动机，根据每一位字符进行状态转移
    '''

    def isNumber(self, s: str) -> bool:
        if not s:
            return False
        transTable = [
            [1, 2, 7, -1, -1, 0],
            [-1, 2, 7, -1, -1, -1],
            [-1, 2, 3, 4, -1, 9],
            [-1, 3, -1, 4, -1, 9],
            [6, 5, -1, -1, -1, -1],
            [-1, 5, -1, -1, -1, 9],
            [-1, 5, -1, -1, -1, -1],
            [-1, 8, -1, -1, -1, -1],
            [-1, 8, -1, 4, -1, 9],
            [-1, -1, -1, -1, -1, 9]
        ]
        # 代表每一列是什么意思
        cols = {'sign': 0, 'number': 1, '.': 2, 'exp': 3, 'other': 4,
                'blank': 5}

        def get_col(c: str):
            if c.isdigit():
                return 'number'
            if c in {'+', '-'}:
                return 'sign'
            if c == '.':
                return '.'
            elif c in {'E', 'e'}:
                return 'exp'
            if c == ' ':
                return 'blank'
            else:
                return 'other'

        legal_state = {2, 3, 5, 8, 9}
        state = 0
        # 状态转换
        for c in s:
            state = transTable[state][cols[get_col(c)]]
            if state == -1:
                return False
        if state in legal_state:
            return True
        return False
