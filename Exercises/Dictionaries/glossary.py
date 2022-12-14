# Creating a glossary with 5 words related to computing:

glossary = {
    'recursion':'noun. Recursion means "defining a problem in terms of itself". This can be a very powerful tool in writing algorithms. Recursion comes directly from Mathematics, where there are many examples of expressions written in terms of themselves. For example, the Fibonacci sequence is defined as: F(i) = F(i-1) + F(i-2) ',
    'data':'noun. Data are facts and statistics collected together for reference or analysis.',
    'vector':'noun. A quantity having direction as well as magnitude, especially as determining the position of one point in space relative to another.',
    'abstract':'adjective. Existing in thought or as an idea but not having a physical or concrete existence. Abstract concepts such as love or beauty',
    'integer':'noun. A number that is not a fraction; a whole number.',}

for word,meaning in glossary.items():
    print('\n'+ word.title() + ':')
    print('\t' + meaning)