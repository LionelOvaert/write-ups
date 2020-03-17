# b01lers CTF – Scrambled

* **Category:** Web
* **Points:** 200

## Challenge

> I was scanning through the skies. And missed the static in your eyes. Something blocking your reception. It's distorting our connection. 
> With the distance amplified. Was it all just synthesized? And now the silence screams that you are gone. You've tuned me out. I've lost 
> your frequency.
> 
> web.ctf.b01lers.com:1002

## Solution
Visiting the website only gives us a Youtube integration of an album of Starset. The source code contains nothing suspicious so I looked further. When looking at the cookies, we see that 2 cookies are defined:

*frequency=1*

*transmissions=kxkxkxkxsh_t14kxkxkxkxsh*

When looking at transmission, we see that there is something hidden in the garbage. Performing more requests show us that frequency has no effect but transmissions is loaded randomly with different values. When performing enough requests, we see that some parts seem to come back. We can thus deduce that it prints a part of the flag with a number corresponding to the position of this part in the whole flag.

I wrote a [script](solve.py) that performs requests and fills a map. I know that there were 68 parts because when reloading my page some times during my tests, I came across a transmissions cookie containing *kxkxkxkxshs%7D67* and another one containing *pc0kxkxkxkxsh*.

After saving these results in a [file](transmissions), I wrote a small [script](cut_transmissions.py) to print the flag.

```
pctf{Down_With_the_Fallen,Carnivore,Telescope,It_Has_Begun,My_Demons}
```