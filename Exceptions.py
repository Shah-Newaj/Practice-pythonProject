# cart = 0
#
# if cart != 2:
#     raise Exception("Cart count not matched")
#
# assert (cart == 2)

try:
    with open('test.txt') as reader:
        print(reader.read())

except Exception as e:
    print(e)

finally:
    print("Clearing up resources")