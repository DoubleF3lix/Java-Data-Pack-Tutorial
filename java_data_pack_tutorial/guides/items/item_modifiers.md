# Item Modifiers

---

This lesson will look into the `item` command in more detail.

## Block Slots
Player's aren't the only thing with inventories: many blocks have inventories too, like chests, furnaces, and hoppers. The item command works on those too. Last lesson had the syntax
```
item entity <targets: selector> ...
```
But, we can also write
```
item block <target: coordinates> ...
```
which will manipulate items in the block at the target coordinates. Last lesson also discussed slots for players, but these blocks have other slots (it would't make sense for a chest to have `armor.head`): `container.n`. This will select the nth slot in the container, and works similarly to `inventory.n`. For example, to put a diamond in the center of a chest at `0, 0, 0`, you could do
```
item block 0 0 0 container.13 replace diamond
```
Of course, relative and local coordinates work too, so you could have done
```
item block ~ ~ ~ container.13 replace diamond
```
to select the chest the player is standing on (chests don't have full height hitboxes, so when you stand on top of it, you're actually in the block).

## Other slots
As well as the previously mentioned slots, there are a few more slots (remember, the command can target non-player entities):
```
horse.saddle # Replaces a horse's (or donkey, or mule) saddle slot
horse.chest  # Replaces a donkey or mule's chest
horse.armor  # Replaces a horse's or llama's armor slot
horse.n      # Replaces the nth slot in a donkey/mule's chest
villager.n   # Replaces the nth slot in a villager's inventory
enderchest.n # Replaces the nth slot in a player's enderchest
```
These are useful sometimes, though a lot less widely used.

## Item Copy
`replace` isn't the only thing you can do with `/item`. While it's useful, it doesn't help if you want to set an **unknown item**. For example, what if you wanted to set the middle slot of a chest to be what the player was holding?

The syntax is
```
item <target: block|entity> ... <slot: slot> copy <from: block|entity> ... <from_slot: slot> [modifier: item_modifier]
```
(You can ignore the optional modifier for now).

It's all the same up until `copy`. Then, you specify a place to copy from as if we had started a new `/item` command. To copy the item in our hand to the middle slot (`container.13`) of a chest, you could do
```
item block ~ ~ ~ container.13 copy entity @s weapon.mainhand
```
or, to put a helmet on from the first slot of an enderchest, you could do
```
item entity @s armor.head copy entity @s enderchest.0
```
Remember, the first section in the command specifies the *destination*, the second part selects what will be put there.

## Item Modifiers
Sometimes you might want to manipulate the item in the inventory itself. You don't want to replace it with something hardcoded, you don't want to copy it from somewhere. This could be setting its name; enchanting it; setting a compass's location... there are many possibilities. This is where item modifiers help.

Item modifiers go in the `item_modifiers` folder in your datapack. They're JSON files and can be used with the `item` command. They have a syntax like so:
```json
{
    "function": "<function_name>",
    "other paramaters": "to the function"
}
```
Alternatively, you can have a list of functions:
```json
[
    {
        "function": "<function a>",
        "foo": "bar"
    },
    {
        "function": "<function b>",
        "quux": 3
    }
]
```
There are many different function types, and for a full list you can check [the wiki page](https://minecraft.gamepedia.com/Item_modifier). This lesson will look at a few common ones.

Before going into more detail about item modifiers, you need to know how to use them. They `item` command has one further modifier )(instead of `replace` or `copy`), `modify`. Its syntax is
```
item ... modify <modifier: item_modifier>
```
`modifier` is a namespaced identifier that references your item modifier. The command will run the modifier on the stack, and put the resulting item back into the same slot. For example, if you had a modifier `foo:bar`, which set the name of an item to "John", you could run
```
item entity @s weapon.mainhand modify foo:bar
```
to set the item in your mainhand to have the name "John". It doesn't matter which item it is, and it will keep other data (like enchantments).

Alternatively, you can specify a modifier at the end of the `copy` subcommand (as seen in the syntax above), which will run the modifier on the item being copied. It's equivalent to copying the item then running `item ... modify` on the slot, but more compact. For example, to copy the item in your offhand into a chest, but modified with modifier `foo:quux`, you could do
```
item block ~ ~ ~ container.0 copy entity @s weapon.offhand foo:quux
```

### Number Providers
Item modifieres often require numbers, e.g in `set_count`, you need to specify a count to set (or add). These places (usually) accept **number providers**, which are small objects that output a number. The most simple one is:
```json
{
    "type": "constant",
    "value": <int>
}
```
which would output a constant number here. Note, in this situation, you **don't need an object**. You can simply write `3` in the place of a number provider.

There are random ones too,
```json
{
    "type": "uniform",
    "min": <number provider>,
    "max": <number provider>
}
```
would output a uniformly-chosen random number from `min` to `max` (like a dice).
```json
{
    "type": "binomial",
    "n": <number provider>,
    "p": <number provider>
}
```
outputs a random number following the [binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution) with `n` trials, and a `p` chance of success of a trial. (For example, setting `n` to 10 and `p` to 0.5 would be like flipping a coin ten times and counting the heads).

## Commonly-used modifiers
### Set count
`set_count` will change the number of items in a stack. It looks as follows:
```json
{
    "function": "set_count",
    "count": <number provider>,
    "add": <bool>
}
```
`add` is optional (defaulting to `false`), and will add to the current stack size instead of ignoring it. For example, to add 1 to a stack, you could do
```json
{
    "function": "set_count",
    "count": 1,
    "add": true
}
```
or to set a stack to have a random number of items from 1 to 64, you could do
```json
{
    "function": "set_count",
    "count": {
        "type": "uniform",
        "min": 1,
        "max": 64
    }
}
```
### Set name
`set_name` can set the name of an item.
```json
{
    "function": "set_name",
    "name": <json_component>,
    "entity": "this"
}
```
`name` here is a [json component](/java_data_pack_tutorial/pages/text/formatting_text.html) which will be the name of the item. `entity` is something for a later section (about loot tables), but it can be set to `this` for now (it controls what `@s` will be in the json component).

### Set nbt
`set_nbt` can be used to set arbritrary [nbt](/java_data_pack_tutorial/pages/nbt/introduction_to_nbt/structure.html) on an item.
```json
{
    "function": "set_nbt",
    "nbt": <nbt: string>
}
```
`nbt` is a string containing the nbt to set. Remember to escape quotes (`"`) in the nbt with backslashes, e.g `"{foo:\"bar\"}"`.