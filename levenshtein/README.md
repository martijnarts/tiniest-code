# Levenshtein Distance

The Levenshtein distance is a useful measure of difference between two strings.
It could be described as the number of steps required to get from one string to
another using additions, substitutions and removals.

## Example

To get from the string *cat* to the string *scent* would require the following
steps:

* *cat*
* *scat* (Addition of *s*)
* *scet* (Substitution of *a* by *e*)
* *scent* (Addition of *n*)

This requires three steps and as such the Levenshtein distance is equal to
three.

## Parameters

* `a` and `b`  
   The two string between which the distance should be calculated.
