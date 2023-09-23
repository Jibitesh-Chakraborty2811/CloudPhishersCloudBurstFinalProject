# CloudPhishersCloudBurstFinalProject <br>
## Level-1 : Finding Probability of Cloud Burst occuring a particular week based on rainfall departure of past 14 weeks
**Approach : Used a custom CNN-LSTM Architecture for the purpose** <br>
Used 1D Convolutions to extract relevant features from a time series data of weekly departures stretching over a period of 14 weeks. <br>
The resultant sequence is fed to a LSTM of 100 units to form an encoded vector. <br>
The encoded vector is further fed to a fully connected neural network for classification. 
**Accuracy : 97%**

## Level-2 : Monitoring images of clouds to find exactly when cloudburst would occur
**Aproach : Custom CNN model which takes images of clouds and gives a probability of cloud burst** <br>
**Accuracy : 98%**
