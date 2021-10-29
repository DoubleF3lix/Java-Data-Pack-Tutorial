# Getting started

## Initial Startup


### Before Starting
You should be familiar with your system and file explorer, be comfortable with creating, renaming, opening, and editing both files and folders, and own a legal copy of Minecraft. If you don't own a copy of minecraft, you can get one [here](https://www.minecraft.net/en-us/store/minecraft-java-edition).


### Enabling File Extensions
Enabling file extensions will allow to you create functions that aren't secretly `.txt` files. On Windows 10, you can find this in the "View" tab. <br><br>![Enabling File Extensions](/Java-Data-Pack-Tutorial/images/enableFileExtensions.png)

    
## Text Editors
    
Most text editors like Notepad should work for creating functions. However, it is recommended you use Visual Studio Code, which you can get [here](https://code.visualstudio.com/). It has extensions that have features such as auto-complete, syntax highlighting, and code snippets.


### Installing Visual Studio Code Extensions (Optional)
The first one is language-mcfunction by <a class="textLink" href="/Java-Data-Pack-Tutorial/images/mondaysBeLike.png">Arcen</a>soth, which you can get [here](https://marketplace.visualstudio.com/items?itemName=arcensoth.language-mcfunction), or by clicking the extensions button in your toolbar (it looks like a grid of four with one block coming off) and searching for "language-mcfunction". This extension enables syntax highlighting for minecraft functions.

The second extension is Datapack Helper Plus by SPGoding which you can get [here](https://marketplace.visualstudio.com/items?itemName=SPGoding.datapack-language-server), or by clicking the extensions button in your toolbar and searching for "data-pack helper plus". This extension helps with auto-completion, command syntax, code snippets, and all sorts of other features.

---
# Activity 1 - Creating your first Datapack
Datapack structure will be discussed more in-depth in the next lesson, but here we'll setup the very basics.

First, go to your game files. For Windows users, by default, this is in `C:\Users\<USERNAME>\AppData\Roaming\.minecraft`. This directory can be accessed on Windows 10 by typing `%appdata%` in your search bar, and then going into the `.minecraft` folder. It is recommended you create a shortcut here and place it somewhere you'll remember for easy access later.

Go into your world (preferably an unimportant world) and in the `datapacks` folder, create a new folder with any name. Inside of that folder, create a new file named `pack.mcmeta`(replacing any extensions, if present) and a new folder which should be named `data`. The `data` folder holds all of the namespaces for your datapack. You can have as many namespaces as you'd like, but for this course, we'll only use the `minecraft` namespace and a single namespace with a name of your choosing.

Open `pack.mcmeta` and add the following lines:
```json
{
  "pack": {
    "pack_format": 7,
    "description": "Datapack description"
  }
}
```
Depending on your version, you may need to edit the `pack_format`. See the table below.
<table>
    <tr>
        <th>Version</th>
        <th>Pack Format</th>
    </tr>
    <tr>
        <td>1.13 to 1.14</td>
        <td>4</td>
    </tr>
    <tr>
        <td>1.15 to 1.16.1</td>
        <td>5</td>
    </tr>
    <tr>
        <td>1.16.2 to 1.16.5</td>
        <td>6</td>
    </tr>
    <tr>
        <td>1.17+</td>
        <td>7
    </tr>
</table>

By adding the `pack.mcmeta` file with the text entered, Minecraft will recognize the folder as a datapack. 
Enter your world and type `/datapack list` in chat. If you were already in the world, type `/reload` before typing `/datapack list`. Note that the `data` folder is not required to make a datapack, but it is required for all content. <br>
If you see something like `[vanilla (built-in)], [file/<DATAPACK NAME> (world)]`, then you did it! If not, you can download a sample datapack [here](/Java-Data-Pack-Tutorial/samples/unit1/lesson1.zip) to compare.