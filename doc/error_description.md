# ERROR DESCRPTION

## [Err## 1]

```
[Err## 1] amino acid '.' unknown. Please check your fasta file or your
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
