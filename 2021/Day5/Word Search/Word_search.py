from collections import Counter, defaultdict


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        char_dict, rows, cols = defaultdict(list), len(board), len(board[0])

        # keep a dict for all position of a letter
        for i in range(rows):
            for j in range(cols):
                char_dict[board[i][j]].append([i, j])

        # check if dfs should be performed
        cnt_chars = Counter(word)
        for x, cnt in cnt_chars.items():
            if cnt > len(char_dict[x]):
                return False

        def dfs(board, word, prev_x, prev_y, idx, visited):
            letter = word[idx]
            if letter in char_dict:
                # fetch list of all position
                list_pos = char_dict[letter]
                for pos in list_pos:
                    xi, yi = pos[0], pos[1]
                    if (xi, yi) not in visited and (abs(xi - prev_x) + abs(yi - prev_y)) <= 1:
                        if idx + 1 == len(word):
                            return 1
                        else:
                            ans = dfs(board, word, xi, yi, idx +
                                      1, visited + [(xi, yi)])
                            if ans:
                                return 1

            return 0

        if len(word) == 1 and word[0] in char_dict:
            return True
        if word[0] in char_dict:
            for pos in char_dict[word[0]]:
                dfs_ans = dfs(board, word, pos[0], pos[1], 1, [
                              (pos[0], pos[1])])
                if dfs_ans == 1:
                    return True
        return False
