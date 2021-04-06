class Solution
{
public:
    bool checkPresent(vector<vector<char>> board, string word)
    {
        int A[26];
        memset(A, 0, sizeof(A));
        for (int i = 0; i < board.size(); ++i)
        {
            for (int j = 0; j < board[0].size(); ++j)
            {
                board[i][j] = toupper(board[i][j]);
                A[board[i][j] - 'A']++;
            }
        }

        for (int i = 0; i < word.length(); ++i)
        {
            word[i] = toupper(word[i]);
            A[word[i] - 'A']--;
            if (A[word[i] - 'A'] < 0)
                return false;
        }
        return true;
    }

    bool isNextValid(vector<vector<char>> board, int x, int y, string word, int count)
    {

        if (board[x][y] == word[count])
        {
            return true;
        }
        return false;
    }

    void findPath(vector<vector<char>> board, string word, bool &flag, vector<vector<int>> &visited, int count, int x, int y)
    {

        if (count == word.length() - 1)
        {
            flag = 1;
            return;
        }

        visited[x][y] = 1;

        count++;

        if (x + 1 < board.size() && !visited[x + 1][y] && isNextValid(board, x + 1, y, word, count))
        {
            findPath(board, word, flag, visited, count, x + 1, y);
        }
        if (x - 1 >= 0 && !visited[x - 1][y] && isNextValid(board, x - 1, y, word, count))
        {

            findPath(board, word, flag, visited, count, x - 1, y);
        }
        if (y + 1 < board[0].size() && !visited[x][y + 1] && isNextValid(board, x, y + 1, word, count))
        {

            findPath(board, word, flag, visited, count, x, y + 1);
        }
        if (y - 1 >= 0 && !visited[x][y - 1] && isNextValid(board, x, y - 1, word, count))
        {
            findPath(board, word, flag, visited, count, x, y - 1);
        }

        visited[x][y] = 0;
    }

    bool exist(vector<vector<char>> &board, string word)
    {
        bool flag = false;

        if (!checkPresent(board, word))
            return false;

        for (int i = 0; i < board.size(); ++i)
        {
            for (int j = 0; j < board[i].size(); ++j)
            {
                if (board[i][j] == word[0])
                {
                    vector<vector<int>> visited(board.size(), vector<int>(board[0].size(), 0));
                    findPath(board, word, flag, visited, 0, i, j);

                    if (flag == true)
                    {
                        return true;
                    }
                }
            }
        }
        return false;
    }
};