# INDEX  
- [INDEX](#index)
      - [DOCS](#docs)
    - [NUMPY](#numpy)
#### DOCS  
### NUMPY  
the difference between `numpy array` and a `list`:  
| NUMPY ARRAY | LIST |  
| ---- | ---- |  
| Fixed size block of contiguous memory | scattered in memory with pointer links |  
| single block of RAM with no gaps | various blocks in RAM w/ pointers to the next element |  
| __n__ elements with excatly __m__ bytes | vary bytes |  
| use byte offset to index | need to start at head of list to follow link chains to wanted index |  

:::mermaid
block-beta
db(("DB"))
  blockArrowId6<["&nbsp;&nbsp;&nbsp;"]>(down)
  block:ID
  1
  2
  3
  4
  end
:::  
:::mermaid
block-beta
1 space 2
1-->2
:::