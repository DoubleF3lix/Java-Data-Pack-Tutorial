# Formatting Text

<hr>

In this lesson, you'll learn everything about the structure of JSON text components.

<br>

## Introduction

Raw JSON text is the official format that Minecraft uses to display styled text to players. It is present in the chat, titles, signs, books, entity names, item names, container names, bossbars, advancements, `pack.mcmeta` descriptions...
<!-- FINISH THIS PARAGRAPH  -->

<br>

## Raw String

Raw strings are the simplest method to display messages, they are pure text without any formatting options available. Raw strings are usually surrounded by quotation marks(").

**Examples:**

- `"Hello World!"` -> Hello World!

<br>

## Components

JSON text components are pieces of text with special functionalities. A single component is usually a compound(surrounded by curly brackets "{...}") containing special tags that add special attributes to a text.

```json
{ ... "tag":"value", "tag":"value" ... }
```

Multiple components can be grouped together inside an array(surrounded by square brackets "[...]") to create fancy text with complex formatting.

```json
[ <component>, <component>, <component> ]
```

<!-- NEEDS CONFIRMATION -->
Component arrays[...] can be nested inside component arrays.

```json
[ <component>, [ ... <nested component array> ... ], <component> ]
```
<!-- NEEDS CONFIRMATION -->

<br>

### Content Types

A component can display multiple types of content, however only one type is allowed per component.

<br>

#### Text

The `"text"` tag is used to display plain text. The value usually is a string, however numbers and booleans are also accepted. Without any formatting tag, a component containing only a `"text"` tag is the same as a raw string.

**Examples:**
- `{"text":"Hello World!"}` -> Hello World!
- `["Raw strings and", {"text":" text components."}]` -> Raw strings and text components.

<br>

#### Translation

The `"translate"` tag is used to display text based on the current selected language. It refers to a translation key defined in a [language file](https://minecraft.gamepedia.com/Resource_Pack#Language) in a resource pack. If the current language does not have the referenced value, the translation key will be displayed instead.

**Examples:**
- `{"translate":"block.minecraft.stone"}` -> Stone
- `{"translate":"my.custom.translation"}` -> my.custom.translation

##### With Tag

Using the `"with"` tag it's possible to display external JSON text components in the translated message. 
<!-- INCOMPLETE -->

<br>

#### Keybind

The `"keybind"` tag is used to display a certain key to the player, depending on their options. This is useful for telling them to press a certain key, so that even if they've rebound it, they'll be told the right thing. A list of valid keys is [here](https://minecraft.gamepedia.com/Controls#Configurable_controls).

**Examples**:
- `{"keybind": "key.attack"}` -> Left Button
- `{"keybind": "key.jump"}` -> Space

<br>

### Formatting

As stated earlier, components accept multiple formatting options to enhance the appearance of a text. 

<br>

#### Bold

<br>

#### Italic

<br>

#### Strikethrough

<br>

#### Underlined

<br>

#### Obfuscated

<br>

#### Color

To specify a color to a component, use the `"color"` tag. There are 16 default colors to choose from based on their english names, but since version 1.16 it's possible to use an Hex Color Code to pick any custom color. The default colors are:

<table style="text-align:center;">
    <tr>
        <th>Name</th>
        <th>Hex</th>
    </tr>
    <tr style="background-color:#000000;">
        <td>black</td>
        <td>#000000</td>
    </tr>
    <tr style="background-color:#0000AA;">
        <td>dark_blue</td>
        <td>#0000AA</td>
    </tr>
    <tr style="background-color:#00AA00;">
        <td>dark_green</td>
        <td>#00AA00</td>
    </tr>
    <tr style="background-color:#00AAAA;">
        <td>dark_aqua</td>
        <td>#00AAAA</td>
    </tr>
    <tr style="background-color:#AA0000;">
        <td>dark_red</td>
        <td>#AA0000</td>
    </tr>
    <tr style="background-color:#AA00AA;">
        <td>dark_purple</td>
        <td>#AA00AA</td>
    </tr>
    <tr style="background-color:#FFAA00;">
        <td>gold</td>
        <td>#FFAA00</td>
    </tr>
    <tr style="background-color:#AAAAAA;">
        <td>gray</td>
        <td>#AAAAAA</td>
    </tr>
    <tr style="background-color:#555555;">
        <td>dark_gray</td>
        <td>#555555</td>
    </tr>
    <tr style="background-color:#5555FF;">
        <td>blue</td>
        <td>#5555FF</td>
    </tr>
    <tr style="background-color:#55FF55;">
        <td>green</td>
        <td>#55FF55</td>
    </tr>
    <tr style="background-color:#55FFFF;">
        <td>aqua</td>
        <td>#55FFFF</td>
    </tr>
    <tr style="background-color:#FF5555;">
        <td>red</td>
        <td>#FF5555</td>
    </tr>
    <tr style="background-color:#FF55FF;">
        <td>light_purple</td>
        <td>#FF55FF</td>
    </tr>
    <tr style="background-color:#FFFF55;">
        <td>yellow</td>
        <td>#FFFF55</td>
    </tr>
    <tr style="background-color:#FFFFFF;">
        <td>white</td>
        <td>#FFFFFF</td>
    </tr>
</table>
<!-- TABLE NEEDS A REWORK -->


**Examples:**

- `{"text":"I'm red.", "color":"red"}` -> <span style="color:#FF5555;">I'm red.</span>
- `[{"text":"I'm green", "color":"green"}, {"text":" and blue.", "color":"blue"}]` -> <span style="color:#55FF55;">I'm green</span><span style="color:#5555FF;"> and blue.</span>
- `{"text":"I'm a custom color using an Hex code.",  "color":"#748A9E"}` -> <span style="color:#748A9E;">I'm a custom color using an Hex code.</span>

<br>

<br>

<hr>

<br>

## Tips

- When working with colored item names, it's recommended to insert an empty string in the beginning of the array to prevent the color from leaking to the parent text component whenever the item is referenced.
**Example:** `{"text":"foobar", "color":"gold"}` -> `["", {"text":"foobar", "color":"gold"}]`
<!-- WRITE MORE TIPS -->