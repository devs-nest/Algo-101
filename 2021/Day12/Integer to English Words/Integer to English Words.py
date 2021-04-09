class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
            'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        thousand = 'Thousand Million Billion'.split()

        def word(num, idx=0):
            if num == 0:
                return []
            if num < 20:
                return [to19[num-1]]
            if num < 100:
                return [tens[num//10-2]] + word(num % 10)
            if num < 1000:
                return [to19[num//100-1]] + ['Hundred'] + word(num % 100)

            p, r = num//1000, num % 1000
            space = [thousand[idx]] if p % 1000 != 0 else []
            return word(p, idx+1) + space + word(r)
        return ' '.join(word(num)) or 'Zero'
