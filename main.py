def fill_spiral_clockwise(n):
    matrix = [[0] * n for _ in range(n)]
    #Bu qator n x n o'lchamdagi bo'sh (faqat 0 lardan iborat) matritsa yaratadi.
    num = 1
    top, bottom, left, right = 0, n - 1, 0, n - 1
     #top, bottom, left, right — chegaralarni belgilaydigan o'zgaruvchilar:
    while top <= bottom and left <= right:
        # Chapdan o'ngga
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
    #Bu qism yuqori (top) qatorni chapdan o'ngga to'ldiradi va keyin yuqori chegarani (top) bir qator pastga tushiradi.


        # Yuqoridan pastga
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
    #Bu qism pastki (bottom) qatorni o'ngdan chapga to'ldiradi va keyin pastki chegarani (bottom) bir qator yuqoriga ko'taradi.
        # O'ngdan chapga
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
      #Bu qism pastki (bottom) qatorni o'ngdan chapga to'ldiradi va keyin pastki chegarani (bottom) bir qator yuqoriga ko'taradi.
        # Pastdan yuqoriga
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    #Bu qism chap (left) ustunni pastdan yuqoriga to'ldiradi va keyin chap chegarani (left) bir ustun o'ngga siljitadi.
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{x:3}" for x in row))
   #Har bir satr uchun matritsadagi qiymatlar ketma-ket joylashtiriladi.
if __name__ == "__main__":
    n = 7

    matrix = fill_spiral_clockwise(n)
    print_matrix(matrix)

# yangilandi



