this challenge is provided with a Nintendo DS rom with a breakout game inside

you can actually play the game, and you can notice how the first map is similar to an "f", so you can try completing it when you realize that the second one is an "l"

at this point is unlikely that a human can finish this game so in desmume we have the RAM search in the tools where we can search for the lives (5, 4, 3 ..) and then enable a cheat to have infinte lives

example:
```
lives_addr = 0x02060DB8
```

next we realize that after the 'g' of "flag" the game restart from the beginning, so we search for the map number in memory ('f' is level 0 and after 'g' is level 5 so we are going to seach level 6)

```
level_addr = 0x02060DBA
```

now we play the maps changing the cheat every time until we have the complete flag

```
flag{Br3Ak0U7!!1}
```
