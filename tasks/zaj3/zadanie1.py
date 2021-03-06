# -*- coding: utf-8 -*-


def load_data(path):
    """
    Funkcja która ładuje dane z pliku zawierającego ngramy. Plik ten jest
    plikiem csv zawierającym n-gramy.

    Tak w ogóle tutaj możecie "zaszaleć" i np. nie zwracać list a jakieś
    generatory żeby mniej pamięci zużywać.

    Do testów tej funkcji i tam wynik tej funkcji zostanie potraktowany tak:

    >>> data = load_data('foo')
    >>> data = [list(data[0]), list(data[1])]

    :param str path: Ścieżka
    :return: Lista dwuelementowych krotek, pierwszym elementem jest ngram, drugim
    ilość wystąpień ngramu
    """


def suggester(input, data):
    """
    Funkcja która sugeruje następną literę ciągu ``input`` na podstawie n-gramów
    zawartych w ``data``.

    :param str input: Ciąg znaków o długości 6 znaków lub mniejszej
    :param list data: Data jest krotką zawierającą dwie listy, w pierwszej liście
                      zawarte są n-gramy w drugiej ich częstotliwości.
                      Częstotliwość n-gramu data[0][0] jest zawarta w data[0][1]

    :return: Listę która zawiera krotki. Pierwszym elementem krotki jest litera,
             drugim prawdopodobieństwo jej wystąpienia. Lista jest posortowana
             względem prawdopodobieństwa tak że pierwszym elementem listy
             jest krotka z najbardziej prawdopodobną literą.

    Przykład implementacji
    ----------------------

    By wygenerować częstotliwości należy:

    Dla ustalenia uwagi zakładamy ze input zawiera ciąg znaków `foo`

    1. Odnaleźć pierwsze wystąpienie ngramu rozpoczynającego się od wartości
       ``foo``. Tutaj polecam algorytm przeszukiwania binarnego i moduł
       ``bisect``.
    2. Znaleźć ostatnie wystąpienie ngramu. Tutaj można albo ponownie przeszukać 
       binarnie, albo założyć po prostu przeszukać kolejene elementy listy.

       .. note::

            Kroki 1 i 2 można zastąpić mało wydajnym przeszukiwaniem naiwnym,
            tj. przeiterować się po liście i jeśli ciąg znakóœ rozpoczyna się od
            'foo' (patrz: https://docs.python.org/3.4/library/stdtypes.html#str.startswith)
            zapamiętujemy go

    3. Stworzyć słownik który odwzorowuje następną literę (tą po `foo`) na
       ilość wystąpień. Pamiętaj że w data może mieć taką zawartość 
       ``[['fooabcd', 300], ['fooa    ', 300]]`` --- co w takim wypadku w słowniku tym
       powinno być {'a': 600}.

    4. Z tego słownika wyznaczyć prawdopodobieństwo wystąpienia kolejnej litery.

    Przykład zastosowania:

    >>> data = load_data("path")
    >>> suggester('ąęćś', data)
    []
    >>> suggester('pytho', data)
    [('n', 1.0)]
    >>> suggester('pyth', data)
    [('o', 0.7794117647058824),
     ('a', 0.1323529411764706),
     ('e', 0.07352941176470588),
     ('i', 0.014705882352941176)]
    """
