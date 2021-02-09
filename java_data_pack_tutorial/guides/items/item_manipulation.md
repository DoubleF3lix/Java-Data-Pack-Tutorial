# Item Manipulation

---

In this lesson, you'll learn basic item manipulation - giving the player itemes, and taking them away.

## Items
To modify items, we first need to know how they're represented in commands. They're quite simple: every item has an identifier, and you just use that. Dirt is `minecraft:dirt`; stone shovels are `minecraft:stone_shovel`; waxed weathered cut copper stairs are `minecraft:waxed_weathered_cut_copper_stairs`. You usually don't need to include `minecraft:` as it is automatically added, so I could have just written `dirt`, say.

You can find an item's id by enabling advanced tooltips (`F3+H`) and hovering over it.

<img src="/java_data_pack_tutorial/images/items/tooltip_hover.png" alt="Image showing using advanced tooltips to find an item's id.">

A more advanced feature of items in commands is specifying an [nbt tag](/java_data_pack_tutorial/pages/nbt/introduction_to_nbt/structure.html), which looks something like `dirt{foo: "bar"}`. However, that will be discussed in a later section.

## Give Command
The first command is `/give`. This command is used to give players particular items - It could be used to give someone a stack of dirt, for instance. Its syntax is as follows:
```
give <targets: selector> <item: item> [count: int]
```
For example, to give yourself a stack of dirt, you could do
```
give @s dirt 64
```
The number here is optional and often omitted; it defaults to one, so
```
give @a diamond_pickaxe
```
gives everyone a diamond pickaxe.

## Clear command
The next command is `/clear`. This command removes certain items from the player - from removing their entire inventory, to removing 5 sand. Its syntax is:
```
clear [targets: selector] [item: item] [count: int]
```
`targets` defaults to `@s`; `item` defaults to everything; and `count` defaults to maximum.

As you can see, you can just run
```
clear
```
which will clear your entire inventory.

You could remove 5 blocks of sand from every player with
```
clear @a sand 5
```

## Item command
The final command we'll look at in this lesson is `/item`. This command is a lot more specific than `/give` or `/clear`, and a lot more complex. In this lesson, we'll look at one basic usage, with the following syntax:
```
item entity <targets: selector> <slot: slot> replace <item> [count: int]
```
`count` defaults to 1.

This will replace a certain slot in the player's inventory with the specified item. There are many different slot selectors; notably
```
inventory.n # The nth slot in the inventory, starting at the top-left at 0.
hotbar.n    # The nth hotbar slot, starting on the left at 0.
armor.      # A certain armor slot on the player
    head
    chest
    legs
    feet
weapon.     # A player's hand.
    mainhand
    offhand
```

For example, to put a stack of snowballs in the player's hand, you could use
```
item entity @s weapon.mainhand replace snowball 64
```