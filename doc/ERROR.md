# ERROR DESCRIPTION

> ## Menu
> 
> **[[Err## 1]](#err-1)**
> 
> **[[Err## 2]](#err-2)**
> 
> **[[Err## 3]](#err-3)**
> 
> **[[Err## 4]](#err-4)**
> 
> **[[Err## 5]](#err-5)**
> 
> **[[Err## 6]](#err-6)**
>
> **[[Err## 7]](#err-7)**
>
> **[[Err## 8]](#err-8)**


## [Err## 1]

```
[Err## 1] Amino acid '.' unknown. Please check your fasta file or your
input sequence.
```

In your input sequence (terminal or a `.fasta`/`.fa` file), there's a one letter
code that is not in the classical list. It could be a letter that the program
don't take in consideration, or a other character put here by error. Next here,
you can see the classical amino acid (in one *letter code* format) implemented
(21):

| Amino acid                       | One letter code |
| :------------------------------- | :-------------: |
| **Alanine**                      |        A        |
| **Arginine**                     |        R        |
| **Asparagine**                   |        N        |
| **Aspartic acid (or aspartate)** |        D        |
| **Cysteine**                     |        C        |
| **Glutamic acid (or glutamate)** |        E        |
| **Glutamine**                    |        Q        |
| **Glycine**                      |        G        |
| **Histidine**                    |        H        |
| **Isoleucine**                   |        I        |
| **Leucine**                      |        L        |
| **Lysine**                       |        K        |
| **Methionine**                   |        M        |
| **Phenylalanine**                |        F        |
| **Proline**                      |        P        |
| **Selenocysteine**               |        U        |
| **Serine**                       |        S        |
| **Threonine**                    |        T        |
| **Tryptophan**                   |        W        |
| **Tyrosine**                     |        Y        |
| **Valine**                       |        V        |

> **NOTE :** The `upper()` python method from string is actually used. Which
> mean that `'a'` and `'A'` are equivalent.

## [Err## 2]

```
[Err## 2] Given sequence too short.
```

You actually give in input a sequence that is too short. It should at least be
2 amino acids long. Extend your sequence too keep processing.

## [Err## 3]

```
[Err## 3] The '.fasta' file ('.') is in the wrong format.
```

You actually input a fasta file that have a wrong format. Please, respect the
next one:

```fasta
>sequence_1
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
>sequence_2
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

With all "X" representing a classical amino acid (see the list upper, in
**[[Err## 1]](#err-1)**).

## [Err## 4]

```
[Err## 4] Unexpected result of the 'snake drag'. Please, restart the simulation.
```

An error that should never occur. If that the case, please **signal it**!

## [Err## 5]

```
[Err## 5] The maximal temperature is inferior to the minimal one. Please, invert
value.
```

In the given parameters, the maximal temperature is actually inferior to the
minimal one. To correct it, simply invert the value.

## [Err## 6]
```
[Err## 6] The temperature only accept positive integer.
```

You actually give one temperature that is inferior or equal to 0. Value should
be strictly superior to 0. Please change the given value.

### [Err## 7]

```
[Err## 7] A probability should be include in [0, 1].
```

Actually, math define that a probability have to be superior to 0 and inferior
to 1. So, if you give a probability not include in that interval, an error is
throw.

### [Err## 8]

```
[Err## 8] Number of step should at least be 1.
```

Do to the Monte Carlo algorithm, you actually need to do **AT LEAST** one step.
So you have to give in arguments a value > 0.