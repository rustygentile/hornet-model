Regression Model
================

Problem Statement
-----------------

Reported sightings can be classified as either a positive ID, a negative ID, or unverified. Positive ID's are those that have been verified to be Asian giant hornets by a lab. Negative ID's are those that have been determined to be another species. Unverified sightings have neither been confirmed nor denied. Given an unverified sighting, we are interested in predicting whether or not it is a positive ID.

.. image:: https://github.com/rustygentile/hornet-model/raw/main/images/training_data.png

Visualizing the data, we see many more reported sightings in 2020 than the previous year. This is no doubt due to the influence of the New York Times article.

Logistic Regression
-------------------

Since a positive or negative ID is a binary dependent variable, a logistic regression model would be a good choice. Given a set of dependent variables, logistic regression can be used to estimate the probability of a binary outcome. Since the number of sightings in 2020 is much greater than that of 2019, the data was divided as such and separate models were used for each year.

.. image:: https://github.com/rustygentile/hornet-model/raw/main/images/regression_results.png

Using only latitude and longitude as predictors, we can already produce a reasonable model.

Feature Generation
------------------

The model can be improved by coupling it with simulation results. Since new hives are not expected to be outside the flight range of pre-existing hives, distance can be good predictor. To calculate the distance between two sets of coordinates, the Haversine formula can be used:

    | :math:`a = \sin^2{(\frac{\phi_2 - \phi_1}{2})} + \cos{\phi_1}\cos{\phi_2}\sin^2{(\frac{\lambda_2 - \lambda_1}{2})}`
    
    | :math:`c = 2 \arctan_2{(\sqrt{a}, \sqrt{1 - a})}`

    | :math:`d = r \cdot c`

Here, :math:`\phi_1` and :math:`\phi_2` are the two latitude points in degrees, :math:`\lambda_1` and :math:`\lambda_2` are longitudes in degrees, and :math:`r` is the radius of the Earth.

To make use of this in a regression model, the distance between each unverified sighting was compared to a simulated population model. The minimum of these distances was used as an additional predictor variable. This yields a new regression model which is plotted along with the simulation results.

.. image:: https://github.com/rustygentile/hornet-model/raw/main/images/feature_generation.png  

Model Evaluation
----------------

Typically, data would be divided into training and validation to assess a regression model. In this case, however, positive ID data was quite sparse. A typical split might be to use 20% of a data set for validation. With only 14 positive ID's, this would make, rounding up, three positive cases to test. This is too few to be statistically significant.

A qualitative assessment however, shows the model with the distance feature to be an improvement. From the figures above, we can see high probabilities clustered closer to the simulated population in the latter model. These are closer to the confirmed sightings as well. Also, the feature generation model shows a wider range of probabilities in its predictions.
