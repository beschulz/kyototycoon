Performance
=======================================

The following is the output of benchmark.py it's a modified version of the benchmark that ships with pykt. As always, do not trust a benchmark, that you have not forged yourself.

The results::

	implementation          set             get            gets       increment         replace           total
	pykt        3.0184381008148 2.3861417770386 4.6767139434814 1.2522919178009 1.0413010120392 12.3748867511749
	kyototycoon 1.0114710330963 1.1232841014862 3.0113148689270 0.6714899539948 0.7781660556793 6.5957260131836
	pykt emu    0.9092319011688 0.6884479522705 2.6841168403625 0.6197800636292 0.6409928798676 5.5425696372986


- pykt: https://github.com/mopemope/pykt (outdated, does not pass its own tests anymore)
- kyototycoon: this module
- pykt emu: an pykt emulation layer provided by kyototycoon
