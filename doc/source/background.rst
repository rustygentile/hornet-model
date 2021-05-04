Background
==========

Introduction
------------

The Asian giant hornet saw significant attention in 2020. This attention is mainly due to a New York Times `article <https://www.nytimes.com/2020/05/02/us/asian-giant-hornet-washington.html/>`_ that went viral. Since publication, the number of reported sightings in the northwest spiked. While some of these have been positively identified as Asian giant hornets, most of them are cases where another species was mistakenly reported.

.. image:: https://github.com/rustygentile/hornet-model/raw/main/images/sightings.png

As their name suggests, the Asian giant hornet is not native to North America. The species is potentially invasive and as the Times article notes, we may have a limited window of opportunity to eradicate it.

The goal of this effort is to develop a model that can aid in classifying reported sightings. Since most sightings are false ID's, scientists would like to be able to prioritize which sightings warrant further investigation. To this end, two modelling approaches are used here. First, a simulation was developed which models a population of hornet hives in the northwest. Second, a logistic regression model was created which estimates the probability that a reported sighting is real.

Data Sets
---------

Data for the models in this project was taken from the Consortium for Mathematics and Its Applications (COMAP) Mathematical Contest in Modeling (MCM). The main project data set can be downloaded from `here <https://www.comap.com/undergraduate/contests/mcm/contests/2021/problems/2021_MCM_Problem_C_Data.zip>`_ . This data set catalogues sightings of Asian giant hornets in North America reported by the general public. Data is organized in the following columns:

================  ==============================================================
Column            Description
================  ==============================================================
GlobalID          Unique identifier for each data entry.
Detection Date    When the sighting occurred.
Submission Date   When the sighting was reported to officials.
Latitude          Location of the sighting.
Longitude         Location of the sighting.
Notes             Provided by the reporter.
Lab Status        'Positive ID', 'Negative ID', 'unverified', or 'unprocessed'
Lab Comments      Feedback from the lab.
================  ==============================================================

There are 4440 rows of data with not every field containing an entry. Sightings are confined mainly to the Northwest United States (Washington) and British Columbia, Canada.

A geography shapefile taken from `here <https://www.sciencebase.gov/catalog/item/51bf5940e4b0eb321c798ec9>`_ was also used.
