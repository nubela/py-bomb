"""---------------------
========================
Rationale behind py-bomb
========================

(This is an exercise in crafting the directives and specifications of this project via elaboration on the rationality behind py-bomb.)
This project seeks to answer the needs of having to run a script every X duration, primarily python functions/scripts.

It needs to be

* Super simple to add functions to be run
Enough said.

* Non-blocking so it runs everything it needs to run
It should run all functions, even if there is 1 that blocks.

* All scripts end eventually
That is to say, functions should timeout.
---------------------"""