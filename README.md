# strjump

A python package to calculate referenced indexes in a string

## Example

    string = [
        '1:',
        strjump.Reference(1),
        ',2:',
        strjump.Reference(2),
        '|',
        strjump.Identifier(1, 'f'),
        'irst|',
        strjump.Identifier(2, 's'),
        'econd|'
    ]
    result = strjump.process(string)
    assert '1:9,2:15|first|second|' == result

And that's it. The `result` string is a character delimited array with three
nodes:
1. 1:9,2:15
2. first
3. second

The first node can be translated as a *dict*: `{1: 9, 2: 15}`. The values in
this *dict* are the indexes in the string `result` to which a jump should be
made. Respectively, these are the first characters in each of nodes 2
('>f<irst') and 3 ('>s<econd').
