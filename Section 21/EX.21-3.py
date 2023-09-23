'''
Hash table
해시테이블
    key, value 로 데이터를 저장하는 자료구조
    각 키는 해시 함수를 사용하여 특정 인덱스(주소)에 매핑
    매핑된 인덱스 값을 저장하거나 검색하여 빠르게 데이터 접근이 가능하다.


'''




class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * self.size
        #[None, None, None, None, None, None, None, None, None, None]
    def hash_function(self, key):
        return hash(key) % self.size #0-9까지의 값, 10이 지정되어 있기에

    def insert(self, key, value):

        # key : 'John Doe'
        # value : '555-555-5555'
        hash_index = self.hash_function(key)
        #print(f'key:{key}')
        #print(f'hash_index: {self. hash_table[hash_index]}')

        if self.hash_table[hash_index] is None:
            self.hash_table[hash_index] = []
        self.hash_table[hash_index].append((key, value))

    def search(self, key):
        hash_index = self.hash_function(key)
        bucket = self.hash_table[hash_index]
        if bucket is None:
            return None
        for k, v in bucket:
            if k == key:
                return v
        return None

# 실행 코드
#print(hash('abc')) #특정의 난수값이 나오게 됨
hash_table = HashTable(10)  # 크기가 10인 hashtable 생성
hash_table.insert('John Doe', '555-555-5555')
hash_table.insert('Jane Doe', '555-555-5556')
hash_table.insert('Jim Doe', '555-555-5557')
hash_table.insert('KoreaIT', '555-555-5558')

print(hash_table.search('John Doe'))
print(hash_table.search('Jane Doe'))
print(hash_table.search('Jim Doe'))
print(hash_table.search('KoreaIT'))