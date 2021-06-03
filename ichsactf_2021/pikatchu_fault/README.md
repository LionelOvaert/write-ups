# ICHSACTF 2021 – Pickatchu's fault

* **Category:** Fault injection
* **Points:** 100

## Challenge

<blockquote>

I have a pretty weird girlfriend, she gave me a device to decrypt her secret messages to me. She said not to worry it is an efficient RSA implementation using CRT - whatever.

One time my pikatchu got an uncommon cold and sneezed exacty when I fed her secret message to the decryptor. I got unreadable nonsense as a result I suspect it's my pikatchu's fault for having an electric sneeze and it confused the decryptor. My confidence about it raised after I tried to decrypt again and got a readable message.

I wonder though if it is possible to get the private key from that faulty message.
</blockquote>

<pre><strong>N</strong>:
1442810616582210031124017910470259303092222960691026106186062145979847704244321767570863851139
3783602097391544907229222395222465303690975922805833664159517707002845392996861764206707180372
7339894005778388879249123955329250656432386378120975316570828371584368485947083092389183903081
9136123405953417807714159587301831311257597460053952279875589531142636209130135679472786409316
5846318233065617022292712839240223002241134094765005135404901074586741323378531189871102865921
0459404697157632161207329160205284278593716414015217858246285858530941235013515772482205679305
83676467206786442597142305655569749177107891502253803

<strong>e</strong>:65537

<strong>M</strong>:
4c6f766520616e64206b69737365732c206d697373696e6720796f7521000102030405060708090a0b0c0d0e0f1011
12131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f40
4142434445464748494a4b4c4d4e4f505152535455565758595a5b5c5d5e5f606162636465666768696a6b6c6d6e6f
707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e
9fa0a1a2a3a4a5a6a7a8a9aaabacadaeafb0b1b2b3b4b5b6b7b8b9babbbcbdbebfc0c1c2c3c4c5c6c7c8c9cacbcccd
cecfd0d1d2d3d4d5d6d7d8d9dadbdcdddedfe0e1e2

<strong>M`</strong>:
1a36d7ecad4b18bc765ff0e3d3ecde7cae84bf1cc445a6fdcb48c335d9d3a043817fc014d55bfad94b51eb522b4ff7
19d33f012afe1498efafe660b97d1cb806d4ff7985a40a14f9bec9d93e2eb20f3820423ba0e34302adc82156673fa1
64822779174e9b7a84a417873358d1d774ccdfdb1f36de6aa8249b00184aac2feb003782f16fb3f5d7b113387989f6
62062452793bbaad87014b1ebd4a020342a11a19d95f4d3b29dd5449c57ea0fd3b881542a7b8b0bdbc9dcb7b19337f
40e723439365dc29625cb775e91aef886d79d1403725c5aefa21b3d69f8cacbbbafb8b35c86822113e71bd272ca7cd
f68da0ab397c658cb6cc14225732bc07726155ecd1
</pre>

## Solution

In this challenge, we are provided with a hint about the type of encryption we are facing: RSA-CRT, i.e. RSA with chinese remainder theorem optimization. A detailed explanation about how this works can be found [here](https://crypto.stackexchange.com/a/2580).

Let's now look at the 4 different values we received:
1. N: the modulus of the RSA encryption,
1. e: the exponent of the public key,
1. M: a hexadecimal representation of the message
1. M`: a hexadecimal representation of the faulty message.

<br>
The message M can be decoded to ascii as it is a correctly decrypted message:
<pre>
Love and kisses, missing you!	

 !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâ
</pre>

However as M is a faulty message, trying to convert it back to ascii results in gibberish!
As this is a fault injection challenge, there must be something to do with those two messages that can allow us to retrieve d (the exponent of the private key)...
This is exactly where RSA-CRT fault attack comes in hand!
<br>

The fault attack requires e, N, a valid message m and a faulty message (i.e. a bad decryption of the same message m), which looks just like all we were given for this challenge, awesome! Let's dig into the attack.
<br>
When decrypting a message, the CRT optimization computes M such that

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>m</mi>
  <mo>&#x2261;<!-- ≡ --></mo>
  <mo stretchy="false">(</mo>
  <msup>
    <mi>M</mi>
    <mi>d</mi>
  </msup>
  <mo lspace="thickmathspace" rspace="thickmathspace">mod</mo>
  <mi>N</mi>
  <mo stretchy="false">)</mo>
  <mspace width="0.667em" />
  <mi>mod</mi>
  <mspace width="thinmathspace" />
  <mspace width="thinmathspace" />
  <mi>p</mi>
