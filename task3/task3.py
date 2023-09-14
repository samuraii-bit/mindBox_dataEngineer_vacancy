from pandas import DataFrame
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc

spark = SparkSession.builder.master('local').appName('task3').getOrCreate()

products = DataFrame(data = {'product_id': [1, 2, 3, 4, 5, 6, 7, 8],
                             'product_name' : ['milk', 'cheese', 'yogurt', 'bread', 'melon', 'apples', 'banana', 'cards'],
                             'c_id' : [[1], [1], [1], [2], [3], [3], [3], []]})

categories = DataFrame(data = {'category_id': [1, 2, 3, "None"],
                               'category_name' : ['dairy', 'bakery', 'fruits', "None"],
                               'products' : [[1, 2, 3], [4], [5, 6, 7], []]})

print(products.head(10), '\n\n', categories.head(10))

pDf = spark.createDataFrame(products)
cDf = spark.createDataFrame(categories)
print(pDf.show(truncate=False), cDf.show(truncate=False))

print(pDf.c_id[0])

cond = [pDf.c_id[0] == cDf.category_id]
resultDf = pDf.join(cDf, cond, 'inner').select(pDf.product_name, cDf.category_name)
resultDf = resultDf.union(pDf.join(cDf, cDf.products == pDf.c_id, 'inner').select(pDf.product_name, cDf.category_name))
print(resultDf.show(truncate=False))