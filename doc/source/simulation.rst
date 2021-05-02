Simulation Model
================

Asian Hornet Life Cycle
-----------------------
To simulate the hornet population, it is first necessary to the hive life cycle. Asian giant hornet nesting follows a yearly cycle. Inseminated queens hibernate through the winter and emerge to feed in the spring. Queens that survive go on to build nests starting in April. A fully developed nest can house hundreds of hornets. In the Fall, the original queen will die and the male hornets mate with new queens. The new queens then leave to hibernate, with the rest of the nest dying in the winter.

Basic Hive Population Model
---------------------------
With this in mind, we can derive a simple model. Start by defining a few parameters. Let:

	| :math:`N_t` be the number of hives at year :math:`t`
	
	| :math:`p_s` be the probability that a hive survives long enough to produce mating queens
	
	| :math:`n_q` be the number of new queens produced by a hive
	
	| :math:`p_{qs}` be the probability that a new queen survives long enough to build a another hive

Then the expected number of hives for the next season will simply be:

	| :math:`N_{t+1} = N_t \cdot p_s \cdot n_q \cdot p_{qs}`

This doesn't tell us very much on its own. Only that the population will change by some factor each year.

Spatial Model
-------------

We can also include hive locations in our model. Using the confirmed sightings data, we start with a population of hives each at a prescribed latitude and longitude. Then for the next generation of hives, we calculate a new random location within the range of a new queen's flight. For each surviving new hive we choose a random angle :math:`\theta` and a random distance :math:`d`.

If latitude and longitude coordinates were a cartisian plane, then to calculate the new set of coordiates we might use:

	| :math:`Lat_{new} = Lat + d \cdot \cos{\theta} \cdot c`

	| :math:`Long_{new} = Long + d \cdot \sin{\theta} \cdot c`
	
Where :math:`c` is a constant that represents distance per degree. Degrees of longitude, however, represent different distances depending on whether you are near the euqator or a pole. So instead we have:

	| :math:`Lat_{new} = Lat + d \cdot \cos{\theta} \cdot c`

	| :math:`Long_{new} = Long + d \cdot \frac{\sin{\theta}}{\cos{(Lat)}} \cdot c`

It is also worth noting, however, that this is still not entirely accurate, since the surface of the Earth is curved. For our purposes though, this is good enough since we're working with relatively small distances.

Geography Model
---------------

Suppose we calculate a new hive location and find that it's in the ocean. Of course, a hornet wouldn't build a new nest in that case. To account for this correctly, we need to check each location. For this (and for visualizations), we used `GeoPandas <https://geopandas.org/>`_. Geography data in the form of a shapefile was taken from `here <https://www.sciencebase.gov/catalog/item/51bf5940e4b0eb321c798ec9>`_.

TODO...

Results
-------

TODO...

Model Analysis
--------------

TODO...
