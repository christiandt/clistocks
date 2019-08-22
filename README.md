# clistocks
Simple python 2.7 scripts to get stocks with graphs in cli. Dataset from Financial Times Markets.

## Sample:

Use issueId directly

    print Security("36276")

Or search for it using the Searcher

    print Security(str(Searcher('GOOG')))

Include exchange for better result

    print Security(str(Searcher('TSLA:NSQ')))


## Sample output:
```/usr/bin/python2.7 /Users/christue/Documents/prog/clistocks/main.py
Apple Inc
Current value: 212.46 USD
Latest change: -0.18 (-0.08%)
  213.04  ┤                       
  209.76  ┤     ╭╮             ╭─ 
  206.47  ┼─────╯╰╮      ╭╮  ╭─╯  
  203.19  ┤       ╰╮  ╭╮ ││ ╭╯    
  199.91  ┤        │ ╭╯╰─╯╰─╯     
  196.62  ┤        │╭╯            
  193.34  ┤        ╰╯             

Alphabet Inc
Current value: 1189.53 USD
Latest change: -1.72 (-0.14%)
 1250.41  ┤  ╭╮                   
 1230.70  ┤  │╰─╮                 
 1210.98  ┤  │  ╰─╮   ╭╮ ╭╮  ╭╮   
 1191.26  ┤  │    ╰╮ ╭╯╰─╯│ ╭╯╰── 
 1171.55  ┤  │     ╰─╯    ╰─╯     
 1151.84  ┼──╯                    
 1132.12  ┤                       

Tesla Inc
Current value: 222.15 USD
Latest change: 1.32 (0.59%)
  264.88  ┤╭╮                     
  256.67  ┼╯│                     
  248.47  ┤ │  ╭─╮                
  240.26  ┤ │ ╭╯ ╰─╮ ╭──╮╭╮       
  232.05  ┤ ╰─╯    ╰─╯  ╰╯│  ╭─╮╭ 
  223.85  ┤               ╰──╯ ╰╯ 
  215.64  ┤                       


Process finished with exit code 0
```