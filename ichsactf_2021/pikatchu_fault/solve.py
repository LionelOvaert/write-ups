from math import gcd
import gmpy2

N = 14428106165822100311240179104702593030922229606910261061860621459798477042443217675708638511393783602097391544907229222395222465303690975922805833664159517707002845392996861764206707180372733989400577838887924912395532925065643238637812097531657082837158436848594708309238918390308191361234059534178077141595873018313112575974600539522798755895311426362091301356794727864093165846318233065617022292712839240223002241134094765005135404901074586741323378531189871102865921045940469715763216120732916020528427859371641401521785824628585853094123501351577248220567930583676467206786442597142305655569749177107891502253803
e = 65537
M = 0x4c6f766520616e64206b69737365732c206d697373696e6720796f7521000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f404142434445464748494a4b4c4d4e4f505152535455565758595a5b5c5d5e5f606162636465666768696a6b6c6d6e6f707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeafb0b1b2b3b4b5b6b7b8b9babbbcbdbebfc0c1c2c3c4c5c6c7c8c9cacbcccdcecfd0d1d2d3d4d5d6d7d8d9dadbdcdddedfe0e1e2
M_faulty = 0x1a36d7ecad4b18bc765ff0e3d3ecde7cae84bf1cc445a6fdcb48c335d9d3a043817fc014d55bfad94b51eb522b4ff719d33f012afe1498efafe660b97d1cb806d4ff7985a40a14f9bec9d93e2eb20f3820423ba0e34302adc82156673fa164822779174e9b7a84a417873358d1d774ccdfdb1f36de6aa8249b00184aac2feb003782f16fb3f5d7b113387989f662062452793bbaad87014b1ebd4a020342a11a19d95f4d3b29dd5449c57ea0fd3b881542a7b8b0bdbc9dcb7b19337f40e723439365dc29625cb775e91aef886d79d1403725c5aefa21b3d69f8cacbbbafb8b35c86822113e71bd272ca7cdf68da0ab397c658cb6cc14225732bc07726155ecd1

p = gcd(M_faulty - M, N)
q = N // p
phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)
print(f"d: {d}")