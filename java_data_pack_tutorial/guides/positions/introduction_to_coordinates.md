# Introduction to coordinates

---

## What are coordinates?

Coordinates are used to refer to positions. The minecraft world is 3d, and has three coordinate planes: x, y, and z. Every block has its own x, y and z position.
<!--More info, better wording-->

<!--Something about where they're used in mc, separation by spaces, etc.-->

## Absolute coordinates

Absolute coordinates are the simplest type of coordinates. They are just numbers, and refer to a constant x, y, or z. `0 0 0` refers to the block at `0, 0, 0`.

## Relative coordinates

Absolute coordinates aren't usually very helpful. Usually, you want to refer to coordinates relative to the player. That's why relative coordinates exist. These are a tilde `~` followed by an optional (defaults to 0) number, and mean that for the number, `0` is the executor's position. `~`. These can even be mixed and matched with absolute coordinates
```
~ ~ ~ # The current position
~ ~5 ~3 # 5 blocks up and 3 blocks east
0 ~ 0 # The same y coordinate, at `0, 0`
```

## Local coordinates

Sometimes, even setting the player to the origin isn't enough. You may need to have them aligned to the player's rotation too, so you can specify blocks 'forward' and 'down' instead of at the constant planes. For this, local coordinates can be used. These start with a `^` followed by an optional number, defaulting to 0 like with relative coordinates.

They refer to `^left ^up ^forward`. As an important note, these **cannot be mixed with absolute or relative coordinates** (if you really need to do so, you should look at the [execute command](/java_data_pack_tutorial/pages/execution/introduction_to_execute.html)).
```
^ ^ ^ # Equivalent to `~ ~ ~` (usually, though not always, this will be covered when looking at the execute command)
^ ^ ^5 # 5 blocks forwards of the executor
^3 ^-2 ^ # 3 blocks to the left, and 2 blocks down from the executor.
^ ^ 0 # INVALID
```

<!--Add a quiz-->