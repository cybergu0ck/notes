# Boolean Logic

<br>
<br>

## Logic Gates

<br>

### Nand Gate

Nand gate and Nor Gate are called Universal Gates. All the other gates and chips can be built from Nand gate.

![img](./_assets/nandgate.png)

<br>

### Not Gate (Inverter)

![img](./_assets/notgate.png)

<br>

### And Gate

![img](./_assets/andgate.png)

<br>

#### Or Gate

![img](./_assets/orgate.png)

<br>

### Xor Gate

![img](./_assets/xorgate.png)

<br>

### Multiplexer (Mux)

![MUX](./_assets/mux.png)

<br>

### DeMultiplexer (Dmux)

![MUX](./_assets/demux.png)

<br>
<br>

## Multi-Bit versions of basic gates

Computer hardware is often designed to process multi-bit values—for example, computing a bitwise And function on two given 16-bit inputs.

- HDL programs treat multi-bit values like single-bit values, except that the values can be indexed in order to access individual bits. For example, if `in` and `out` represent 16-bit values, then `out[3] = in[5]` sets the 3rd bit of out to the value of the 5th bit of in. The bits are indexed from right to left, the rightmost bit being the 0’th bit and the leftmost bit being the 15’th bit (in a 16-bit setting).

//TODO - Write a clean explanation with illustration for multi bit version of gates

<br>
<br>

//TODO - Write about HDL and add HDL for all the above gates using Nand
