

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 1}


def displayInventory(inv):
    print('Inventory:')
    item_total = 0
    for k, v in inv.items():
        print(k, end=": ")
        print(inv[k])
        item_total = item_total + inv[k]
    print('Total number of items: ' + str(item_total))


def addToInventory(inv, addedItems):
    itemHolder = []
    wat = ''

    for v in addedItems:
        for k in inv.keys():
            if v != k and v != wat:
                itemHolder.append(v)
                wat = v
            else:
                break

    for i in range(0, len(itemHolder)):
        inv[itemHolder[i]] = 0

    for v in addedItems:
        for k in inv.keys():
            if v == k:
                print()
                inv[k] = inv[k] + 1
                break
            


inventory2 = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby']

addToInventory(inventory2, dragonLoot)

displayInventory(inventory2)