</math>
<br>
<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi>m</mi>
  <mo>&#x2261;<!-- ≡ --></mo>
  <mo stretchy="false">(</mo>
  <msup>
    <mi>M</mi>
    <mi>d</mi>
  </msup>
  <mo lspace="thickmathspace" rspace="thickmathspace">mod</mo>
  <mi>N</mi>
  <mo stretchy="false">)</mo>
  <mspace width="0.667em" />
  <mi>mod</mi>
  <mspace width="thinmathspace" />
  <mspace width="thinmathspace" />
  <mi>q</mi>
</math>
<br><br>
This is where things went wrong with our faulty message, one of these conditions is not valid which means our message M has been computed with only one of the primes p or q. That means we can recover one of these by taking the difference between M` and M and find its greatest common divisor with N. After recovering p, we get q very easily as N is simply the product of p and q.

```python
p = gcd(M_faulty - M, N)
q = N // p
```


Using p and q, we can now compute phi which is necessary to compute d. D is the [modular multiplicative inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse) of e modulo phi. I used the python package gmpy2 to compute this.

```python
phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)
```


We have successfully retrieved the exponent of the private key, YEY! All we have to do know is to recompose the private key in PEM format using n, d and e. The best tool I know for this is [rsatool](https://github.com/ius/rsatool).

```sh
$ python3 rsatool.py -f PEM -o key.pem \
-n 14428106165822100311240179104702593030922229606910261061860621459798477042443217675708638511393783602097391544907229222395222465303690975922805833664159517707002845392996861764206707180372733989400577838887924912395532925065643238637812097531657082837158436848594708309238918390308191361234059534178077141595873018313112575974600539522798755895311426362091301356794727864093165846318233065617022292712839240223002241134094765005135404901074586741323378531189871102865921045940469715763216120732916020528427859371641401521785824628585853094123501351577248220567930583676467206786442597142305655569749177107891502253803 \
-d 13927260208160851273168991722564283386822742716211558894905574481434476015976362003153636716782787406135239390175338130631041451394511474721585404416773111512281825613802393593347951685990202444992284591051282570272765062567751385670770235348699061208848696643358689550316194748122080685633902593209538369648020016950725241914128427426181200853813780280418534945324283000328195029549077883174468731375021652886332921294680654036771136340708646981474467045117633333235082327437009829103951133021935022509161321697315036893038044551865404678468781999558076673840626279900650444816785725034016769360917075634274855065281 \
-e 65537
```


We get a base64 encoded file. Decoding it uncovers the flag for us.

```
0rJ5zo	>ϳaWVF;-޸H>eO22yJjdHw^O$VŮj]ЋZޖA>VA0?v MYS52fug9d&z1BđT\6` =[2ɶ'>:gq7.+fJV&~*7^#[|uMJL`IS˼	Ɔ3ϔO ltL1`6da$*nS=,ѢLv
۾uLs	tJ!8'~oYD9%2s\WJVK`YdłO7^
{S'7ۏи9EyYb0zeWaӷrY!Ls6O,D//Yai9vU_-CH7TԒ$s/NZ)Ap!k-+Ύ5ܯڣ=EG<qǪ_@#X	0ȖF	3.O7eF|@M>-pZGdwiTsiuS8.BuhcUny9
<J)G3 @w	֩G7{x<6^5Iz$hICHSA_CTF{***_*****_****_****_*_*****_****_***}	

 !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMOQf!|r[gIfmq{|x3Qf=[&N;:t.Z\
Oе'e|!U=vH݇pn
qRG@z{t$FΆa*9O7g|"V<Ot`ͷī*@E[hϝ([w0a-PN^&W#FDTwu녨M	<:Jmk{Cu20@cbA>a3Pv;a!mA;F7b
=8ZmRaX+IS"^l17.W@ZcM(&S5slMbTsfk
```

The whole python script can be found [here](solve.py)

<details>
<summary>Flag</summary>
<pre>ICHSA_CTF{who_needs_more_than_1_fault_with_crt}</pre>
</details>