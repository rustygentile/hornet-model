Background
==========

The Asian giant hornet saw significant attention in 2020. This attention is mainly due to a New York Times `article <https://www.nytimes.com/2020/05/02/us/asian-giant-hornet-washington.html/>`_ that went viral. Since publication, the number of reported sightings in the northwest spiked. While some of these have been positively identified as Asian giant hornets, most of them are cases where another species was mistakenly reported.

.. image:: https://github.com/rustygentile/hornet-model/raw/main/images/sightings.png

As their name suggests, the Asian giant hornet is not native to North America. The species is potentially invasive and as the Times article notes, we may have a limited window of opportunity to eradicate it.

The goal of this effort is to develop a model that can aid in classifying reported sightings. Since most sightings are false ID's, scientists would like to be able to prioritize which sightings warrant further investigation. To this end, two modelling approaches are used here. First, a simulation was developed which models a population of hornet hives in the northwest. Second, a logistic regression model was created which estimates the probability that a reported sighting is real.

