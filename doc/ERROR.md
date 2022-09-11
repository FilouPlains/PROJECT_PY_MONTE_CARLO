# ERROR DESCRPTION

> ## Navigation menu
> 
> **[[Err## 1]](#err-1)**
> 
> **[[Err## 2]](#err-2)**
> 
> **[[Err## 3]](#err-3)**
> 
> **[[Err## 4]](#err-4)**


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
