# 複製List,避免原本的List被更動
L = ["hello", "world"]
L2 = L.copy()  # 使用copy()複製List
print(L2)  # ["hello", "world"]
L2[0] = "python"  # 修改複製後List的索影0資料
print(L)  # ["python", "world"]原本的List不影響
print(L2)  # ["python", "world"]複製後的List可以影響
# 這跟變數的=賦値不同,一般情況下會開2個記憶體空間
# 在List的情況下使用=會讓兩個變數名稱指向同一個記憶體空間
# 這導致修改一個List會影響到另一個List
# 所以在需要複製List時,應該使用copy()方法

# remove()刪除指定位置的資料
L = ["hello", "world", "python"]
L.remove("world")  # 移除"world"
print(L)  # ["hello", "python"]

# pop()刪除最後一個資料
L = ["hello", "world", "python"]
# 不給索引時,pop()會刪除最後一個資料
L.pop()  # 刪除最後一個資料
print(L)  # ["hello", "world"]
s = L.pop(1)  # 刪除索引1的資料
print(s)  # world
print(L)  # ["hello"]
