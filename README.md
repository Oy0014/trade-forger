<div align="center">
    <img src="https://user-images.githubusercontent.com/84878036/227357445-aaf2dfc4-e89d-4cae-aa30-d3d3621ac2b5.png" width=80% /> 
</div>


# Usage

Before attempting to use the forger, you should understand what each text area means, and how it will be rendered:

| Name | Functionaliy |
|:----------:|-------------|
| Victim Username | The username of the other trader |
| Attacker Limited ID's | The limtiteds you are "trading" to the other trader, when supplied limited ID's |
| Victim Limited ID's | The limiteds the other trader is "trading" for your limtiteds, when supplied limited ID's |

---

> ## Limited ID's?
> You can find the ID of a limited via [Rolimons](https://rolimons.com), search the limited you want the id to, and copy the set of numbers at the end of the URL
> 
> `https://www.rolimons.com/item/1530795` -> `1530795`
>

---

## Serials
If your limited has a serial on it, prefix the limited ID with an "s":

`494291269` -> `s494291269`

---

## Multiple items

If you want an certain side of the trade to have multiple limiteds, seperate them by a comma:

`s494291269 and s2409285794` -> `s494291269,s2409285794`


# Installation

- Clone the git repository
- Run: `pip install -r requirements.txt`
- `cd` into the `src/` directory
- Run `python main.py`
- You now have a local forger running on `http://127.0.0.1:3000`
