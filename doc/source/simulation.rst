Simulation Model
================

Asian Hornet Life Cycle
-----------------------
To simulate a hornet population, it is first necessary to understand the hive life cycle. Asian giant hornet nesting follows a yearly cycle. Inseminated queens hibernate through the winter and emerge to feed in the spring. Queens that survive go on to build nests starting in April. A fully developed nest can house hundreds of hornets. In the Fall, the original queen will die and the male hornets mate with new queens. The new queens then leave to hibernate, with the rest of the nest dying in the winter.

Basic Hive Population Model
---------------------------
With the hornet life cycle in mind, we can derive a simple model. Start by defining a few parameters. Let:

	| :math:`N_t` be the number of hives at year :math:`t`
	
	| :math:`p_s` be the probability that a hive survives long enough to produce mating queens
	
	| :math:`n_q` be the number of new queens produced by a hive
	
	| :math:`p_{qs}` be the probability that a new queen survives long enough to build a another hive

Then the expected number of hives for the next season will simply be:

	| :math:`N_{t+1} = N_t \cdot p_s \cdot n_q \cdot p_{qs}`

This doesn't tell us very much on its own. Only that the population will change by some factor each year.

Spatial Model
-------------

We can also include hive locations in our model. Using the confirmed sightings data, we start with a population of hives each at a prescribed latitude and longitude. Then for each hive in the next generation of hives, we calculate a new random location within the range of a new queen's flight. For each surviving new hive we choose a random angle :math:`\theta` and a random distance :math:`d`.

If latitude and longitude coordinates were a cartisian plane, then to calculate the new set of coordinates we might use:

	| :math:`Lat_{new} = Lat + d \cdot \cos{\theta} \cdot c`

	| :math:`Long_{new} = Long + d \cdot \sin{\theta} \cdot c`
	
Where :math:`c` is a constant that represents distance per degree. Degrees of longitude, however, represent different distances depending on whether you are near the equator or a pole. So instead we have:

	| :math:`Lat_{new} = Lat + d \cdot \cos{\theta} \cdot c`

	| :math:`Long_{new} = Long + d \cdot \frac{\sin{\theta}}{\cos{(Lat)}} \cdot c`

It is also worth noting, however, that this is still not entirely accurate, since the surface of the Earth is curved. For our purposes though, this is good enough since we're working with relatively small distances.

Geography Model
---------------

Suppose we calculate a new hive location and find that it's in the ocean. Of course, a hornet wouldn't build a new nest in that case. To account for this correctly, we need to check each location. To address this (and for visualizations), `GeoPandas <https://geopandas.org/>`_ was used. Geography data in the form of a shapefile was taken from `here <https://www.sciencebase.gov/catalog/item/51bf5940e4b0eb321c798ec9>`_.

Shapefiles contain mainly sets of polygon coordinates. Depending on the underlying geography, these can become quite complicated. For locations with many small lakes or islands, there need to be many polygons. Since new set coordinates need to be compared with every polygon, this gets computationally expensive. So for these simulations, the goegraphy of only a few US and Canadian states was used, namely:

* British Columbia 
* Yukon 
* Alberta 
* Washington 
* Oregon 
* Idaho 
* Montana 
* Nevada 
* California 
* Utah 
* Wyoming 

It might be interesting to include more goegraphical features in the model. For instance, land cover `data <https://hub.arcgis.com/datasets/esri::world-land-cover>`_ could be used to determine whether a location was in a forested area or not. I may undertake this in the future, though I wasn't able to find a good set of such GIS data that was also free.

Model Assumptions
-----------------

One important assumption with these simulations is that dispersal only occurs naturally from young queens flying to new locations. This is mostly likely not the case since there have been sightings in North America many miles apart, in Vancouver Island and Washington State. As we will show, it would take several years for a naturally dispersing population to reach such a range. This indicates that the Asian giant hornet most likley had help from humans in dispersing. Nonetheless, we will proceed by assuming only short dispersal distances, since little is known about human interaction at this point. 

Two sets of parameters were used. The first makes very conservative assumptions about population growth:

	| :math:`N_0 = 5`

	| :math:`p_s = 0.4` 
	
	| :math:`n_q = 30`
	
	| :math:`p_{qs} = 0.1`

	| :math:`d_{max} = 5\text{km}`

The second makes more aggressive assumptions: 

	| :math:`N_0 = 10`

	| :math:`p_s = 0.6` 
	
	| :math:`n_q = 30`
	
	| :math:`p_{qs} = 0.15`

	| :math:`d_{max} = 10\text{km}`

Simulations were repeated 10 times for each set of parameters.

Results
-------

Plotting the hive populations from all simiulations, we see a wide range of possible outcomes:

.. image:: https://github.com/rustygentile/hornet-model/raw/main/images/simulation_results.png

Also worth noting, is that for the conservative parameters, most scenarios show the population dying out. This would indicate that not all hives in the wild necessarily need to be destroyed. If eradiaction efforts are only partially successful, this could still have a large impact on controlling the spread. This conclusion though, is heavily dependent on the actual initial population and our :math:`p_s` parameter.

Plotting the population of hives from selected simulations with geography provides another way to visualize the results: 

.. image:: https://github.com/rustygentile/hornet-model/raw/main/images/simulation_results_geo.png

Model Analysis
--------------

TODO...
