# meal-tagger
A python module for interfering ingredients of meals based on their descriptions.

[![Build
Status](https://travis-ci.org/hladny-matfyzak/meal-tagger.svg?branch=master)](https://travis-ci.org/hladny-matfyzak/meal-tagger)

## Example

This module can be used in the following way:


    import mealtagger as mt
    for tag in mt.tag('Vypr.syr 130g')
        print tag,
    # vyprážaný syr

    for tag in mt.tag('Palacinky s džemom 350g')
        print tag,
    # palacinka džem
