# Conquer_Binance_NFT

### Motivation
I have gone around Opensea, Dappradar, ETH Chain to see their NFT (Non-Fungible Token) price and volume data. Unfortunately, all of them has very strict anti-websrcaper policy. Basically, I tried to pretend myself as a web browser, also trying to fill in the requested payload data, or trying to find some tricks/rules among the url links. None of them worked. Maybe they count on selling data to make money. You can chose to buy data API access from Opensea and DappRadar. 

Or you can choose to use selenium to deal with it, to the best of my knowledge, selenium + advanced knowledge of anti-captcha, can solve everything.

Here I give a modern method to deal with **Binance NFT data** (https://www.binance.com/zh-CN/nft/ranking?tab=collection&chain=ETH), if some one, have the need to deal with ETH chain or Opensea, and would like treat me several couple of coffee, I would consider spending more time. 

![Image text](https://github.com/Neural-Finance/Conquer_Binance_NFT/blob/main/fig/Binance-NFT-Page.png)


### Example
If we should rank() the price of stocks in the sample trading day. In order to let the neural network learn this operator, we have to let sample1 see the features belong to sample2. As metioned above, the traditional structure can't see the features belong to other sample. Thus, we should put all sample's data into one picture, and let it serves as X. The output should be all sample's value, which is Pred_Y. And the real factor value array should be Y. The mean squared error of Y and pred_Y, severs as loss function.


### Project Structure
```
Main.py --You can run it to train the network and test the data.
```

```
Data_processing.py --Built the figure data
```

```
Querry.py --a sub function for Data_processing, here, you can put in a formula, which produces x and y
```

```
Lenet.py --The neural network model structure (Tensorflow 1.3)
```

```
hyper_parameters.py --all the hyper-parameters
```

### Input X and Output Y
![Image text](https://github.com/Neural-Finance/Cross_sample_financial_feature_engineering/blob/master/fig/1.png)
![Image text](https://github.com/Neural-Finance/Cross_sample_financial_feature_engineering/blob/master/fig/2.png)
