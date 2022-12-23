# --------------------------------------------------------------------------------------------------------
# Slice list into 3 equal chunks and reverse each chunk
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
n=3
x = list(divide_chunks(sample_list,n))
print("Chunk_1",x[0])
print(x[0][::-1])
print("Chunk_2",x[1])
print(x[1][::-1])
print("Chunk_3",x[2])
print(x[2][::-1])