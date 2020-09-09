import time


def read_file(filename):
    count = 0 
    data = []
    with open(filename, 'r') as f:
    	for line in f:
    		data.append(line)
    		count += 1
    		if count % 1000 == 0: # %為求餘數的功能
    			print(len(data))
    print('檔案總共有', len(data), '筆資料')
    return data


# 計算每筆留言的平均長度
def my_avg_length(data): # 我的作法 去除空格
    length = 0
    for d in data:
         length += len(d.split())
    print(length / count)


def teachers_avg_length(data):# 老師的作法
    sum_len = 0
    for d in data:
    	sum_len += len(d)
    print('平均是', sum_len / len(data))


def length_less_than_100(data):
    new = []
    for d in data:
    	if len(d) < 100:
    		new.append(d)
    print('一共有', len(new), '筆留言長度小於100個字母')
    print(new[0].strip())


def comment_mentioned_good(data):
    good = []
    for d in data:
    	if 'good' in d:
    		good.append(d)
    print('一共有', len(good), '筆留言提到"good"')


# 清單篩選快寫法 "list comprehension"
def list_comprehension(data):
    good = [d for d in data if 'good' in d]
    print('一共有', len(good), '筆留言提到"good"')

    bad = ['bad' in d for d in data]
    print(bad)


# 利用dict做文字的計數 找出最常出現的單字
# 文字計數
def words_count(data):
    wc = {} # word_count
    for d in data:
        words = d.split()
        for word in words:
            if word in wc:
                wc[word] += 1
            else:
                wc[word] = 1

    for word in wc:
        if wc[word] > 1000000:
            print(word, wc[word])
    return wc


def google_word(wc):
    while True:
        word = input('請輸入想查找次數的單字: ')
        if word == 'q':
            break
        if word in wc:
            print(word, '出現過的次數為: ', wc[word], '次。')
        else:
            print(word, '沒有出現過喔!')
    print('感謝使用本查詢功能。')


def main():
    data = read_file('reviews.txt')
    teachers_avg_length(data)
    length_less_than_100(data)
    comment_mentioned_good(data)
    wc = words_count(data)
    google_word(wc)


main()